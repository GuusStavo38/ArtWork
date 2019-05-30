# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CatawikiItem(scrapy.Item):
    # define the fields for your item here like:
    lot_title = scrapy.Field()
    lot_id = scrapy.Field()
    artist = scrapy.Field()
    artwork_title = scrapy.Field()
    year = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    current_bid = scrapy.Field()
    favorites = scrapy.Field()


class Painting(CatawikiItem):
    technique = scrapy.Field()
    signature = scrapy.Field()
    edition = scrapy.Field()
    period = scrapy.Field()
    image_size = scrapy.Field()
    total_dimensions = scrapy.Field()
    sold_with_frame = scrapy.Field()
    notes = scrapy.Field()
