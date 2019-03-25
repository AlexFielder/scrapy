# -*- coding: utf-8 -*-
import scrapy


class AutocaddotnetbotSpider(scrapy.Spider):
    name = 'autocaddotnetbot'
    #allowed_domains = ['https://forums.autodesk.com/t5/net/bd-p/152?solved-posts-page=115']
    start_urls = ['https://forums.autodesk.com/t5/net/bd-p/152?solved-posts-page=115/']

    def start_requests(self):
        for i in range(1, 171):
            pageUrl = 'https://forums.autodesk.com/t5/net/bd-p/152?solved-posts-page=' + str(i)
            yield scrapy.Request(pageUrl, callback= self.parsePage)

    def parsePage(self, response):
        for solvedSolutionUrl in response.xpath("//div[@class='MessageSubjectIcons ']/a/@href").extract():
            yield scrapy.Request(solvedSolutionUrl, dont_filter=True, callback = self.parseSolutionUrl, meta={'source_page_url': response.url})

    def parseSolutionUrl(self, response):
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
