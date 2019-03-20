# -*- coding: utf-8 -*-
import scrapy


class MtmbotSpider(scrapy.Spider):
    name = 'mtmbot'

    def start_requests(self):
        urls = [
            'https://modthemachine.typepad.com/my_weblog/2015/09/add-control-to-toolbar-panel.html',
            'https://modthemachine.typepad.com/my_weblog/2015/09/extrude-profile-with-hole.html',
            'https://modthemachine.typepad.com/my_weblog/2015/09/fusion-360-hackathon-qa-1-2.html',
            'https://modthemachine.typepad.com/my_weblog/2015/10/fusion-360-hackathon-qa-7-8-9-10.html',
            'https://modthemachine.typepad.com/my_weblog/2015/10/use-entitlement-api-from-fusion.html',
            'https://modthemachine.typepad.com/my_weblog/2015/11/fusion-add-in-path.html',
            'https://modthemachine.typepad.com/my_weblog/2016/01/run-fusion-commands.html',
            'https://modthemachine.typepad.com/my_weblog/2016/01/selection-object-properties-become-invalid.html',
            'https://modthemachine.typepad.com/my_weblog/2016/02/fusion-add-in-with-mfc.html',
            'https://modthemachine.typepad.com/my_weblog/2016/04/fusion-meetups-and-melting-butter.html',
            'https://modthemachine.typepad.com/my_weblog/2016/05/appearance-properties.html',
            'https://modthemachine.typepad.com/my_weblog/2016/05/is-point-on-face.html',
            'https://modthemachine.typepad.com/my_weblog/2016/08/drive-robot-arm-in-fusion-update.html',
            'https://modthemachine.typepad.com/my_weblog/2016/08/drive-robot-arm-in-fusion.html',
            'https://modthemachine.typepad.com/my_weblog/2016/12/parameter-io-issues.html',
            'https://modthemachine.typepad.com/my_weblog/2017/01/store-and-restore-occurrence-position.html',
            'https://modthemachine.typepad.com/my_weblog/2017/02/connect-to-fusion-lifecycle-from-fusion-360-add-in.html',
            'https://modthemachine.typepad.com/my_weblog/2017/04/units-and-parameters-in-inventor.html',
            'https://modthemachine.typepad.com/my_weblog/2017/06/getting-the-overall-size-of-parts.html',
            'https://modthemachine.typepad.com/my_weblog/2017/06/use-chromiumwebbrowser-from-inventor.html',
            'https://modthemachine.typepad.com/my_weblog/2018/10/troubleshooting-debugging.html',
            'https://modthemachine.typepad.com/my_weblog/2018/12/prepare-add-in-for-ui-preview.html',
            'https://modthemachine.typepad.com/my_weblog/2019/03/accessing-iproperties.html',
            'https://modthemachine.typepad.com/my_weblog/2019/03/automate-creation-of-named-geometry.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # allowed_domains = ['https://modthemachine.typepad.com/']
    # start_urls = ['https://modthemachine.typepad.com//my_weblog//2019//03//automate-creation-of-named-geometry.html']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('.entry-header::text').extract()
        codeSamples = response.css('pre::text').extract()
        times = response.css('.date-header::text').extract()
        # footers = response.css('.post-footers *::text').getall() #response.css('.post-footers::text').extract()
        #this gets the xpath text from the 'post footers' section:
        #response.xpath("//div/div[2]/p[1]/span[1]/a[1]/text()").extract()
        #loop to
        #response.xpath("//div/div[2]/p[1]/span[1]/a[#]/text()").extract()
        #this gets the text from the footers:
        #response.css('.post-footers *::text').getall()
        #comments = response.css('.comments-content::text').extract()
        for i in range(1, 20):
            if response.xpath("//div/div[2]/p[1]/span[1]/a[" & i & "]/text()").extract() != "":
                footers += response.xpath("//div/div[2]/p[1]/span[1]/a[" & i & "]/text()").extract()
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