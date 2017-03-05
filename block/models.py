from django.db import models

class Block(models.Model):
    block_name = models.CharField("板块名称",max_length=100)
    block_description = models.CharField("板块描述",max_length=100)
    manager_name = models.CharField("管理员名称",max_length=100)
    block_status = models.IntegerField("状态",choices=((0,"正常"),(-1,"删除")))

    def __str__(self):
        return self.block_name
    class Meta:
        verbose_name = "各板块信息"
        verbose_name_plural = "板块集合"