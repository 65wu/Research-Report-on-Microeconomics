# 微观经济学市场调研报告
___
## 调研目标：
调查python相关书籍的需求与价格，计算分析点弹性，为商家制度最佳定价策略
___
## 调研工具：
1. python3.7
2. Anaconda
3. Scrapy
4. pandas
5. matplotlib
___
## 调研阶段:
1. 数据采集:
利用scrapy框架爬取当当网4200本python书，收集了相关书籍的商品名、价格、链接、评论数,并将数据存储到json文件中
2. 数据分析：
  + 将json文件转换成csv文件
  + 用pandas进行数据预筛选
  + 生成初步筛选的散点图
  + 生成箱形图，利用箱形图观察离群点的分布
  + 利用箱形图的数据进行再次筛选

3. 数据可视化:
  + 生成再次筛选的散点图
  + 生成评论数与价格的分布条形统计图
___
### 注意事项
1. 建议安装Anaconda环境
使用`pip install scrapy`或`conda install scrapy`安装Scrapy框架
2. 在项目根目录使用语句`scrapy crawl myspd --nolog`运行爬虫程序
3. 生成的json文件请注意保存路径，路径的修改于pipeinclines.py中的以下语句中修改
`self.file = codecs.open("Your_Path/getdata.json", "wb", encoding="utf-8")`
4. 请注意data_cleaning_and_visualize读取的csv文件路径
