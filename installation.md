pip3 install scrapy
scrapy version
# Create project
scrapy startproject quotes_spider
# Basic template
## template quotes.py  to url quotes.toscrape.com
scrapy genspider quotes quotes.toscrape.com 
# Basic template
## template example.py to url example.com
scrapy genspider example example.com 
# List available spiders 
scrapy list
# Activate shell
scrapy shell
fetch("http://quotes.toscrape.com/")
response
response.css('h1')
response.css('h1::text')
response.xpath('//h1')
response.xpath('//h1/a')
response.xpath('//h1/a/text()')
response.xpath('//h1/a/text()').extract()
response.xpath('//h1/a/text()').extract_first()
response.xpath('//*[@class="tag-item"]')
len(response.xpath('//*[@class="tag-item"]'))
response.xpath('//*[@class="tag-item"]/a/text()').extract_first()
# To run spider
scrapy crawl quotes

from scrapy.selector import Selector
%paste
sel = Selector(text=html_doc)
sel.extract()
sel.xpath('/html/head/title')
# Select all titles
sel.xpath('//title').extract()
sel.xpath('//text()').extract()
sel.xpath('/html/body/p/text()').extract()
sel.xpath('//p/text()').extract()
sel.xpath('//h2/a/@href').extract()