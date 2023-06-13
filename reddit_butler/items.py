# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    #All data being scraped from each reddit post. Spider will collect from each post off front page of old.reddit.com
    title = scrapy.Field()
    user = scrapy.Field()
    upvotes = scrapy.Field()
    comments = scrapy.Field()
    subreddit = scrapy.Field()
    content_link = scrapy.Field()
    awards = scrapy.Field()
    time = scrapy.Field()
