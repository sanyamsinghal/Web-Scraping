# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonscrapingItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_scrapper'
    page_number = 2
    start_urls = ['https://www.amazon.in/s?k=mobiles&i=electronics&bbn=1389401031&rh=n%3A976419031%2Cn%3A1389401031%2Cp_89%3AHonor%7CLenovo%7CMi%7COnePlus%7CSamsung&s=review-rank&dc&fst=as%3Aoff&qid=1558988917&rnid=3837712031&ref=sr_pg_2']

    def parse(self, response):
        #all_div_tags = response.xpath('//div[@class="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]')
        items = AmazonscrapingItem()

        for div_tag in response.xpath('//div[@class="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]'):
            product_name = div_tag.css('span.a-size-medium::text').extract()
            product_price = div_tag.css('.a-spacing-top-small .a-price:nth-child(1) .a-price-whole').css('::text').extract()
            product_rating = div_tag.css('span.a-icon-alt::text').extract()
            product_imagelink = div_tag.css('.a-spacing-none .s-image::attr(src)').extract()


            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_rating'] = product_rating
            items['product_imagelink'] = product_imagelink

            yield items

            next_page = "https://www.amazon.in/s?k=mobiles&i=electronics&bbn=1389401031&rh=n%3A976419031%2Cn%3A1389401031%2Cp_89%3AHonor%7CLenovo%7CMi%7COnePlus%7CSamsung&s=review-rank&dc&page=" + str(AmazonSpider.page_number) + "&fst=as%3Aoff&qid=1558988917&rnid=3837712031&ref=sr_pg_2"

            if AmazonSpider.page_number <= 39:
                 AmazonSpider.page_number += 1
                 yield response.follow(next_page, callback=self.parse)
