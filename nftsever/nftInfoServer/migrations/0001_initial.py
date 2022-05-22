# Generated by Django 4.0.4 on 2022-05-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nftCardsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, default=None, max_length=100, null=True, verbose_name='获取价格的时间')),
                ('lowestPrice', models.IntegerField(blank=True, default=None, null=True, verbose_name='当前最低价格')),
                ('lockNum', models.IntegerField(blank=True, default=None, null=True, verbose_name='当前锁单量')),
                ('goodName', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='商品名称')),
            ],
            options={
                'verbose_name': 'nft实时信息',
                'verbose_name_plural': 'nft实时信息',
            },
        ),
    ]
