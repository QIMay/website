from django.shortcuts import render
from block.models import Block

def index(request):
    block_infos=Block.objects.filter(block_status=0).order_by("-id")
    #block_infos的值为Block类(写在block.models里面)下面block_status为0(0代表正常)的对象
    #显示的内容由admin管理,写在block.admin里面
    return render(request,"index.html",{"blocks":block_infos})

