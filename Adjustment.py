import pandas as pd
import numpy as np
import pickle
import random



#一.M为所有检测的因子的个数
M =300


#二.生成(0,0.05)之间的随机数，作为数组存储起来
p_value=np.zeros(M)
for i in range(M):
    p_value[i]= random.uniform(0,1)/20


#三.生成显著性水平：0.05
#FWER
Alpha_w = 0.05
#FDR
Alpha_d = 0.05


#四.产生调整后的显著性水平
#1.Bonferroni's adjustment
Alpha_w_B_ad = Alpha_w/M    #p_value 中所有小于等于Alpha_w_H_ad的P值对应的因子有效

#2.Holm's adjustment
#1)首先对所有的P值进行排序，默认从小到大
sorted_p = sorted(p_value)
#2)进行序列调整，找到合理的临界值
k=0
for j,p in enumerate(sorted_p):
    if p>Alpha_w/(M+1-(j+1)):
        k=j
        break
Alpha_w_H_ad= sorted_p[k-1]  #sorted_p 中所有小于等于Alpha_w_H_ad的P值对应的因子有效

#3.BHY's adjustment
#1)首先对所有的P值进行排序，默认从小到大
sorted_p_ = sorted(p_value)
#2)计算调整项C(M)
C=0
for m in range(M):
    C=C+1/(m+1)
#3)进行序列调整，找到合理的临界值
k_=0
for j,p in enumerate(sorted_p_):
    if p<=(Alpha_d*(j+1))/(C*M):
        k=j
        break
Alpha_d_BHY_ad = sorted_p_[k]  #sorted_p_ 中所有小于等于Alpha_w_BHY_ad的P值对应的因子有效
