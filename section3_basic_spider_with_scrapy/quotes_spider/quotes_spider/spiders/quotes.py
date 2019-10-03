# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader

from section3_basic_spider_with_scrapy.quotes_spider.quotes_spider.items import QuotesSpiderItem 

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item= QuotesSpiderItem(),  response= response)
        # h1_tag = response.xpath('//h1/a/text()').extract_first()
        # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        # yield { 'H1 tag' : h1_tag, 'Tags': tags}
        quotes = response.xpath('//*[@class="quote"]')
        quotes.xpath('.//*[@class="text"]/text()').extract()
        for quote in quotes:
            text = quotes.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            yield{
                'Text': text,
                'Author': author,
                'Tags': tags
            }
        next_page_url = response.xpath('.//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
