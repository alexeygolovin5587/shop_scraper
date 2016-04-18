import scrapy
from shopscraper.items import ShopscraperItem, CategoryItem
import math

# class for scraping data from souq.com
class SouqSpider(scrapy.Spider):

	# spider name
	name = "souq"

	allowed_domains = ["uae.souq.com"]
	basic_url = "http://uae.souq.com/ae-en"
	#start_urls = ["http://uae.souq.com/ae-en/mobile-phone/apple/new/a-7-c/l/?sortby=sr"]

	# category of spider
	sp_cate = "category"

	page = 1
	page_size = 0

	product_urls = []

	def start_requests(self):
		return [scrapy.Request("http://uae.souq.com/ae-en", callback=self.get_category, dont_filter=True)]

	# parse category list of product
	def get_category(self, response):
		# get top level category list
		categories = response.xpath("//li[contains(@class, 'level0')]/a/text()")
		sub_categories = response.xpath("//div[contains(@class,'level1')]")

		# crawl leaf category list and their urls
		for index in range(1, len(categories)-1):
			top_cate_name = categories[index].extract().strip()
			
			temp = sub_categories.xpath(".//h4")
			for sub_cate in temp:
				sub_cate_name = self.check_value(sub_cate.xpath("./text()"))
				print top_cate_name + "/" + sub_cate_name

				next_nodes = sub_cate.xpath("./following-sibling::ul[1]/li")[:-1]

				for leaf_cate in next_nodes:
						cate_item = CategoryItem()
						cate_item['name'] = top_cate_name + "/" + sub_cate_name + "/" + self.check_value(leaf_cate.xpath("./a/text()"))
						cate_item['url'] = self.check_value(leaf_cate.xpath("./a/@href"))
					
						yield cate_item

		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
	
	def get_product_url(self, response):
		if self.page == 1:
			total_product = self.check_value(response.xpath("//div[@class='listing-page-text']/text()"))
			total_product = int(total_product.encode('utf8').split('\xc2\xa0')[0])

			self.page_size = int(math.ceil(total_product / 15.0))
		
		if self.page <= self.page_size:
			products = response.xpath("//div[@class='placard']")
			for product in products:
				product_url = product.xpath(".//a[1]/@href")[0].extract().strip()
				if not product_url is None:
					self.product_urls.append(product_url)

			self.page += 1
			url = "http://uae.souq.com/ae-en/mobile-phone/apple/new/a-7-c/l/?sortby=sr&page=%d" % self.page
			request = scrapy.Request(url, callback=self.parse, dont_filter=True)
			yield request

		else:
			for url in self.product_urls:
				request = scrapy.Request(url, callback=self.parse_product_info, dont_filter=True)
				yield request
		

	# parse product info in a page which has 48 products.
	def parse_product_info(self, response):
		item = ShopscraperItem()

		item['name'] = self.check_value(response.xpath("//h1[@itemprop='name']/text()"))
		
		if item['name'] is None:
				item['name'] = self.check_value(response.xpath("//h6[@itemprop='name']/text()"))

		item['price'] = self.check_value(response.xpath("//h3[@class='price']/text()"))
		item['url'] = response.url

		yield item

	def check_value(self, value):
		if len(value) > 0:
			return value[0].extract().strip()
		else:
			return None
		

		
