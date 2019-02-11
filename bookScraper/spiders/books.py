# -*- coding: utf-8 -*-
import scrapy
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

    def parse_url(self, response):
        title = response.xpath(
            '//*[@class="col-sm-6 product_main"]/h1/text()').extract_first()

        print(title)