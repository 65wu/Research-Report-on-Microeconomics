# -*- coding: utf-8 -*-
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AutopjtPipeline(object):
    def __init__(self):
#此时存储到的文件是getdata.json,注意这里将路径修改为你自己要保存文件的路径
        self.file = codecs.open("F:/craw/bookpjt/getdata.json", "wb", encoding="utf-8")
    def process_item(self, item, spider):
#每一页中包含多个商品信息，所以可以通过循环，每一次处理一个商品
#其中len(item["name"])为当前页中商品的总数，依次遍历
        for j in range(0,len(item["name"])):
#将当前页的第j个商品的名称赋值给变量name
            name=item["name"][j]
            price=item["price"][j]
            comnum=item["comnum"][j]
            link=item["link"][j]
#将当前页下第j个商品的name、price、comnum、link等信息处理一下
#重新组合成一个字典
            books={"name":name,"price":price,"comnum":comnum,"link":link}
            #将组合后的当前页中第j个商品的数据写入json文件
            i=json.dumps(dict(books), ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)
#返回item
        return item
    def close_spider(self,spider):
        self.file.close()