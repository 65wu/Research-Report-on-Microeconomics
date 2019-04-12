# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#定义好name用来存储商品名
    name=scrapy.Field()
#定义好price用来存储商品价格
    price=scrapy.Field()
#定义好link用来存储商品链接
    link=scrapy.Field()
#定义好comnum用来存储商品评论数
    comnum=scrapy.Field()
