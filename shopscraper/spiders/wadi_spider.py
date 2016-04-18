'''
	Spider class for scraping data from en-ae.wadi.com
'''

import scrapy
from shopscraper.items import ShopscraperItem, CategoryItem
import math

# spider for scraping data from en-ae.wadi.com
class WadiSpider(scrapy.Spider):
	
	# spider name
	name = "wadi"

	allowed_domains = ["en-ae.wadi.com"]
	basic_url = "https://en-ae.wadi.com"

	# category of spider
	sp_cate = "category"

	# list of product urls
	product_urls = []

	def start_requests(self):
		return [scrapy.Request("http://en-ae.wadi.com", callback=self.get_category, dont_filter=True)]

	# parse category list of product
	def get_category(self, response):
		# get top level category list
		categories = response.xpath("//a[@class='navigation']")

		# crawl leaf category list and their urls
		for category in categories:
			top_cate_name = self.check_value(category.xpath("./text()"))

			next_node = category.xpath("./following-sibling::div[1]")

			# parse second level category list
			sub_categories = next_node.xpath(".//li")

			index = 0
			sub_cate_name = ''

			for sub_category in sub_categories:
				if index == 0: # crawl the second level category name
					sub_cate_name = self.check_value(sub_category.xpath("./a/text()"))
				else: # crawl the leaf level category names and urls
					cate_item = CategoryItem()
					cate_item['name'] = top_cate_name + "/" + sub_cate_name + "/" + self.check_value(sub_category.xpath("./a/text()"))
					cate_item['url'] = self.basic_url + self.check_value(sub_category.xpath("./a/@href"))
					
					yield cate_item
				
				index += 1

	# check whether a html element is existed or not.
	def check_value(self, value):
		if len(value) > 0:
			return value[0].extract().strip()
		else:
			return None

