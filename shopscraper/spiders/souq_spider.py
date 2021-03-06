import scrapy
from shopscraper.items import ShopscraperItem, CategoryItem
import math

import os
import shutil

import json

from database.database_manager import *

import datetime

# class for scraping data from souq.com
class SouqSpider(scrapy.Spider):

	# spider name
	name = "souq"

	allowed_domains = ["uae.souq.com"]
	basic_url = "http://uae.souq.com/ae-en"

	page = 1
	page_size = 0

	# dirctory for saving images
	image_path = 'images/images_souq'

	# attribute name map
	additional_attr_map = {
		'Display Size': 'Screen Size',
		'Megapixel': 'Resolution',
		'Lens Or Flash_Type': 'Interchangeable Lense Type',
		'Power Tools_Type': 'Type',
		'Storage Capacity': 'Hard Disk Capacity',
		'Processor Type': 'Processor'
	}

	# attribute value map
	value_map = {
		'Bluetooth': "Wireless",
		'Remote Control': "Camera Remote",
		'Battery Charger': "Battery & Chargers",
		'Lens Cap Holder': "Lens Accessories",
		'Lens Filter': "Filters",
		'Lighting Studio': "Lighting & Studio",
		'Monopod and Monopods': "Tripod and Monopods"
	}

	def __init__(self, all_products, csv):
		# the value that points out that this is first time to scrape or not
		#    	If the value is true, the program will skip the product that is in database
		#		Otherwise, the program will scrape all data and save them in database.
		
		self.all_products = all_products
		self.csv = csv

		# get database connection
		self.db = getConnection()

		### if you want to scrap all products again.
		if self.all_products == True:
			
			# delete all products from product table in database
			self.db.product.delete_many({"domain":"uae.souq.com"})
			
			if os.path.exists(self.image_path):
				# delete all image files
				shutil.rmtree(self.image_path)

		### if you want to skip product what is scraped before
		# *** set 'delete_flag' field of all products in database with 1
		else:
			update_db(self.db.product, {"domain":"uae.souq.com"}, {"delete_flag":1})

		# create directory, if image path is not existed.
		if not os.path.exists("images"):
			os.mkdir("images")

		if not os.path.exists(self.image_path):
			os.mkdir(self.image_path)

		
	# *** Read category list with urls from database and additional attributes, and create requests.
	def start_requests(self):
		category_requests = []
	
		category_data = getCategory(self.db)

		for category in category_data:

			# fetch category id, additional attributes and souq urls from categorydelete table
			if category["souq_url"]['enable'] == 0:
				continue;

			category_id = category["_id"]
			additional_attributes = category["additional_attributes"]
			souq_urls = category["souq_url"]['url'].split(',,')

			for souq_url in souq_urls:
				if souq_url is u'':
					continue
				
				request = scrapy.Request(souq_url, callback=self.get_product_url, dont_filter=True)
				request.meta['category_id'] = category_id
				request.meta['additional_attributes'] = additional_attributes
				request.meta['product_urls'] = []
				request.meta['page'] = 1

				# accumulate category list
				category_requests.append(request)
	
		return category_requests
	
	def get_product_url(self, response):
		
		# *** If it's the first page in category pages, scrape total number of products and calculate the number of pages in this category	
		page = response.meta['page']

		if page == 1:
			total_product = self.check_value(response.xpath("//div[@class='listing-page-text']/text()"), "total number of product")
			total_product = int(total_product.encode('utf8').split('\xc2\xa0')[0])

			page_size = int(math.ceil(total_product / 15.0))
		else:
			page_size = response.meta['page_size']
		
		# *** scrape product name and product url from product tiles, save them into a list variable.
		if page <= page_size:
			products = response.xpath("//div[@id='content-body']//div[@class='placard']")
			for product in products:

				# *** scrape current price and product url from product tiles
				product_url = self.check_value(product.xpath(".//a[1]/@href"), "product url")

				price = self.check_value(product.xpath(".//span[contains(@class, 'was')]/text()"), "product original price")		# 'price' is original price
				discounted_price = self.check_value(product.xpath(".//span[@class='is block']/text()"), "product discounted price") # 'discounted price' is current price
				
				if price == u'':
					price = discounted_price

				### if you want to scrap all products again.
				if self.all_products == True:
					# *** accumulate product urls that should be scraped 
					if not product_url == u'':
						if product_url not in [item['url'] for item in response.meta['product_urls']]:
							response.meta['product_urls'].append({'url':product_url, 'price':price, 'discounted_price':discounted_price})
					
				### if you want to skip product what is scraped before			
				else:
					# *** check whether product is in database or not, by using product url
					if checkProduct(self.db, product_url) == True:
					
						# *** check whether current price is same as a price in database
						if checkPrice(self.db, product_url, discounted_price) == False:
							# update product price in database with new priceType: Cases & Bags
							update_db(self.db.product, {"product_url":product_url}, {"discounted_price":discounted_price})
						# add logic for original price 
						if checkOriginPrice(self.db, product_url, price) == False:
							# update product price in database with new price
							update_db(self.db.product, {"product_url":product_url}, {"price":price})				

						# set delete flag with 0
						update_db(self.db.product, {"product_url":product_url}, {"delete_flag":0})

					else:
						# *** accumulate product urls that should be scraped 
						if product_url != u'':
							if product_url not in [item['url'] for item in response.meta['product_urls']]:
								response.meta['product_urls'].append({'url':product_url, 'price':price, 'discounted_price':discounted_price})
					
				
			# update page number
			page += 1
			basic_url = response.url.split('page')[0]

			if 'page' in response.url:
				url = "%spage=%d" % (basic_url, page)
			else:
				if '?' in basic_url:
					url = "%s&page=%d" % (basic_url, page)
				else:
					url = "%s?page=%d" % (basic_url, page)

			# make recursive request to get the whole product urls of this category
			request = scrapy.Request(url, callback=self.get_product_url, dont_filter=True)
			request.meta['product_urls'] = response.meta['product_urls']
			request.meta['category_id'] = response.meta['category_id']
			request.meta['additional_attributes'] = response.meta['additional_attributes']
			request.meta['page'] = page
			request.meta['page_size'] = page_size

			yield request

		# *** if there is no more page, go to product detail page.
		else:
			
			for element in response.meta['product_urls']:				
				request = scrapy.Request(element['url'], callback=self.parse_product_info, dont_filter=True)
				request.meta['price'] = element['price']
				request.meta['discounted_price'] = element['discounted_price']
				request.meta['product_urls'] = response.meta['product_urls']
				request.meta['category_id'] = response.meta['category_id']
				request.meta['additional_attributes'] = response.meta['additional_attributes']

				yield request
		

	# *** parse product info in product detail page.
	def parse_product_info(self, response):
		item = ShopscraperItem()

		# get product name
		item['product_name'] = self.check_value(response.xpath("//h1[@itemprop='name']/text()"), "product name")
		
		if item['product_name'] == u'':
			item['product_name'] = self.check_value(response.xpath("//h6[@itemprop='name']/text()"), "product name")

		'''temp_name = item['product_name'].split("-")
		if len(temp_name) > 1:
			item['sku_product_id'] = temp_name[len(temp_name)-1].strip()
			temp_name = '-'.join(temp_name[:-1])
			item['product_name'] = temp_name.strip()'''

		# get product price
		item['price'] = float(response.meta['price'].split(' ')[0].replace(',',''))

		# get product discounted price
		item['discounted_price'] = float(response.meta['discounted_price'].split(' ')[0].replace(',',''))
	
		# get product url
		item['product_url'] = response.url

		# get category id
		item['category_id'] = response.meta['category_id']

		# get in stock
		item['in_stock'] = True
	
		# get domain
		item['domain'] = 'uae.souq.com'

		# get disable
		item['disable'] = False

		# get delete flag
		item['delete_flag'] = False

		# get currency
		item['currency'] = "AED"

		# get currency
		item['updated_date'] = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

		# crawl data from product connections block
		connection_titles = response.xpath("//span[@class='connection-title']")
		
		connections = dict()
		for connection in connection_titles:
			title = self.check_value(connection.xpath("./text()"), "additional attribute name")
			value = self.check_value(connection.xpath("./following-sibling::div[1]/span/text()"), "additional attribute value")
			
			if value.split(' ')[0].isdigit():
				connections[title] = int(value.split(' ')[0])
			else:
				connections[title] = value
		

		# crawl data from specs block
		specs_short = response.xpath("//div[@id='specs-short']")
		specs = dict()
		if len(specs_short) > 0:
			keys = specs_short[0].xpath(".//dt")
			for key in keys:
				key_str = self.check_value(key.xpath("./text()"), "extra field name")
				value_str = self.check_value(key.xpath("./following-sibling::dd[1]/text()"), "extra field value")
				specs[key_str] = value_str

		# crawl data from item details block
		detail_short = response.xpath("//div[@class='item-details-mini']")
		detail = dict()
		if len(detail_short) > 0:
			keys = detail_short[0].xpath(".//dt")
			for key in keys:
				key_str = self.check_value(key.xpath("./text()"), "detail field name")
				value_str = self.check_value(key.xpath("./following-sibling::dd[1]/text()"), "detail field value")
				detail[key_str] = value_str

		# get sku or product id
		temp_id = self.check_dict_key(specs, 'Item EAN', item['product_url'])
		
		item['sku_product_id'] = temp_id

		# get product brand
		item['brand_name'] = self.check_dict_key(specs, 'Brand', item['product_url'])
		
		# get image_url	and create request for downloading product image.	
		temp = self.check_value(response.xpath("//div[@class='vip-item-img-container']//img/@src"), "product image url")
		#item['img_url'] = "%s/%s/%s" % (os.path.dirname(os.path.abspath(__file__)), self.image_path, temp.split("/")[-1])
		item['img_url'] = "%s/%s/%s.jpg" % (self.image_path, item['category_id'], item['product_name'])
		# get additional fields
		extra_fields = dict()
		extra_fields_temp = response.meta['additional_attributes']
		
		for extra_field in extra_fields_temp:
			if extra_field == u"Type":
				srch_name = self.db.category.find_one({"_id":item['category_id']})["name"] + "_Type"
			else:
				srch_name = extra_field
			
			# get additional data from spec block
			if extra_field != u'':
				if srch_name in self.additional_attr_map:
					extra_fields[extra_field] = self.check_dict_key(specs, self.additional_attr_map[srch_name], "spec")
					
				else:
					extra_fields[extra_field] = self.check_dict_key(specs, extra_field, "spec")

			# get additional data from connection block
			if extra_fields[extra_field] == u'':
				if extra_field in self.additional_attr_map:
					extra_fields[extra_field] = self.check_dict_key(connections, self.additional_attr_map[srch_name], "connection")
				else:
					extra_fields[extra_field] = self.check_dict_key(connections, extra_field, "connection")

			# get addictional data from detail block
			if extra_fields[extra_field] == u'':
				if extra_field in self.additional_attr_map:
					extra_fields[extra_field] = self.check_dict_key(detail, self.additional_attr_map[srch_name], "detail")
				else:
					extra_fields[extra_field] = self.check_dict_key(detail, extra_field, "detail")

			# change a value with normal one
			# extra_fields[extra_field] = self.get_additional_value(srch_name, item)

			if extra_fields[extra_field] == u'':
				extra_fields[extra_field] = self.get_additional_value(srch_name, item)

			if extra_fields[extra_field] in self.value_map.keys():
				extra_fields[extra_field] = self.value_map[extra_fields[extra_field]]
			
			extra_fields[extra_field] = self.unit_filter(extra_field, extra_fields[extra_field], self.db.category.find_one({"_id":item['category_id']})["name"], extra_fields)

			if self.db.category.find_one({"_id":item['category_id']})["parent"] == "Laptops and Notebooks" or self.db.category.find_one({"_id":item['category_id']})["name"] == "Tablets":
				if self.db.category.find_one({"_id":item['category_id']})["parent"] == "Laptops and Notebooks":
					temp_extra = self.getComputerInfo(item['product_name'], "Laptops and Notebooks", extra_fields)
				else:
					temp_extra = self.getComputerInfo(item['product_name'], self.db.category.find_one({"_id":item['category_id']})["name"], extra_fields)					

				extra_fields = temp_extra
		
		temp_list = []
		for field in extra_fields.keys():
			temp_list.append({"name":field, "value":extra_fields[field]})

		item['additional_attributes'] = temp_list

		# run pipeline for saving all attributes of a product into database 
		if checkProduct(self.db, item['product_url']) != True:
			yield item

			request = scrapy.Request(temp, callback=self.download_image, dont_filter=True)
			request.meta['category_id'] = item['category_id']
			request.meta['product_name'] = item['product_name']
			yield request

	# download image and save it in the given path.
	def download_image(self, response):
		category_id = response.meta['category_id']
		path = self.image_path + "/" + str(category_id)
		# create directory, if image path is not existed.
		if not os.path.exists(path):
			os.mkdir(path)

		filename = response.meta['product_name'].replace("/", "")
		path = path + "/" + filename + ".jpg"

		with open(path, 'wb') as f:
			f.write(response.body)

	# check whether scraped html node is existed or not 
	def check_value(self, value, label):
		if len(value) > 0:
			return value[0].extract().strip()
		else:
			if label != u'product original price':
				print "error: cannot find html node for %s" % label # log for errors
			return ''

	# check whether the key is in dictionary or not
	def check_dict_key(self, dictionary, key, url):
		if key in dictionary.keys():
			return dictionary[key]
		else:			
			print "error: there is no field named '%s', when scraping data from %s" % (key, url) # log for errors
			return ''

	def get_additional_value(self, attr_name, product):
		if attr_name == "Headphone Type":
			category_name = self.db.category.find_one({"_id":product["category_id"]})["name"]
			type_name = ['In ear', 'On ear', 'Over ear']
			
			for elem in type_name:
				if elem in category_name:
					return elem

		elif attr_name == u"Connectivity":
			product_name = product["product_name"]
			type_name = ['Wireless', 'Bluetooth']
			
			for elem in type_name:
				if elem in product_name:
					return "Wireless"
			return "Wired"

		elif attr_name == u"Megapixel":
			
			product_name = product["product_name"].split(" ")
			type_name = ['MP,', 'Megapixel,']
			
			for elem in type_name:
				if elem in product_name:
					return product_name[product_name.index(elem)-1].split(' ')[0] + " MP"

		return ''

	# change a unit with normal one, if it's necessary
	def unit_filter(self, key, value, category_name, extra_fields):
		if key == u"Megapixel":
			if value[len(value)-2:] == u"MP":
				return value[:-2].strip() + " MP"
			elif value[len(value)-1:] == u"P":
				return "%.2f MP" % (float(value[:-1].strip()) / 1000)

		if key == u"Screen Size":
			return value + " Inch"

		if key == u"Accessory Type":
			if value != "Controllers":
				return "Others"

		if category_name == u"Mobile Phones":
			if key == u"Type":
				if value == u"Mobile Phone":		# Convert Mobile Phone type in souq = Basic Phone
					return "Basic Phone"
				else:
					return "Smartphone"
			if key == u"Operating System":
				if 'Type' in extra_fields:
					if extra_fields['Type'] == u"Basic Phone": # If Type= Basic Phone then OS = Native
						return "Native"
					elif 'ios' in value.lower():
						return 'iOS'

		return value

	# get computer info from product name
	# 	product brand - processor, screen size, storage capacity, ram, vga, os, color
	def getComputerInfo(self, product_name, category_name, extra_fields):
		temp = product_name.split(" - ")
		
		if len(temp) <= 1 or (len(temp) > 1 and len(temp[1]) < 30) and category_name == "Laptops and Notebooks":
			temp =  product_name.split("(")
			if len(temp) <= 1:
				temp = product_name.split(",")
			else:
				temp = temp[1].split(")")[0]
				temp = temp.split(",")
		else:
			temp = temp[1].split(",")

		data = dict()
		if category_name == "Laptops and Notebooks":
			data['Processor Type'] = temp[0].strip()
			tmp_list = temp[1:]
		else:
			tmp_list = temp
			if "Operating System" in extra_fields:
				data['Operating System'] = extra_fields['Operating System']
		

		for elem in tmp_list:

			# parse processor type
			if category_name == "Laptops and Notebooks" and "Core" in elem or 'hz' in elem.lower():
				data['Processor Type'] += " " + elem

			# parse screen size
			if "INCHES" in elem or "Inch" in elem or "\"" in elem or elem.lower().isdigit():
				screen_temp = elem.split("Inch")[0].strip()
				screen_temp = screen_temp.split("\"")[0].strip()
				screen_temp = screen_temp.split("INCHES")[0].strip()
				data['Screen Size'] = screen_temp + " Inch"

				screen_tmp = data['Screen Size'].split(" ")
				data["Screen Size"] = screen_tmp[screen_tmp.index("Inch")-1] + " Inch"
			
			# parse storage size and ram size
			if ('GB' in elem or 'TB' in elem) and 'VGA' not in elem:
				if 'GB' in elem:
					tmp = elem.split("GB")[0].strip()
				else:
					tmp = elem.split("TB")[0].strip()

				if tmp.isdigit():
					num = int(tmp)
					if 'TB' in elem:
						num *= 1024
					if category_name == "Laptops and Notebooks":
						if num >= 16:
							data['Storage Capacity'] = "%d GB" % num
						else:
							data['RAM'] = "%d GB" % num
					else:
						data['Storage Capacity'] = "%d GB" % num

			# parse operating sytem
			if category_name == "Laptops and Notebooks":
				os = elem.strip()
				if "window" in os.lower() or "windows" in os.lower() or "win" in os.lower():
					data['Operating System Type'] = "Windows"
				elif "mac" in os.lower():
					data['Operating System Type'] = "Mac OS"
				elif "chrome" in os.lower():
					data['Operating System Type'] = "Chrome"
				elif "linux" in os.lower() or 'unix' in os.lower() or 'android' in os.lower():
					data['Operating System Type'] = "Linux"
				elif "dos" in os.lower():
					data['Operating System Type'] = "DOS"

			# parse color
			if elem.strip().lower() in ['black', 'silver', 'gold', 'blue', 'gray', 'white', 'space gray']:
				data['Color'] = elem.strip()
				
		return data
		

		
