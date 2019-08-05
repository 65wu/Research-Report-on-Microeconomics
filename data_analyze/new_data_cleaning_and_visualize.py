import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


result_list = []

# 读取.csv文件数据
data = pd.read_csv("F:\\craw\\bookpjt\\csvFile.csv", encoding='ANSI')
# 选定评论数的列值大于100其小于10000的行,选定价格小于300的行
first_data = data.loc[(100 < data["comnum"]) & (data["comnum"] < 10000) & (data["price"] < 300)]

fig = plt.figure(figsize=(10, 6))

# 初始化两个子图，分布为一行两列
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 绘制箱型图
ax1.boxplot(first_data['price'].values)
ax1.set_xlabel('price')
ax2.boxplot(first_data['comnum'].values)
ax2.set_xlabel('comnum')

# 设置x，y轴取值范围
ax1.set_ylim(0, 200)
ax2.set_ylim(0, 10000)
plt.show()

# # 删除价格￥150以上，评论数700以上的数据
second_data = first_data.loc[(first_data["price"] < 100) & first_data["comnum"] < 3000]
price = list(second_data["price"])
old_comments = list(second_data["comnum"])
# 创建一个数组，存储相同价格数评论数的平均值
comments_and_price = dict(zip(price, old_comments))
comments_and_price = sorted(comments_and_price.items(), key=lambda d: d[0])

# 创建一个二维数组表示价格和评论数的映射关系，其中第一列存放评论数，第二列存放平均价格

# 这里是很关键的一步，当当网不公布月销量，这里我假设需求量与评论数呈现一个简单的线性正相关关系
price = np.array(list(p[0] for p in comments_and_price))
old_comments = np.array(list(c[1] for c in comments_and_price))
##################################


def regression(x, y, power):
    # A矩阵
    m = []
    for i in range(power):
        a = x ** i
        m.append(a)
    A = np.array(m).T
    b = y.reshape(y.shape[0], 1)

    ##################################
    def projection(A, b):
        AA = A.T.dot(A)  # A乘以A转置
        w = np.linalg.inv(AA).dot(A.T).dot(b)  # (A^T 乘以 A)^(-1)乘以A^T乘以b
        return w

    new_comments = A.dot(projection(A, b))
    new_comments.shape = (new_comments.shape[0],)
    plt.plot(old_comments, price, color='m', linestyle='', marker='o', label=u"已知数据点")
    plt.plot(new_comments, price, color='b', linestyle='', marker='.', label=u"拟合曲线")
    plt.show()

    w0 = w1 = w2 = w3 = w4 = 0
    w = projection(A, b)
    # 拟合曲线一阶导数
    if power == 5:
        w0 = w[4]
        w1 = w[3]
        w2 = w[2]
        w3 = w[1]
        w4 = w[0]
    if power == 4:
        w0 = w[3]
        w1 = w[2]
        w2 = w[1]
        w3 = w[0]

    if power == 3:
        w0 = w[2]
        w1 = w[1]
        w2 = w[0]

    if power == 2:
        w0 = w[1]
        w1 = w[0]

    return w0, w1, w2, w3, w4


test_power = 4
# 拟合函数
a, b, c, d, e = regression(price, old_comments, test_power)


def get_y0(x, power):
    y0 = 1
    if power == 5:
        y0 = a * (x ** 4) + b * (x ** 3) + c * (x ** 2) + d * x + e
    if power == 4:
        y0 = a * (x ** 3) + b * (x ** 2) + c * x + d
    if power == 3:
        y0 = a * (x ** 2) + b * x + c
    if power == 2:
        y0 = a * x + b
    if power == 1:
        y0 = a
    return y0


# 拟合函数的一阶导数
def get_y1(x, power):
    y1 = 1
    if power == 5:
        y1 = 4 * a * (x ** 3) + b * (x ** 2) + c * x + d
    if power == 4:
        y1 = 3 * a * (x ** 2) + 2 * b * x + c
    if power == 3:
        y1 = 2 * a * x + b
    if power == 2:
        y1 = a
    if power == 1:
        y1 = 0
    return y1


# 需求弹性函数
def demand_elasticity(x, power):
    return -(get_y1(x, power) * x / get_y0(x, power))
# 解需求弹性为1的最优解


x0 = np.linspace(0, 175)
# 绘制拟合函数
plt.plot(get_y0(x0, test_power), x0, 'b', linewidth=1, label="f(x)")
plt.show()

# 绘制拟合函数一阶导数
plt.plot(get_y1(x0, test_power), x0, 'g', linewidth=1, label="f'(x)")
plt.show()

# 绘制需求弹性曲线
plt.plot(x0, demand_elasticity(x0, test_power), 'r', linewidth=1, label="价格弹性曲线")
plt.show()

for price in range(1, 175):
    if 1 - 5e-2 <= demand_elasticity(price, test_power) <= 1 + 5e-2:
        print("近似解为:")
        print(price)










