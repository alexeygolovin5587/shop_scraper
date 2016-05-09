# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from database.database_manager import *

import json

class ShopscraperPipeline(object):

	# the path for csv files
	path = "data"

	def open_spider(self, spider):
		# get database connection
		self.db = getConnection()

		# if need to save scraped data with csv format.
		if spider.csv == True:
			# create directory, if it's not existed.
			if not os.path.exists(self.path):
				os.mkdir(self.path)

			self.file = open("%s/%s.csv" % (self.path, spider.name), 'wb')
		
			temp = '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"\n' % ("Product Name", "Brand Name", "Product Url", "SKU/Product ID", "Price", "Discounted Price", "In Stock", "Image Url", "Category ID", "Additional Attributes")

			self.file.write(temp)

	def close_spider(self, spider):
		if spider.csv == True:
			self.file.close()
		
		# Delete all data that has delete_flag attribute with 'True'
		self.db.product.delete_many({'delete_flag': 1})

	def process_item(self, item, spider):
		# if need to save scraped data with csv format.
		if spider.csv == True:				
			temp = '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"\n' % (item["product_name"], item["brand_name"], item["product_url"], item["sku_product_id"], item["price"], item["discounted_price"], item["in_stock"], item["img_url"], item["category_id"], json.dumps(item["additional_attributes"]))

			print temp
			#unicode encoding
			temp = temp.encode('utf8')
			#write line
			self.file.write(temp)
		
		# insert product data into product table in database
		self.db.product.insert_one(item)

		return item
