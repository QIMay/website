from django.shortcuts import render
from .models import ActivateCode
from django.utils import timezone

def activate(request,code):
    query = ActivateCode.objects.filter(code=code,expire_timestamp__gte=timezone.now())
    if query.count() > 0:
        user_activate_info = query[0]
        user_activate_info.owner.is_active = True
        user_activate_info.owner.save()
        return render(request,"success.html",{"msg":"激活成功","link":"#","hint":"去登陆"})
    else:
        return render(request,"success.html",{"msg":"激活失败"})


