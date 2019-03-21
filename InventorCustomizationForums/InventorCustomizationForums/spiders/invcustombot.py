# -*- coding: utf-8 -*-
import scrapy

# starts here: http://https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1
# ends here: https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=171

class InvcustombotSpider(scrapy.Spider):
    name = 'invcustombot'
    allowed_domains = ['https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1']
    start_urls = ['http://https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1/']

    def parse(self, response):
        pass
