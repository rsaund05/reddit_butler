import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from scrapy.http.request import Request

from reddit_butler.items import PostItem

class butler(scrapy.Spider):
    name = "butler"
    default = ['https://old.reddit.com']

    def __init__(self, *args, **kwargs): #Pull in comma seperated list of URLs to scan
        super(butler, self).__init__(*args, **kwargs) 
        self.start_urls = kwargs.get('start_urls').split(',')

    
    def parse(self, response):
        
        def format_comment(x):
            res = int(re.sub("[^0-9]", "", x))
            return res
        
        next_selector = response.xpath('//span[@class="next-button"]/a/@href')
        for p in response.xpath('//div[@id="siteTable"]/div[contains(@class, "thing")]'):
            i = ItemLoader(item=PostItem(), selector=p)
            i.add_xpath('title', ['.//a[@class="title may-blank "]/text()', './/a[@class="title may-blank outbound"]/text()'], MapCompose(str.strip, str.title))
            i.add_xpath('user','.//p[@class="tagline "]/a[1]/text()')
            i.add_xpath('upvotes','.//div[@class="score likes"]/@title', MapCompose(int))
            i.add_xpath('comments','.//a[contains(@data-event-action, "comments")]/text()', MapCompose(lambda x:format_comment(x)))
            i.add_xpath('subreddit', './/p[@class="tagline "]/a[2]/text()')
            i.add_xpath('content_link', './/a[contains(@data-event-action, "title")]/@href')
            i.add_xpath('awards', ['.//a[@class="awarding-link"]/@data-count', './/a[@class="awarding-show-more-link"]/text()'], MapCompose(lambda x: format_comment(x)))
            i.add_xpath('time', './/time/@datetime')
            yield i.load_item()

        for url in next_selector.extract():
            yield Request(url, callback=self.parse)