# -*- coding: utf-8 -*-
import scrapy
from bookpjt.items import BookpjtItem
from scrapy.http import Request


class MyspdSpider(scrapy.Spider):
    name = "myspd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://search.dangdang.com/?key=python&act=input&show=big&page_index=1#J_tab']

    def parse(self, response):
        item=BookpjtItem()
#通过各Xpath表达式分别提取商品的名称、价格、链接、评论数等信息
        item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
#提取完后返回item
        yield item
#接下来很关键，通过循环自动爬取100页的数据
        for i in range(1,101):
#通过上面总结的网址格式构造要爬取的网址
            url="http://search.dangdang.com/?key=python&act=input&show=big&page_index="+str(i)+"#J_tab"
#通过yield返回Request，并指定要爬取的网址和回调函数
#实现自动爬取
            yield Request(url, callback=self.parse)