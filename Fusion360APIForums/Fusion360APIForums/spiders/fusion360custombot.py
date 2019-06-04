# -*- coding: utf-8 -*-
import scrapy


class Fusion360custombotSpider(scrapy.Spider):
    name = 'fusion360custombot'
    # allowed_domains = ['https://forums.autodesk.com/']
    start_urls = ['https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22?solved-posts-page=1/']

    def start_requests(self):
        url = 'https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22?solved-posts-page=1'
        # item = "0"
        # item = BaseUrl()
        # item.totalPages = 0
        # request = scrapy.Request(url=url, callback=self.getTotals, meta={'item': item})
        # request.meta['item'] = item
        # yield request
        # newItem = BaseUrl()
        # newItem = request.meta['item']
        # print("pagesTotal :" + str(newItem.totalPages)) #str(item))
        for i in range(1, 24):
            pageUrl = 'https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22?solved-posts-page=' + str(i)
            yield scrapy.Request(pageUrl, callback= self.parsePage) #, meta={'source_page_url': pageUrl}) #, method='GET')
        #debug single page works okay:
        # pageUrl = 'https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22?solved-posts-page=1'
        # yield scrapy.Request(pageUrl, callback= self.parsePage) #, method='GET')

    def getTotals(self, response):
        print("total pages: " + response.css('.lia-paging-page-last a::text').extract_first())
        item = response.meta['item']
        item.totalPages = int(response.css('.lia-paging-page-last a::text').extract_first())
        # print("pagesTotal :" + item['pagesTotal'])
        yield item

    def parsePage(self, response):
        for solvedSolutionUrl in response.xpath("//div[@class='MessageSubjectIcons ']/a/@href").extract():
            yield scrapy.Request(solvedSolutionUrl, dont_filter=True, callback = self.parseSolutionUrl, meta={'source_page_url': response.url})

    def parseSolutionUrl(self, response):
        #need to figure out how to get the div that this is part of: itemprop="acceptedAnswer"
        # solutionDiv = response.xpath('//div[@itemprop = "acceptedAnswer"]').extract_first()
        # solutionDiv = response.css('div[itemprop=acceptedAnswer]').extract_first()
        
        # print(solutionDiv)
        yield {
            'url' : response.url,
            'thread title' : response.css(".PageTitle *::text").extract_first(),
            'thread created at' : response.css(".autodesk-reply-time span::attr(title)").extract_first(),
            'thread created by' : response.css(".UserName span::text").extract_first(),
            'solution created at' : response.css("div[itemprop='acceptedAnswer'] div[class='lia-quilt-column-alley lia-quilt-column-alley-single'] .DateTime span::attr(title)").re(r"(?:\u200e)(.*)"), #response.css("div[itemprop='acceptedAnswer'] div[class='lia-quilt-column-alley lia-quilt-column-alley-single'] .DateTime span::attr(title)").extract(),
            'solution Title' : response.css("div[itemprop='acceptedAnswer'] div[class='lia-message-subject'] *::text").re_first(r"(?:\n\s+)(.*)(?:\n\s+)"),
            'solution' : response.css("[itemprop='acceptedAnswer'] pre *::text").extract(),
            'author' : response.css("[itemprop='acceptedAnswer'] .UserName span *::text").extract_first(),
            'solutions source page url' : response.meta.get('source_page_url')
            #'tags' : solutionDiv.xpath(''), #
        }

class BaseUrl:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
    totalPages = 0
    