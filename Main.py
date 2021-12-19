#Install given libraries
#!pip install scrapy
#!pip install crochet

# scrape webpage
import scrapy
from scrapy.crawler import CrawlerRunner
# text cleaning
import re
# Reactor restart
from crochet import setup, wait_for
setup()

import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('result.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

import logging 

class main(scrapy.Spider):
    name='Products'
    allowed_domans=['www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']
    start_urls=['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']
    custom_settings = {
        'LOG_LEVEL': logging.WARNING,
        'ITEM_PIPELINES': {'__main__.JsonWriterPipeline': 1}, # Used for pipeline 1
        'FEED_FORMAT':'json',                                 # Used for pipeline 2
        'FEED_URI': 'result.json'                        # Used for pipeline 2
    }
    
    def parse(self,response):
        for item in response.xpath('//div[@id="Div1"]'):
            yield{
                'Title':item.css('div.product-description a::text').get(),
                'Manufacturer':item.css('div.product-description div.catalog-item-brand-item-number a::text').get(),
                'Price in Dollars':item.css('div.catalog-item-price span.price span::text').get(),
                'Stock Status':item.css('div.catalog-item-price div div span.status span::text').get()
            }
            
@wait_for(10)
def run_main():
    crawler = CrawlerRunner()
    d = crawler.crawl(main)
    return d
  
#Run the program
run_main()
