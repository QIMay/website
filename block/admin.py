from django.contrib import admin

from .models import Block

#Django提供admin来进行站点管理

class BlockAdmin(admin.ModelAdmin):
    list_display=("block_name","block_description","manager_name","block_status")
    #/admin/block/block/中显示的内容列
admin.site.register(Block,BlockAdmin)