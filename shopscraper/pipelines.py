# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
class ShopscraperPipeline(object):

	path = "data"
	def open_spider(self, spider):

		# create directory, if it's not existed.
		if not os.path.exists(self.path):
			os.mkdir(self.path)

		self.file = open("%s/%s_%s.csv" % (self.path, spider.name, spider.sp_cate), 'wb')
		
		if spider.sp_cate == 'category': # header for product category
			temp = '"%s","%s"\n' % ("name", "url")
		else: # header for product information
			temp = '"%s","%s","%s"\n' % ("name", "url", "price")

		self.file.write(temp)

	# save results in csv file.
	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):

		if spider.sp_cate == 'category': # write the information of product category
			temp = '"%s","%s"\n' % (item["name"], item["url"])
		else: # write the information of product
			temp = '"%s","%s","%s"\n' % (item["name"], item["url"], item["price"])

		#unicode encoding
		temp = temp.encode('utf8')
		#write line
		self.file.write(temp)

		return item
