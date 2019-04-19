import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 读取.csv文件数据
data = pd.read_csv("F:\\craw\\bookpjt\\csvFile.csv", encoding='ANSI')

# 选定评论数的列值大于15其小于1000的行,选定价格小于300的行
Data = data[data['price']<300]
data0 = Data[Data['comnum']>15]
data1 = data0[data0['comnum']<1000]

# print(data1.loc[:,"comnum"])

##################################

#画散点图（横轴：价格，纵轴：评论数）
#设置图框大小
fig = plt.figure(figsize=(10,6))
plt.plot(data1['price'],data1['comnum'],"o")
#展示x，y轴标签
plt.xlabel('price')
plt.ylabel('comnum')
plt.show()

##################################

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
ax1.set_ylim(0,300)
ax2.set_ylim(15,1000)
plt.show()

##################################

#删除价格￥150以上，评论数700以上的数据
data2=data1[data['price']<150]
data3=data2[data2['comnum']<700]

##################################

#data3为异常值处理后的数据
fig = plt.figure(figsize=(10,6))
plt.plot(data3['price'],data3['comnum'],"o")
plt.xlabel('price')
plt.ylabel('comnum')
plt.show()

##################################

pricemax=data3['price'].max()
pricemin=data3['price'].min()
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

##################################

# 创建一个二维数组，其中一列存储相同价格出现次数，一列记录相同价格总评论数
static = np.full((150,2),0.0)
data3_price = data3.loc[:,'price'].tolist()
data3_comnum = data3.loc[:,'comnum'].tolist()
data4 = list(zip(data3_price, data3_comnum)) 
    
for j in range(0,150):
    for k in range( len(data4) ):
        if data4[k][0] == j:
            static[j][0] += 1
            static[j][1] += data4[k][1] 
            
# 创建一个数组，存储相同价格评论数平均值        
average_comnum = np.full(150,0.0)

for j in range(0,150):
    if static[j][0] != 0:
        average_comnum[j] = static[j][1] / static[j][0]

# 创建一个二维数组表示价格和评论数的映射关系，其中第一列存放价格，第二列存放平均评论数
data_latest = np.full((391,2),0)
k = 0

for j in data3['price']:
    if average_comnum[int(j)] != 0:
        data_latest[k][0] = int(j)
        data_latest[k][1] = average_comnum[int(j)]
        k += 1

data_latest = data_latest[data_latest[:,0]>0]
price = data_latest[ : , 0 ]
comnum = data_latest[ : , 1 ]

##################################

#A矩阵
m=[]
for i in range(4):
    a = comnum ** (i)
    m.append(a)
A=np.array(m).T
b=price.reshape(price.shape[0],1)

##################################

def projection(A,b):
    AA = A.T.dot(A)#A乘以A转置
    w=np.linalg.inv(AA).dot(A.T).dot(b)

#    拟合函数原型 f(x) = ax^3 + bx^2 + cx^1 + dx^0
    print(w) 
#    d = [4.25266168e+01]
#    c = [1.16898193e-02]
#    b = [8.35253350e-05]
#    a = [7.31648548e-07]
    
    return A.dot(w)

Price = projection(A,b)
Price.shape = (Price.shape[0],)
plt.plot(comnum,price,color='m',linestyle='',marker='o',label=u"已知数据点")
plt.plot(comnum,Price,color='b',linestyle='',marker='.',label=u"拟合曲线")
plt.show()

##################################

# 拟合曲线一阶导数

x0 = np.linspace(0, 250)
d = 6.80428042e+01
c = -3.56967512e-02
b = -4.91380178e-04
a = -9.55391867e-06

# 拟合函数
def y0(x):    
    y0 = a*(x**3) + b*(x**2) + c*x + d
    return y0

# 拟合函数的一阶导数
def y1(x):
    y1 = 3*a*(x**2) + 2*b*x + c
    return y1

# 需求弹性函数
def demand_elasticity(x):
    return abs( y1(x)*y0(x)/x )

# 绘制拟合函数
plt.plot(x0, y0(x0), 'b', linewidth = 1, label = "f(x)")
plt.show()

# 绘制拟合函数一阶导数
plt.ylim((-2.2e0,-1e-3))
plt.plot(x0, y1(x0), 'g', linewidth = 1, label = "f'(x)")
plt.show()

#绘制需求弹性曲线
plt.plot(x0,demand_elasticity(x0), 'r', linewidth = 1, label = "价格弹性曲线")
plt.show()


# 解需求弹性为1的最优解
for x in range(1,255):
    if 1 - 3e-2 <= demand_elasticity(x) <= 1 + 3e-2:
        print("近似解为:")
        print(x)





    
    
        

   


            
    
