# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import Spider
from scrapy.selector import Selector


from ccfg_loop_scrape.items import CcfgLoopScrapeItem

class CcfgSpider(scrapy.Spider):
    name = "ccfg"
    allowed_domains = ["chocolatecoveredfocusgroups.com"]
    start_urls = (
        'http://www.chocolatecoveredfocusgroups.com/',
    )


    def parse(self, response):
        for href in response.xpath("/html/body/div/div/a"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div class=content/'):
            item = CcfgLoopScrapeItem()
            item['h4_header'] = sel.xpath('/html/body/div/div[@class='content']/h4/text()').extract()
            item['paragraph_text'] = sel.xpath('/html/body/div/div[@class='content']/p/text()').extract()
            item['url'] = sel.xpath('a/@href').extract()

            yield item