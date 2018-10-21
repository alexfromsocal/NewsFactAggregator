import requests
from bs4 import BeautifulSoup
import sys
import re
import scrapy
import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)



##class spider1(scrapy.Spider):
##    name = 'Wikipedia'
##    start_urls = ['https://en.wikipedia.org/wiki/Battery_(electricity)']
##
##    def parse(self, response):
##        print (response.css('h1#firstHeading::text').extract())

            
class spider1(scrapy.Spider):
    #collect website list
    #query= sys.argv[1]
    query='Trump'
    URL=('https://ui.customsearch.ai/hosted-page?customconfig=99345699-6abf-4331-bfca-f0754abd9352&version=latest&market=en-US&q='+query)
    #URL=("https://doc.scrapy.org/en/latest/intro/tutorial.html")
    #print(URL)
    
    name='News'
    start_urls=[URL]

    def parse(self, response):
        print(response.css('div::text').extract())



        #https://www.nytimes.com/2018/10/17/us/politics/trump-china-shipping.html
        #https://www.politico.com/news/donald-trump
        #http://www.latimes.com/topic/politics-government/donald-trump-PEBSL000163-topic.html
        #https://www.nytimes.com/2018/10/17/us/politics/don-mcgahn-leaves-trump-administration.html
        #https://www.nytimes.com/2018/10/14/us/politics/trump-saudi-arabia-arms-deal.html
 
