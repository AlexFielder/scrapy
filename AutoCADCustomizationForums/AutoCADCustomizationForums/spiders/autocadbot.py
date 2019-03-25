# -*- coding: utf-8 -*-
import scrapy


class AutocadbotSpider(scrapy.Spider):
    name = 'autocadbot'
    #allowed_domains = ['https://forums.autodesk.com/t5/net/bd-p/152?solved-posts-page=115']
    start_urls = ['http://https://forums.autodesk.com/t5/net/bd-p/152?solved-posts-page=115/']

    def parse(self, response):
        pass
