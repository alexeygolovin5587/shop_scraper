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

			self.file = open("%s/data.csv" % (self.path), 'a')

	def close_spider(self, spider):
		if spider.csv == True:
			self.file.close()
		
		# Delete all data that has delete_flag attribute with 'True'
		self.db.product.delete_many({'delete_flag': 1})

	def process_item(self, item, spider):
		# if need to save scraped data with csv format.

		category = self.db.category.find_one({"_id":item["category_id"]})

		if spider.csv == True:				
			temp = '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"' % (category['ancestors'][0], category['parent'], category['name'], self.strNoCamma(item["product_name"]), item["brand_name"], self.strNoCamma(item["product_url"]), self.strNoCamma(item["sku_product_id"]), self.strNoCamma(item["domain"]), item["price"], item["discounted_price"], item['currency'], item["in_stock"], self.strNoCamma(item["img_url"]), item["category_id"])

			for tmp in item["additional_attributes"]:
				temp += ',"%s","%s"' % (tmp["name"], tmp["value"])
			temp += "\n"

			print temp
			#unicode encoding
			temp = temp.encode('utf8')
			#write line
			self.file.write(temp)
		
		# insert product data into product table in database
		self.db.product.insert_one(item)

		return item

	def strNoCamma(self, str_val):
		return str_val.replace(",", " ")
