# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
# from event.items import EventItem
import datetime
#import logging
import re


class EventSpider(scrapy.Spider):
    name = 'swing'


    def __init__(self, *args, **kwargs):
        self.start_urls = [start_url]

    def parse(self, response):
        selector = Selector(response)
        homepage_list = selector.xpath()
            # '//div[@class="csliderMain"]/div[@class="content_box"]/div[1]/div[@class="infocon"]/div[2]/table[1]/following-sibling::table')
        for homepage in homepage_list:
            yield Request(homepage, callback=self.parse_homepage)

        next_page_url = selector.xpath(
            '//div[@class="csliderMain"]/div[@class="content_box"]/div[1]/div[@class="infocon"]/div[2]/center/div/a[@href="#"][1]/following-sibling::a[1]/@href').extract()[
            0]
        yield Request(next_page_url, callback=self.parse)


    def parse_homepage(self, response):
        selector = Selector(response)
        single_page_list = selector.xpath()
        for single_page in single_page_list:
            yield  Request(single_page, callback=self.parse_singgle_page)


    def parse_singgle_page(self, response):
        selector = Selector(response)
        single_page_list = selector.xpath()