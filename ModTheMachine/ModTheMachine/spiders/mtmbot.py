# -*- coding: utf-8 -*-
import scrapy


class MtmbotSpider(scrapy.Spider):
    name = 'mtmbot'
    allowed_domains = ['https://modthemachine.typepad.com/']
    start_urls = ['https://modthemachine.typepad.com//my_weblog//2019//03//automate-creation-of-named-geometry.html']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('.entry-header::text').extract()
        codeSamples = response.css('pre::text').extract()
        times = response.css('.date-header::text').extract()
        footers = response.css('.post-footers::text').extract()
        #this gets the xpath text from the 'post footers' section:
        #response.xpath("//div/div[2]/p[1]/span[1]/a[1]/text()").extract()
        #loop to
        #response.xpath("//div/div[2]/p[1]/span[1]/a[#]/text()").extract()
        #comments = response.css('.comments-content::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles,codeSamples,times,footers):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'codeSample' : item[1],
                'created_at' : item[2],
                'footers' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info