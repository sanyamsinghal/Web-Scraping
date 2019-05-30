# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AmazonscrapingItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_rating = scrapy.Field()
    product_imagelink = scrapy.Field()