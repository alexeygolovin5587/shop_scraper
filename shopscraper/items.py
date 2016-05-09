# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopscraperItem(scrapy.Item):
		# define the fields for your item here like:
		_id = scrapy.Field()
		product_name = scrapy.Field()
		brand_name = scrapy.Field()	
		product_url = scrapy.Field()
		sku_product_id = scrapy.Field()
		price = scrapy.Field()
		discounted_price = scrapy.Field()
		in_stock = scrapy.Field()
		domain = scrapy.Field()
		disable = scrapy.Field()
		delete_flag = scrapy.Field()
		category_id = scrapy.Field()

		img_url = scrapy.Field()
		additional_attributes = scrapy.Field()
		updated_date = scrapy.Field()
		currency = scrapy.Field()
		
class CategoryItem(scrapy.Item):
		# define the fields for your item here like:
		name = scrapy.Field()
		url = scrapy.Field()
