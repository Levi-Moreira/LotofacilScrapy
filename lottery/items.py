# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


class LotteryItem(scrapy.Item):
    lottery_number = scrapy.Field()
    lottery_date = scrapy.Field()
    lottery_result_numbers = scrapy.Field()
    lottery_15_winners = scrapy.Field(input_processor=MapCompose(str.strip), )
    lottery_15_winners_cash = scrapy.Field()
    lottery_14_winners = scrapy.Field(input_processor=MapCompose(str.strip), )
    lottery_14_winners_cash = scrapy.Field()
    lottery_13_winners = scrapy.Field(input_processor=MapCompose(str.strip), )
    lottery_13_winners_cash = scrapy.Field()
    lottery_12_winners = scrapy.Field(input_processor=MapCompose(str.strip), )
    lottery_12_winners_cash = scrapy.Field()
    lottery_11_winners = scrapy.Field(input_processor=MapCompose(str.strip), )
    lottery_11_winners_cash = scrapy.Field()

