import scrapy
from shopscraper.items import ShopscraperItem, CategoryItem
import math

import os
import shutil

import json

from database.database_manager import *

import datetime

# class for scraping data from wadi.com
class WadiSpider(scrapy.Spider):

	# spider name
	name = "wadi"

	allowed_domains = ["en-ae.wadi.com"]
	basic_url = "http://en-ae.wadi.com"

	page = 1
	page_size = 0

	# dirctory for saving images
	image_path = 'images/images_wadi'

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
			self.db.product.delete_many({"domain":"en-ae.wadi.com"})
			
			if os.path.exists(self.image_path):
				# delete all image files
				shutil.rmtree(self.image_path)

		### if you want to skip product what is scraped before
		# *** set 'delete_flag' field of all products in database with 1
		else:
			update_db(self.db.product, {"domain":"uae.wadi.com"}, {"delete_flag":1})

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
			
			
			# fetch category id, additional attributes and wadi urls from category table
			if category["wadi_url"]['enable'] == 0:
				continue;

			category_id = category["_id"]
			additional_attributes = category["additional_attributes"]
			wadi_urls = category["wadi_url"]['url'].split(',,')

			for wadi_url in wadi_urls:
				if wadi_url is u'':
					continue

				request = scrapy.Request(wadi_url, callback=self.get_product_url, dont_filter=True)
				request.meta['category_id'] = category_id
				request.meta['additional_attributes'] = additional_attributes
				request.meta['product_urls'] = []

				# accumulate category list
				category_requests.append(request)

		return category_requests
	
	def get_product_url(self, response):
		
		# *** If it's the first page in category pages, scrape total number of products and calculate the number of pages in this category
		if self.page == 1:
			total_product = self.check_value(response.xpath("//div[@id='catalog_content']//strong[1]/text()"), "total number of product")
			print total_product

			total_product = int(total_product.encode('utf8').split('\xc2\xa0')[0])

			self.page_size = int(math.ceil(total_product / 30.0))
			
		# *** scrape product name and product url from product tiles, save them into a list variable.
		if self.page <= self.page_size:
			
			# get product data from javascript
			data = response.body.split('window.pageData.push(')[1]
			data = data.split('}});')[0] + "}}"

			products = json.loads(data)

			for product in products['data']:
				
				# *** scrape current price and product url from product tiles
				product_url = self.basic_url + "/" + self.check_dict_key(product, 'link', 'wadi')
				price = self.check_dict_key(product, 'price', 'wadi')		# 'price' is original price
				discounted_price = self.check_dict_key(product, 'offerPrice', 'wadi') # 'discounted price' is current price	

				### if you want to scrap all products again.
				if self.all_products == True:
					# *** accumulate product urls that should be scraped 
					if not product_url is '' and checkProduct(self.db, product_url) != True:

						item = self.parse_product_info(product, response.meta['category_id'], response.meta['additional_attributes'], response.url)

						yield item
						# make a request for downloading image
						url = "https://b.wadicdn.com/product/%s/1-product.jpg" % self.check_dict_key(product, 'imageKey', 'wadi')
						request = scrapy.Request(url, callback=self.download_image, dont_filter=True)
						request.meta['category_id'] = response.meta['category_id']
						request.meta['product_name'] = self.check_dict_key(product, 'name', 'name')
						yield request

					elif checkProduct(self.db, product_url) == True:
						print "error: '%s' is duplicated" % (product_url) # log for errors
						#sys.exit("SHUT DOWN EVERYTHING!")
					
				### if you want to skip product what is scraped before			
				else:
					# *** check whether product is in database or not, by using product url
					if checkProduct(self.db, product_url) == True:
					
						# *** check whether current price is same as a price in database
						if checkPrice(self.db, product_url, discounted_price) == False:
							# update product price in database with new price
							update_db(self.db.product, {"product_url":product_url}, {"discounted_price":discounted_price})
						# add logic for original price 
						if checkOriginPrice(self.con, product_url, price) == None:
							# update product price in database with new price
							update_db(self.db, {"product_url":product_url}, {"price":price})					

						# set delete flag with 0
						update_db(self.db.product, {"product_url":product_url}, {"delete_flag":0})

					else:
						# *** accumulate product urls that should be scraped 
						
						if not product_url is '':
							item = self.parse_product_info(product, response.meta['category_id'], response.meta['additional_attributes'], response.url)
							
							yield item
							# make a request for downloading image
							url = "https://b.wadicdn.com/product/%s/1-product.jpg" % self.check_dict_key(product, 'imageKey', 'wadi')
							request = scrapy.Request(url, callback=self.download_image, dont_filter=True)
							request.meta['category_id'] = response.meta['category_id']
							request.meta['product_name'] = self.check_dict_key(product, 'name', 'name')
							yield request
					
				
			# update page number
			self.page += 1
			basic_url = response.url.split('page')[0]

			if 'page' in response.url:
				url = "%spage=%d" % (basic_url, self.page)
			else:
				if '?' in basic_url:
					url = "%s&page=%d" % (basic_url, self.page)
				else:
					url = "%s?page=%d" % (basic_url, self.page)

			# make recursive request to get the whole product urls of this category
			request = scrapy.Request(url, callback=self.get_product_url, dont_filter=True)
			request.meta['product_urls'] = response.meta['product_urls']
			request.meta['category_id'] = response.meta['category_id']
			request.meta['additional_attributes'] = response.meta['additional_attributes']
	
			yield request


	# *** parse product info in product detail page.
	def parse_product_info(self, product, category_id, additional_attributes, category_url):

		item = ShopscraperItem()

		# get product name
		item['product_name'] = self.check_dict_key(product, 'name', 'name')
		
		# get product price
		item['price'] =self.check_dict_key(product, 'price', 'wadi')

		# get product discounted price
		item['discounted_price'] = self.check_dict_key(product, 'offerPrice', 'wadi')
	
		# get product url
		item['product_url'] = self.basic_url + "/" + self.check_dict_key(product, 'link', 'wadi')

		# get category id
		item['category_id'] = category_id

		# get in stock
		item['in_stock'] = True
	
		# get domain
		item['domain'] = 'en-ae.wadi.com'

		# get disable
		item['disable'] = False

		# get delete flag
		item['delete_flag'] = False

		# get product brand
		item['brand_name'] = self.check_dict_key(product['brand'], 'name', 'wadi')

		# get sku or product id 
		item['sku_product_id'] = self.check_dict_key(product, 'sku', 'wadi')

		# get currency
		item['currency'] = "AED"

		# get currency
		item['updated_date'] = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
		
		# get image_url	and create request for downloading product image.	
		#item['img_url'] = "https://b.wadicdn.com/product/%s/1-product.jpg" % self.check_dict_key(product, 'imageKey', 'wadi')
		filename = item['product_name'].replace("/", "")
		
		item['img_url'] = "%s/%s/%s.jpg" % (self.image_path, item['category_id'], filename)

		extra_fields = []
		for extra_field in additional_attributes:
			extra_fields.append({"name":extra_field, "value":self.get_additional_value(extra_field, item, product, category_url)})

		
		item['additional_attributes'] = extra_fields

		# run pipeline for saving all attributes of a product into database 
		
		return item		

	# download image and save it in the given path.
	def download_image(self, response):
		category_id = response.meta['category_id']
		path = self.image_path + "/" + str(category_id)
		# create directory, if image path is not existed.
		if not os.path.exists(path):
			os.mkdir(path)

		filename = response.meta["product_name"].replace("/", "")
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

	def get_additional_value(self, attr_name, product, data, category_url):
		
		category_name = self.db.category.find_one({"_id":product["category_id"]})["name"]

		if attr_name == "Display Size":
			product_name = product['product_name'].split(' ')

			if "inches" in product_name:
				value = float(product_name[product_name.index("inches")-1])
				return value

		elif attr_name == "Headphone Type":
			type_name = ['In ear', 'On ear', 'Over ear']
			
			for elem in type_name:
				if elem in category_name:
					return elem

		elif attr_name == "Connectivity":
			product_name = product["product_name"]
			type_name = ['Wireless', 'Bluetooth']
			
			for elem in type_name:
				if elem in product_name:
					return "Wireless"
			return "Wired"

		elif attr_name == "Megapixel":

			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'Camera' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['Camera'].keys() and 'camera_primary_resolution' in data['attributesMap']['groups']['Camera']['attributes'].keys():				
				return data['attributesMap']['groups']['Camera']['attributes']['camera_primary_resolution']['value']

		elif attr_name == "Screen Size":
			
			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'Camera' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['Camera'].keys() and 'screen_size_text' in data['attributesMap']['groups']['Camera']['attributes'].keys():	
							
				return data['attributesMap']['groups']['Camera']['attributes']['screen_size_text']['value'].split(" ")[0] + " Inch"

			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'Display' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['Display'].keys() and 'screen_size_text' in data['attributesMap']['groups']['Display']['attributes'].keys() and 'value' in data['attributesMap']['groups']['Display']['attributes']['screen_size_text'].keys():
				return data['attributesMap']['groups']['Display']['attributes']['screen_size_text']['value'].split(" ")[0] + " Inch"

		elif attr_name == "Type" or attr_name == "Accessory Type":
			
			if category_name == "Mobile Phones":
				if "smartphones" in category_url:
					return "Smartphone"
				elif "basic_phones" in category_url:
					return "Basic Phone"

			if 'highlights' in data.keys():				
				for elem in data['highlights']:
					temp = elem.split(":")				
					if temp[0].strip() == "Type":
						return temp[1].strip()

		elif category_name == "Mobile Phones" and attr_name == "Operating System":
			if "basic_phones" in category_url:
				return "Native"
			else:
				
				if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'General Features' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['General Features'].keys() and 'operating_system' in data['attributesMap']['groups']['General Features']['attributes'].keys() and 'value' in data['attributesMap']['groups']['General Features']['attributes']['operating_system'].keys():
					os = data['attributesMap']['groups']['General Features']['attributes']['operating_system']['value']
					
					if 'ios' in os.lower():
						return "iOS"
					elif 'blackberry' in os.lower():
						return "Blackberry OS"
					elif 'window' in os.lower():
						return "Windows"
					else:
						return os

		elif attr_name == "Storage Capacity":
			
			if "https://en-ae.wadi.com/electronics-mobiles_tablets-tablets/" in category_url:
				memory = "memory_internal_dropdown"
			else:
				memory = "hard_disk_capacity_text"

			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'Memory and Storage' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['Memory and Storage'].keys() and memory in data['attributesMap']['groups']['Memory and Storage']['attributes'].keys() and 'value' in data['attributesMap']['groups']['Memory and Storage']['attributes'][memory].keys():
				if "https://en-ae.wadi.com/electronics-mobiles_tablets-tablets/" in category_url:
					return str(data['attributesMap']['groups']['Memory and Storage']['attributes'][memory]['value'])
				else:
					return str(data['attributesMap']['groups']['Memory and Storage']['attributes'][memory]['value']) + " GB"

		elif attr_name == "RAM":
			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'Memory and Storage' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['Memory and Storage'].keys() and 'ram_size_text' in data['attributesMap']['groups']['Memory and Storage']['attributes'].keys() and 'value' in data['attributesMap']['groups']['Memory and Storage']['attributes']['ram_size_text'].keys():
				return str(data['attributesMap']['groups']['Memory and Storage']['attributes']['ram_size_text']['value']) + " GB"

		elif attr_name == "Processor Type":
			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'Processor' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['Processor'].keys() and 'processor_type' in data['attributesMap']['groups']['Processor']['attributes'].keys() and 'value' in data['attributesMap']['groups']['Processor']['attributes']['processor_type'].keys():
				return data['attributesMap']['groups']['Processor']['attributes']['processor_type']['value']

		elif attr_name == "Operating System Type" or attr_name == "Operating System":
			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'Platform' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['Platform'].keys() and 'operating_system' in data['attributesMap']['groups']['Platform']['attributes'].keys() and 'value' in data['attributesMap']['groups']['Platform']['attributes']['operating_system'].keys():
				os = data['attributesMap']['groups']['Platform']['attributes']['operating_system']['value'].lower()
				
				if "window" in os or "windows" in os or "win" in os:
					return "Windows"
				elif "mac" in os:
					return "Mac OS"
				elif "chrome" in os:
					return "Chrome"
				elif "Android" in os:
					return "Android"
				else:
					return "Linux"

		elif attr_name == "Color":
			if "attributes" in data.keys() and 'color_family_en' in data['attributes'].keys():
				return data['attributes']['color_family_en']

		elif attr_name == "Platform":
			if 'attributesMap' in data.keys() and 'groups' in data['attributesMap'].keys() and 'General Features' in data['attributesMap']['groups'].keys() and 'attributes' in data['attributesMap']['groups']['General Features'].keys() and 'gaming_platform' in data['attributesMap']['groups']['General Features']['attributes'].keys() and 'value' in data['attributesMap']['groups']['General Features']['attributes']['gaming_platform'].keys():
				return data['attributesMap']['groups']['General Features']['attributes']['gaming_platform']['value']

		elif attr_name == "Mobile Accessory Type":
			return "Covers"

		return ''

			

