# -*- coding: utf-8 -*-
import scrapy

# starts here: http://https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1
# ends here: https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=171

#xpath to solution titles: //*[contains(concat( " ", @class, " " ), concat( " ", "MessageSubject", " " ))]
#xpath to solution post: //*[contains(concat( " ", @class, " " ), concat( " ", "lia-accepted-solution", " " ))]
#xpath to solution code: //pre

class InvcustombotSpider(scrapy.Spider):
    name = 'invcustombot'
    allowed_domains = ['https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1']
    start_urls = ['https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=1/']

    def start_requests(self):
        for i in range(1, 171):
            pageUrl = 'https://forums.autodesk.com/t5/inventor-customization/bd-p/120?solved-posts-page=' + str(i)
            # print(pageUrl)
            yield scrapy.Request(pageUrl, callback= self.parsePage, method='GET')

    def parsePage(self, response):
        #icon links structured like this:
            #//*[@id="messageList_solved-posts"]/div/table/tbody/tr[1]/td[2]/div/div[1]/div/div/a
            #//*[@id="messageList_solved-posts"]/div/table/tbody/tr[2]/td[2]/div/div[1]/div/div/a
            #//*[@id="messageList_solved-posts"]/div/table/tbody/tr[3]/td[2]/div/div[1]/div/div/a
            #//*[@id="messageList_solved-posts"]/div/table/tbody/tr[30]/td[2]/div/div[1]/div/div/a
            for j in range(1, 30):
                solutionUrl = response.xpath('//*[@id="messageList_solved-posts"]/div/table/tbody/tr[' + str(j) + ']/td[2]/div/div[1]/div/div/a')
                print(solutionUrl)
                yield scrapy.Request(solutionUrl, callback = self.parseSolutionUrl)
            #         response.css('').get()
            # yield scrapy.Request(url=url, dont_filter=True, callback=self.parse)

    def parseSolutionUrl(self, response):
        #need to figure out how to get the div that this is part of: itemprop="acceptedAnswer"
        # solutionDiv = response.xpath('//div[@itemprop = "acceptedAnswer"]').extract_first()
        solutionDiv = response.css('div[itemprop=acceptedAnswer]').extract_first()
        
        print(solutionDiv)
        yield {
            'created at' : solutionDiv.div('DateTime'), # 
            'solution Title' : solutionDiv.xpath(''), #class="lia-message-subject"
            'solution' : solutionDiv.xpath(''), #response.css('pre::text').extract(),
            'author' : solutionDiv.xpath(''), #class="lia-link-navigation lia-page-link lia-user-name-link"
            'tags' : solutionDiv.xpath(''), #
        }
