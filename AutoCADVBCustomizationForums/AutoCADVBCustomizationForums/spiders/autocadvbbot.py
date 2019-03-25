# -*- coding: utf-8 -*-
import scrapy


class AutocadvbbotSpider(scrapy.Spider):
    name = 'autocadvbbot'
    allowed_domains = ['https://forums.autodesk.com/t5/visual-basic-customization/bd-p/33?solved-posts-page=1']
    start_urls = ['http://https://forums.autodesk.com/t5/visual-basic-customization/bd-p/33?solved-posts-page=1/']

    def parse(self, response):
        pass
