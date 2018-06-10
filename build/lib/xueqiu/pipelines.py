# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class XueqiuPipeline(object):
    # 爬虫启动时执行一次
    def open_spider(self, spider):
        self.f = open("hushen.json", "w")

    # 必须实现的，用来处理每一个item数据
    def process_item(self, item, spider):

        content = json.dumps(dict(item)) + ",\n"
        self.f.write(content)

        return item

    # 爬虫关闭时执行一次
    def close_spider(self, spider):
        self.f.close()
