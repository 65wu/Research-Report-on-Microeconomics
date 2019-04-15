import json
import numpy
import csv
# 读取.json文件
dic = []
f = open("F:/craw/bookpjt/getdata.json", 'r', encoding='utf-8')# 这里为.json文件路径
for line in f.readlines():
    dic.append(json.loads(line))
# 对爬取到的数据作处理，将价格和评论数由字符串处理为数字
tmp = ''
name = []
price = []
comnum = []
link = []
for i in range(0, 3059):
    dic[i]['price'] = tmp + dic[i]['price'][1:]
    dic[i]['comnum'] = dic[i]['comnum'][:-3]+tmp
    price.append(float(dic[i]['price']))
    comnum.append(int(dic[i]['comnum']))
    name.append(dic[i]['name'])
    link.append(dic[i]['link'])
data = numpy.array([name, price, comnum, link]).T

# 将data的数据写入csv文件中
csvFile = open('F:/craw/bookpjt/csvFile.csv', 'w')
writer = csv.writer(csvFile)
writer.writerow(['name', 'price', 'comnum', 'link'])
for i in range(0, 3059):
    writer.writerow(data[i])
csvFile.close()