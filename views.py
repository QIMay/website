from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User


def index(request):
    block_infos = Block.objects.filter(block_status=0).order_by("-id")
    # block_infos的值为Block类(写在block.models里面)下面block_status为0(0代表正常)的对象
    # 显示的内容由admin管理,写在block.admin里面
    return render(request, "index.html", {"blocks": block_infos})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['re_password'].strip()

        if not username or not email or not password:
            return render(request,"register.html",{"error":"字段不能为空","username":username,"email":email})
        if len(username) > 100:
            return render(request,"register.html",{"error":"用户名太长"})
        if password!=re_password:
            return render(request,"register.html",{"error":"两次输入的密码不一致","username":username,"email":email})

        user = User.objects.create_user(username=username,email=email,password=password)
        user.is_active = True
        user.save()

        return render(request, "success.html")

