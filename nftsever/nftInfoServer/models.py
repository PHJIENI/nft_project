from django.db import models

# Create your models here.
# python manage.py makemigrations 和 python manage.py migrate

class nftCardsInfo(models.Model):
    time = models.DateTimeField(max_length=100, blank=True, null=True, default=None, verbose_name="获取价格的时间")
    lowestPrice = models.IntegerField(blank=True, null=True, default=None,verbose_name="当前最低价格")
    lockNum = models.IntegerField(blank=True, null=True, default=None, verbose_name="当前锁单量")
    goodName = models.CharField(max_length=100,blank=True, null=True,default=None, verbose_name="商品名称")
    class Meta:
        # 数据库
        verbose_name = "nft实时信息"
        verbose_name_plural = verbose_name