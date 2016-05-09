'''
	Spider class for scraping data from en-ae.namshi.com
'''

import scrapy
from shopscraper.items import ShopscraperItem, CategoryItem
import math

# spider for scraping data from en-ae.namshi.com
class NamshiSpider(scrapy.Spider):
	
	# spider name
	name = "namshi"

	allowed_domains = ["en-ae.namshi.com"]
	basic_url = "https://en-ae.namshi.com"

	# category of spider
	sp_cate = "category"

	# list of product urls
	product_urls = []

	def start_requests(self):
		return [scrapy.Request("http://en-ae.namshi.com", callback=self.get_category, dont_filter=True)]

	# parse category list of product
	def get_category(self, response):
		# get top level category list
		categories = response.xpath("//ul[@class='level_01']/li")

		# crawl leaf category list and their urls
		for index in range(1, 4):
			top_cate_name = self.check_value(categories[index].xpath(".//span/text()"))
			
			sub_categories = categories[index].xpath(".//ul[@class='level_02']")

			

			for sub_category in sub_categories:
				leaf_categories = sub_category.xpath("./li")

				print leaf_categories
				sub_cate_name = ''
				i = 0

				for leaf_cate in leaf_categories:
					if i == 0: # crawl the second level category name
						sub_cate_name = self.check_value(leaf_cate.xpath("./a/text()"))
					else: # crawl the leaf level category names and urls
						cate_item = CategoryItem()
						cate_item['name'] = top_cate_name + "/" + sub_cate_name + "/" + self.check_value(leaf_cate.xpath("./a/text()"))
						cate_item['url'] = self.basic_url + self.check_value(leaf_cate.xpath("./a/@href"))
					
						yield cate_item
				
					i += 1

	# check whether a html element is existed or not.
	def check_value(self, value):
		if len(value) > 0:
			return value[0].extract().strip()
		else:
			return None

