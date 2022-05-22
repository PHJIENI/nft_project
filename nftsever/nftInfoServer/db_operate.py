from .serializers import nftCardsInfoSerializer
from .models import nftCardsInfo
import copy

def update_db(record):
    # 更新数据库/重写这条记录
    print("开始更新数据库：{}".format(record))
    temp = copy.deepcopy(record)
    serializer = nftCardsInfoSerializer(nftCardsInfo(), data=temp)
    if serializer.is_valid():
        try:
            serializer.save()
            print("success")
            # logger.info("success")
        except BaseException as e:
            print("fail1:{}".format(e))
    else:
        print("fail:{}".format(serializer.errors))
        # logger.info("fail:{}".format(serializer.errors))