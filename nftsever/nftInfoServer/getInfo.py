from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import json
import time
# import matplotlib.pyplot as plt
from .db_operate import update_db
from .config import goods

option =ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument('--no-sandbox')
option.add_argument('--disable-gpu')
option.add_argument('blink-settings=imagesEnabled=false')
option.add_argument('--headless')

from .config import goods

# from config import goods


def getCommodityInfo(id="100513726"):
    driver = webdriver.Chrome(options=option, executable_path='/home/lighthouse/chromedriver')
    # driver = webdriver.Chrome(options=option)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    # driver = webdriver.Chrome()
    driver.get("https://www.ibox.art/zh-cn/item/group/?id={}".format(id))
    sleep(3)
    items = driver.find_elements(by=By.XPATH, value="//tbody/tr")
    res = []
    for i in items:
        res.append((i.find_element(by=By.XPATH, value="td[@class = 'col-status']/div").text,
                    int(i.find_element(by=By.XPATH, value="td[@class = 'col-price']").text.split(" ")[-1])))
    driver.close()
    driver.quit()
    return res


def getLowestPrice(info):
    flag = False
    for i in info:
        if i[0] == "寄售":
            return (i[1])
            flag = True
            break
    if flag == False:
        return (info[-1][1])


def getNumOfLock(info):
    num = 0
    for i in info:
        if i[0] == "锁定中":
            num += 1
    return num


def getCardsInfo(good):
    try:
        res = getCommodityInfo(goods[good])
        price = getLowestPrice(res)
        locknum = getNumOfLock(res)
        data={
            "time": time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(time.time())),
            "lowestPrice": price,
            "lockNum": locknum,
            "goodName": good
        }
        print(data)
        return data
    except Exception as e:
        print("错误信息1:{}".format(e))
    # print('当前边牧的价格:{}'.format(price))
    # print('当前锁单量:{}'.format(locknum))


"""

画图

"""
# res = getCommodityInfo()
# print(getLowestPrice(res))
# print(getNumOfLock(res))
# import matplotlib.pyplot as plt
# p1time = []
# priceBorder = []
# locknums = []
# while(1):
#     try:
#         try:
#             res = getCommodityInfo()
#             price = getLowestPrice(res)
#             locknum = getNumOfLock(res)
#         except Exception as e:
#             print("错误信息1:{}".format(e))
#             continue
#         priceBorder.append(price)
#         locknums.append(locknum)
#         p1time.append(time.strftime('%H:%M:%S', time.localtime(time.time())))
#         print('当前边牧的价格:{}'.format(price))
#         print('当前锁单量:{}'.format(locknum))
#
#         p1 = plt.subplot(2, 1, 1)
#         p1.plot(p1time, priceBorder, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
#         p1.set_ylabel("price",fontsize =14)
#
#         p2 = plt.subplot(2, 1, 2)
#         p2.plot(p1time, locknums, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
#         p2.set_ylabel("locknum", fontsize=14)
#
#         plt.pause(0.1)
#     except Exception as e:
#         print("错误信息2:{}".format(e))
