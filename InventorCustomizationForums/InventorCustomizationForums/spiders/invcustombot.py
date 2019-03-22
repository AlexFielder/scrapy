# -*- coding: utf-8 -*-
import scrapy

# starts here: http://https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1
# ends here: https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=171

#xpath to solution titles: //*[contains(concat( " ", @class, " " ), concat( " ", "MessageSubject", " " ))]
#xpath to solution post: //*[contains(concat( " ", @class, " " ), concat( " ", "lia-accepted-solution", " " ))]
#xpath to solution code: //pre

class InvcustombotSpider(scrapy.Spider):
    name = 'invcustombot'
    # allowed_domains = ['https://forums.autodesk.com/']
    start_urls = ['https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1/']

    def start_requests(self):
        # for i in range(1, 171):
        #     pageUrl = 'https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=' + str(i)
        #     yield scrapy.Request(pageUrl, callback= self.parsePage) #, meta={'source_page_url': pageUrl}) #, method='GET')
        #debug single page works okay:
        pageUrl = 'https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1'
        yield scrapy.Request(pageUrl, callback= self.parsePage) #, method='GET')

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
            'created at' : response.css("div[itemprop='acceptedAnswer'] div[class='lia-quilt-column-alley lia-quilt-column-alley-single'] .DateTime span::attr(title)").extract(),
            'solution Title' : response.css("div[itemprop='acceptedAnswer'] div[class='lia-message-subject'] *::text").re_first(r"(?:\n\s+)(.*)(?:\n\s+)"),
            'solution' : response.css("[itemprop='acceptedAnswer'] pre *::text").extract(),
            'author' : response.css("[itemprop='acceptedAnswer'] .UserName span *::text").extract_first(),
            'solutions source page url' : response.meta.get('source_page_url')
            #'tags' : solutionDiv.xpath(''), #
        }
