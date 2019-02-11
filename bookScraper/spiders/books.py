# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        urls = response.xpath('//h3/a/@href').extract()
        for url in urls:
            absolute_url = response.urljoin(url)
            yield Request(absolute_url, callback=self.parse_url)

        next_page = response.xpath(
            '//*[@class="next"]/a/@href').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse)

    def parse_url(self, response):
        title = response.xpath(
            '//*[@class="col-sm-6 product_main"]/h1/text()').extract_first()
        
        price = response.xpath(
            '//*[@class="price_color"]/text()').extract_first()

        stock = response.xpath(
            '//*[@class="instock availability"]/text()[2]').extract_first()
        stock = re.sub("\D", "", stock)

        UPC = response.xpath(
            '//*[@class="table table-striped"]/tr/th/following-sibling::td/text()')[0].extract()

        yield {
            'Title': title,
            'Price': price,
            'Units Available': stock, 
        }
