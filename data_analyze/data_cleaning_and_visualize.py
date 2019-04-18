import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取.csv文件数据
data = pd.read_csv("F:\\craw\\bookpjt\\csvFile.csv", encoding='ANSI')

# 选定评论数的列值大于10其小于1000的行,选定价格小于200的行
Data = data[data['price']<200]
data0 = Data[Data['comnum']>10]
data1 = data0[data0['comnum']<1000]

# print(data1.loc[:,"comnum"])

#画散点图（横轴：价格，纵轴：评论数）
#设置图框大小
fig = plt.figure(figsize=(10,6))
plt.plot(data1['price'],data1['comnum'],"o")
#展示x，y轴标签
plt.xlabel('price')
plt.ylabel('comnum')
plt.show()

fig = plt.figure(figsize=(10,6))
#初始化两个子图，分布为一行两列
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#绘制箱型图
ax1.boxplot(data1['price'].values)
ax1.set_xlabel('price')
ax2.boxplot(data1['comnum'].values)
ax2.set_xlabel('comnum')
#设置x，y轴取值范围
ax1.set_ylim(0,150)
ax2.set_ylim(0,1000)
plt.show()

#删除价格￥100以上，评论数800以上的数据
data2=data1[data['price']<100]
data3=data2[data2['comnum']<700]
#data3为异常值处理后的数据
fig = plt.figure(figsize=(10,6))
plt.plot(data3['price'],data3['comnum'],"o")
plt.xlabel('price')
plt.ylabel('comnum')
plt.show()

#数据可视化
pricemax=data2['price'].max()
pricemin=data2['price'].min()
commentmax=data3['comnum'].max()
commentmin=data3['comnum'].min()
##计算极差
pricerg=pricemax-pricemin
commentrg=commentmax-commentmin
#组距=极差/组数
pricedst=pricerg/60
commentdst=commentrg/60
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#绘制价格直方图
#numpy.arrange(最小,最大,组距)
pricesty=np.arange(pricemin,pricemax,pricedst)
ax1.hist(data2['price'],pricesty,rwidth=0.6)
ax1.set_title('price')
#绘制评论数直方图
commentsty=np.arange(commentmin,commentmax,commentdst)
ax2.hist(data2['comnum'],commentsty,rwidth=0.6)
ax2.set_title('comnum')
plt.show()