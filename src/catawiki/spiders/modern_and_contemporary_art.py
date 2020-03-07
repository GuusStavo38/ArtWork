# -*- coding: utf-8 -*-
import scrapy
from catawiki.items import CatawikiItem
from scrapy_selenium import SeleniumRequest


class ModernAndContemporaryArtSpider(scrapy.Spider):
    name = 'modern_and_contemporary_art'
    allowed_domains = [
        'auction.catawiki.com',
        'catawiki.com/c/117-modern-contemporary-art',
        'catawiki.com'
    ]
    start_urls = ['http://catawiki.com/c/117-modern-contemporary-art/']

    def parse(self, response):
        # Fetch all the links to the items from the page
        for item_link in response.xpath('//a[contains(@href,"/kavels/")]/@href').getall():
            yield SeleniumRequest(url=item_link, callback=self.parse_item, priority=2)

        javascript = (
            'document.getElementsByClassName("be-pagination")[0]'
            '.getElementsByClassName("next")[0]'
            '.getElementsByClassName("c-link")[0].click();'
        )

        yield SeleniumRequest(url=response.url, callback=self.parse, script=javascript,
                              dont_filter=True, priority=1, wait_time=1)

    @staticmethod
    def parse_item(response):
        # get header part containing the title and reference
        header = response.xpath('//header')
        lot_title = header.xpath('//h1/span/text()').get()
        lot_id = int(header.css('.cw-lot-reference::text').re(r'\d+')[0])

        # get description of the artwork
        description_table = response.css('[id="cw-lot-description"] .cw-spacious').\
            xpath('//tbody/tr')
        description_dict = dict()
        for row in description_table:
            key = row.xpath('th//text()').get()
            value = row.xpath('td//text()').get()
            if value:
                description_dict[key] = value.strip()

        artist = description_dict.get('Artist:', None)
        artwork_title = description_dict.get('Title of artwork:', None)
        year = description_dict.get('Year:', None)

        # get the image url
        image_urls = [response.css('a.cw-image-big-link::attr(href)').get()]

        # get current bid and number of favorites
        bid = response.css('div.cw-bid_info-current_bid strong::text').re(r'\d+')
        if bid:
            current_bid = int(bid[0])
        else:
            current_bid = 0

        favorites_str = response.css('span.cw-favourite-text::attr(data-lot_nr_favorites)').get()
        if favorites_str:
            favorites = int(favorites_str)
        else:
            favorites = 0

        return CatawikiItem(
            lot_title=lot_title,
            lot_id=lot_id,
            artist=artist,
            artwork_title=artwork_title,
            year=year,
            image_urls=image_urls,
            current_bid=current_bid,
            favorites=favorites
        )
