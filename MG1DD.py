# -*- coding: utf-8 -*-
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

la = 0.4
mu = 0.9
len_customer = 10000
repeat_size = 50

def DD(la, mu, len_customer):
    # arrive time
    arr_time = []
    for i in range(len_customer):
        arr_time.append(0.0)
    for i in range(len_customer):
        if i == 0:
            arr_time[i] = 0.0
        else:
            arr_time[i] = arr_time[i - 1] + random.expovariate(la)

    # serve distribution
    # Deterministic Distribution-----------------------------------------
    ser_time = []
    for i in range(len_customer):
        ser_time.append(0.0)

    for i in range(len_customer):
        ser_time[i] = 1/mu

    # -------------------------------------------------------------------

    # leave time
    lea_time = []
    for i in range(len_customer):
        lea_time.append(0.0)
    for i in range(len_customer):
        if i == 0:
            lea_time[i] = arr_time[i] + ser_time[i]
        else:
            if lea_time[i - 1] < arr_time[i]:
                lea_time[i] = arr_time[i] + ser_time[i]
            else:
                lea_time[i] = lea_time[i - 1] + ser_time[i]

    # time line
    moment = np.zeros(2 * len_customer, dtype=np.float32)
    customer_num = np.zeros(2 * len_customer, dtype=np.float32)
    arr = 1
    lea = 1
    counter = 1
    while (arr <= len_customer - 1):
        if (arr_time[arr] < lea_time[lea]):
            moment[counter] = arr_time[arr]
            customer_num[counter] = customer_num[counter - 1] + 1
            counter = counter + 1
            arr = arr + 1
        else:
            moment[counter] = lea_time[lea]
            customer_num[counter] = customer_num[counter - 1] - 1
            counter = counter + 1
            if (lea < len_customer - 1):
                lea = lea + 1
    moment[counter] = lea_time[len_customer - 1]

    # simulating result
    total_Ls = 0
    total_Lq = 0
    total_Ws = 0
    total_Wq = 0
    for i in range(len_customer):
        total_Ws += (lea_time[i] - arr_time[i])
    sim_Ws = total_Ws / (len_customer)

    for i in range(len_customer):
        total_Wq += (lea_time[i] - arr_time[i] - ser_time[i])
    sim_Wq = total_Wq / (len_customer)

    for k in range(1, 2 * len_customer):
        if (moment[k + 1] == 0):
            break
        total_Ls = customer_num[k] * (moment[k + 1] - moment[k]) + total_Ls
    sim_Ls = total_Ls / (lea_time[-1] - arr_time[1])

    for k in range(1, 2 * len_customer):
        if (moment[k + 1] == 0):
            break
        if (customer_num[k] >= 2):
            total_Lq = (customer_num[k] - 1) * (moment[k + 1] - moment[k]) + total_Lq
    sim_Lq = total_Lq / (lea_time[-1] - arr_time[1])

    sim_result = [sim_Ws, sim_Wq, sim_Ls, sim_Lq]
    return sim_result

repeat_results = np.zeros((4, repeat_size), dtype=np.float32)

# Ws:0  Wq:1  Ls:2  Lq:3
for k in range(0, repeat_size):
    temp = DD(la, mu, len_customer)
    repeat_results[0][k] = temp[0]
    repeat_results[1][k] = temp[1]
    repeat_results[2][k] = temp[2]
    repeat_results[3][k] = temp[3]

# theory result
# DD-----------------------------------------------------------------
Ws = (2 * mu - la) / (2 * mu * (mu - la))
Wq = la / (2 * mu * (mu - la))
Ls = (2 * mu * la - la * la) / (2 * mu * mu - (2 * la * mu))
Lq = la * la / (2 * mu * (mu - la))


# -------------------------------------------------------------------


def Mystd(data, ave):
    sum_num = 0.0
    for num in data:
        sum_num = sum_num + (num - ave) * (num - ave)
    #    result = cmath.sqrt(sum_num/len(data))
    result = (sum_num / len(data)) ** 0.5
    return result


def Myvar(data, ave):
    sum_num = 0.0
    for num in data:
        sum_num = sum_num + (num - ave) * (num - ave)
    result = sum_num / len(data)
    return result


# Confidence Interval
stlist = [Mystd(repeat_results[0], Ws), Mystd(repeat_results[1], Wq), Mystd(repeat_results[2], Ls),
          Mystd(repeat_results[3], Lq)]
error = []
n = repeat_size
for st in stlist:
    error.append(1.96 * (st / (n ** 0.5)))

# results
print("    Theory | Average of Repeat Simulation | Standard Deviation | Variance | CI Error")
print("Ws: %.4f " % Ws, "            %.4f            " % np.mean(repeat_results[0]),
      "      %.4f      " % Mystd(repeat_results[0], Ws), "    %.4f " % Myvar(repeat_results[0], Ws),
      "   %.4f " % error[0])
print("Wq: %.4f " % Wq, "            %.4f            " % np.mean(repeat_results[1]),
      "      %.4f      " % Mystd(repeat_results[1], Wq), "    %.4f " % Myvar(repeat_results[1], Wq),
      "   %.4f " % error[1])
print("Ls: %.4f " % Ls, "            %.4f            " % np.mean(repeat_results[2]),
      "      %.4f      " % Mystd(repeat_results[2], Ls), "    %.4f " % Myvar(repeat_results[2], Ls),
      "   %.4f " % error[2])
print("Lq: %.4f " % Lq, "            %.4f            " % np.mean(repeat_results[3]),
      "      %.4f      " % Mystd(repeat_results[3], Lq), "    %.4f " % Myvar(repeat_results[3], Lq),
      "   %.4f " % error[3])


# diagram
x = np.linspace(1, repeat_size, repeat_size)
Ws_line = np.zeros(repeat_size, dtype=np.float32)
for k in range(0, repeat_size):
    Ws_line[k] = Ws
Wq_line = np.zeros(repeat_size, dtype=np.float32)
for k in range(0, repeat_size):
    Wq_line[k] = Wq
Ls_line = np.zeros(repeat_size, dtype=np.float32)
for k in range(0, repeat_size):
    Ls_line[k] = Ls
Lq_line = np.zeros(repeat_size, dtype=np.float32)
for k in range(0, repeat_size):
    Lq_line[k] = Lq

plt.subplot(221)
ax1 = plt.gca()
# ax1.yaxis.set_major_locator(MultipleLocator(0.05))
plt.title('Distribution for Ws')
plt.xlabel('Repeat num')
plt.ylabel('Value')
plt.plot(x, repeat_results[0], 'r', linewidth=1, c='r')
plt.plot(x, Ws_line, 'r', linewidth=1, c='#000000')
####
plt.subplot(222)
ax2 = plt.gca()
# ax2.yaxis.set_major_locator(MultipleLocator(0.05))
plt.title('Distribution for Wq')
plt.xlabel('Repeat num')
plt.ylabel('Value')
plt.plot(x, repeat_results[1], 'r', linewidth=1, c='y')
plt.plot(x, Wq_line, 'r', linewidth=1, c='#000000')
plt.show()
###
plt.subplot(223)
# ax3=plt.gca()
# ax3.yaxis.set_major_locator(MultipleLocator(0.05))
plt.title('Distribution for Ls')
plt.xlabel('Repeat num')
plt.ylabel('Value')
plt.plot(x, repeat_results[2], 'r', linewidth=1, c='g')
plt.plot(x, Ls_line, 'r', linewidth=1, c='#000000')
###
plt.subplot(224)
# ax4=plt.gca()
# ax4.yaxis.set_major_locator(MultipleLocator(0.05))
plt.title('Distribution for Lq')
plt.xlabel('Repeat num')
plt.ylabel('Value')
plt.plot(x, repeat_results[3], 'r', linewidth=1, c='b')
plt.plot(x, Lq_line, 'r', linewidth=1, c='#000000')
plt.show()