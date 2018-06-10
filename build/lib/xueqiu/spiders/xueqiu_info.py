# -*- coding: utf-8 -*-
import json

import scrapy
from xueqiu.items import XueqiuItem

class XueqiuInfoSpider(scrapy.Spider):
    name = 'xueqiu_info'
    allowed_domains = ['xueqiu.com']
    start_urls = []
    hushen_url = 'https://xueqiu.com/stock/cata/stocklist.json?page={}&size=100&order=desc&orderby=percent&type=11%2C12'
    for i in range(1, 57):
        url = hushen_url.format(i)
        start_urls.append(url)
    hongkong_url = 'https://xueqiu.com/stock/cata/stocklist.json?page={}&size=100&order=desc&orderby=percent&type=30'
    for i in range(1, 28):
        url = hongkong_url.format(i)
        start_urls.append(url)
    usa_url = 'https://xueqiu.com/stock/cata/stocklist.json?page={}&size=100&order=desc&orderby=percent&type=0%2C1%2C2%2C3&'
    for i in range(1, 120):
        url = usa_url.format(i)
        start_urls.append(url)


    
    cookies={
    "aliyungf_tc":"AQAAALjDpDdudA4A3lnptzC94xhu + / 6h",
    "xq_a_token":"019174f18bf425d22c8e965e48243d9fcfbd2cc0",
    "xq_a_token.sig":"_pB0kKy3fV9fvtvkOzxduQTrp7E",
    "xq_r_token":"2d465aa5d312fbe8d88b4e7de81e1e915de7989a",
    "xq_r_token.sig":"lOCElS5ycgbih9P - Ny3cohQ - FSA",
    "u":"631528551311911",
    "device_id":"8b9c5376b05a4bba3adcb10471818a29",
    "Hm_lvt_1db88642e346389874251b5a1eded6e3":"1528551314",
    "s":"fz11ww01fz",
    "Hm_lpvt_1db88642e346389874251b5a1eded6e3":"1528553503",
    }
        
    
    def start_requests(self):
        # 发送start_urls的请求，并附带登录状态的Cookies
        for url in self.start_urls:
            yield scrapy.Request(url,cookies=self.cookies, dont_filter=True)

    def parse(self, response):
        node_list = json.loads(response.body.decode())["stocks"]
        print(node_list)
        for node in node_list:
            item = XueqiuItem()
            item["symbol"] = node["symbol"]
            item["code"] = node["code"]
            item["name"] = node["name"]
            item["current"] = node["current"]
            item["percent"] = node["percent"]
            item["change"] = node["change"]
            item["high"] = node["high"]
            item["low"] = node["low"]
            item["high52w"] = node["high52w"]
            item["low52w"] = node["low52w"]
            item["marketcapital"] = node["marketcapital"]
            item["amount"] = node["amount"]
            item["type"] = node["type"]
            item["pettm"] = node["pettm"]
            item["volume"] = node["volume"]
            item["hasexist"] = node["hasexist"]
            yield item