from rest_framework import serializers
from .models import nftCardsInfo




class nftCardsInfoSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(required=False, allow_null=True)
    lowestPrice = serializers.IntegerField(required=False, allow_null=True)
    lockNum = serializers.IntegerField(required=False, allow_null=True)
    goodName = serializers.CharField(required=False, allow_null=True)


    def create(self, validated_data):
        """新建"""
        return nftCardsInfoSerializer(**validated_data)

    def update(self, instance, validated_data):
        """
        根据提供的验证过的数据更新和返回一个已经存在的``实例。
        """
        instance.time = validated_data.get('time', instance.time)
        instance.lowestPrice = validated_data.get('lowestPrice', instance.lowestPrice)
        instance.lockNum = validated_data.get('lockNum', instance.lockNum)
        instance.goodName = validated_data.get('goodName', instance.goodName)
        instance.save()
        return instance

    class Meta:
        model = nftCardsInfo
        # fields = "__all__"
        fields = ["time", 'lowestPrice', 'lockNum', 'goodName']