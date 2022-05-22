import pprint
import json
import time
import matplotlib.pyplot as plt
import requests.packages
plt.ion()
plt.figure(1)
headers = {
    'user-agent': 'iBoxApp',
    'ib-app-version': '1.1.4',
    'ib-device-id': 'ffffffff-f85e-ce29-ffff-ffffef05ac4a_ad',
    'host': 'api-app.ibox.art',
    'content-type': 'application/json;charset=UTF-8',
    'ib-trans-id': '28914632-9888-5081-a114-5dde8cb9908e_flutter',
    'wtoken': 'e447_GmOJR8Czv9ixprMXWcdrf6kg/bKsm6rK0GyRwura72og2LUhLe7AmJCHDAvubJCv7C4E3i2Ey0FtzdnE92dhXGTq7MVbUPlR8QqSOC6EL7u6RHOWyuPC/wb4gOp0KCWNevfyggcN3eisIeM1uYk9rjd+gP9sm1b4KaL7K4a+Kh3lKOlR59DCBXMe01pFBn9cnU6zyyM21lu+X7uM6YTINqzfzxLyL4oPSP4HNA5vneFWdN8Q9dsKo5XWXM7megmAyw7yARXVk/ZN5JuOSuV9c8DyqdMELoAVeH0ImvLprHS5fz2w7qd9jm2hy3dwqOgddmZvBkxuFiIpmrvg+JiE8/XZwZ3EuwgoVhZMnew4eCM7IkeBO0za99suLA850IRFqKvbt2yTcYIZ/PNfQnwsRSXa0hpeqWjeCzflLft1mBIkuTu3azhZtn/eyNk38tmxThkPonUUTezIYwLNgNhqfvHWDHyB0wc7uBu4MuoeNnRPXKJXQ48hYL/Yf9yZ749k720ZSnEMYVe7uOrCdQYl0T9f0M4V92mMwL0RZSFUiaPykg2uNPpZSAaT58aTSHWM&b7ee_80E143AC5AE41D33F3C808B80799A7324A8AC734AC98828B5E',
    'ib-platform-type': 'android',
    'hb-nft-token': 'ZJkV1cNC5UxDB5TEgacXeIKFcvN4JJZlCjNdyOH3p6k=',
    'ib-user-token': 'ZJkV1cNC5UxDB5TEgacXeIKFcvN4JJZlCjNdyOH3p6k='
}
dataBorder = {
    'albumId': '100513726',
    'page': '1',
    'pageSize': '100',
    'order': '1',
    'onSale': '1'
}
dataShibalnu = {
    'albumId': '100513831',
    'page': '1',
    'pageSize': '100',
    'order': '1',
    'onSale': '1'
}
dataTerrier = {
    'albumId': '100513863',
    'page': '1',
    'pageSize': '100',
    'order': '1',
    'onSale': '1'
}
url = 'https://api-app.ibox.art/nft-mall-web/v1.2/nft/product/getProductListByAlbumId'
p1time = []
p2time = []
p3time = []
priceBorder = []
priceShibalnu = []
priceTerrier=[]
while(1):
    try:
        resBorder = requests.get(url=url, headers=headers, params=dataBorder,verify=False)
        resShibalnu = requests.get(url=url, headers=headers, params=dataShibalnu, verify=False)
        resTerrier = requests.get(url=url, headers=headers, params=dataTerrier, verify=False)
        # print("Border:{},Shibalnu:{},Terrier:{}".format(resBorder.status_code,resShibalnu.status_code,resTerrier.status_code))
        if resBorder.status_code == 200 and resShibalnu.status_code == 200:
            dictBorder = json.loads(resBorder.text)
            dictShibalu = json.loads(resShibalnu.text)
            dictTerrier =json.loads(resTerrier.text)
            # print("Border:{},Shibalnu:{},Terrier:{}".format(dictBorder['code'], dictShibalu['code'], dictTerrier['code']))
            if dictBorder['code'] == 1 and dictShibalu['code'] == 1 and dictTerrier['code'] == 1:
                # print("Border:{},Shibalnu:{},Terrier:{}".format(dictBorder['code'], dictShibalu['code'],dictTerrier['code']))
                listBorder = dictBorder['data']['list']
                listShibalnu = dictShibalu['data']['list']
                listTerrier =dictTerrier['data']['list']
                flag = False
                for info in listBorder:
                    if info['gStatus'] != 16:
                        priceBorder.append(int(info['priceCny']))
                        p1time.append(time.strftime('%H:%M:%S', time.localtime(time.time())))
                        print('当前赛博边牧的价格:{}'.format(info['priceCny']))
                        break

                for info in listShibalnu:
                    if info['gStatus'] != 16:
                        priceShibalnu.append(int(info['priceCny']))
                        p2time.append(time.strftime('%H:%M:%S', time.localtime(time.time())))
                        print('当前赛博柴犬的价格:{}'.format(info['priceCny']))
                        break

                for info in listTerrier:
                    if info['gStatus'] != 16:
                        priceTerrier.append(int(info['priceCny']))
                        p3time.append(time.strftime('%H:%M:%S', time.localtime(time.time())))
                        print('当前孙红雷的价格:{}'.format(info['priceCny']))
                        break
                p1 = plt.subplot(3, 1, 1)
                p1.plot(p1time, priceBorder, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
                p1.set_ylabel("Border",fontsize =14)

                p2 = plt.subplot(3, 1, 2)
                p2.plot(p2time, priceShibalnu, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
                p2.set_ylabel("Shibalnu", fontsize=14)
                time.sleep(2)

                p3 = plt.subplot(3, 1, 3)
                p3.plot(p3time, priceTerrier, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
                p3.set_ylabel("Terrier", fontsize=14)
                time.sleep(2)
                plt.pause(0.1)
    except Exception as e:
        print("错误信息:{}".format(e))
# res = requests.get(url=url, headers=headers, params=dataBorder,verify=False)
# print(res.text)
