import scrapy
from reddit_butler.items import PostItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from scrapy.http.request import Request

import datetime
import re

class butler(scrapy.Spider):
    name = "post"
    start_urls = ['https://old.reddit.com']

    def parse(self, response):
        
        def format_comment(x):
            res = int(re.sub("[^0-9]", "", x))
            return res
        
        next_selector = response.xpath('//span[@class="next-button"]/a/@href')
        for p in response.xpath('//div[@id="siteTable"]/div[contains(@class, "thing")]'): #every reddit post on the front page is consitered a 'thing'
            i = ItemLoader(item=PostItem(), selector=p)
            i.add_xpath('title', ['.//a[@class="title may-blank"]/text()', './/a[@class="title may-blank outbound"]/text()'], MapCompose(str.strip, str.title))
            i.add_xpath('user', './/p[@class="tagline"]')