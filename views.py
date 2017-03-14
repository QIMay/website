from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User
from activate.models import ActivateCode
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
import uuid


def index(request):
    block_infos = Block.objects.filter(block_status=0).order_by("-id")
    # block_infos的值为Block类(写在block.models里面)下面block_status为0(0代表正常)的对象
    # 显示的内容由admin管理,写在block.admin里面
    return render(request, "index.html", {"blocks": block_infos})


def register(request):
    error = ""
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['re_password'].strip()

        if not username or not email or not password:
            error = "字段不能为空"
        if password!=re_password:
            error = "两次输入的密码不一致"
        if User.objects.filter(username=username).count()>0:
            error = "用户名已存在"
        if User.objects.filter(email=email).count()>0:
            error = "该邮箱已注册"

        if not error:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.is_active = False
            user.save()

            new_code = str(uuid.uuid4()).replace("-","")
            expire_time = timezone.now() + timedelta(days=3)
            user_activate_info = ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
            user_activate_info.save()

            activate_link = "http://%s/activate/%s" %(request.get_host(),new_code)
            activate_email ='''点击<a href="%s">这里</a>激活'''%activate_link
            send_mail(subject = '[Python Club]激活邮件',
                      message = '点击链接激活:%s'%activate_link,
                      html_message = activate_email,
                      from_email = '404457494@qq.com',
                      recipient_list = [email],
                      fail_silently = False)

            return render(request, "success.html",{"msg":"您已注册成功,请登录邮箱验证"})
        else:
            return render(request,"register.html",{"error":error,"username":username,"email":email})

