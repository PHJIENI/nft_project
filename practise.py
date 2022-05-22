import time
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
plt.figure(1)
t_list = []
result_list = []
print(time.strftime('%H:%M:%S',time.localtime(time.time())))
while True:
    t_list.append(time.strftime('%H:%M:%S',time.localtime(time.time())))
    result_list.append(1)
    plt.subplot(1,2,1)
    plt.plot(t_list, result_list,c='r',ls='-', marker='o', mec='b',mfc='w') ## 保存历史数据
    plt.subplot(1,2,2)
    plt.plot(t_list, result_list, c='r', ls='-', marker='o', mec='b', mfc='w')
    #plt.plot(t, np.sin(t), 'o')
    plt.pause(0.1)
