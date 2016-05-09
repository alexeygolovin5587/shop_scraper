# written by Tom

import sys
import json
from scrapy.utils.project import get_project_settings

from scrapy.crawler import CrawlerProcess
from shopscraper.spiders.souq_spider import SouqSpider
from shopscraper.spiders.wadi_spider import WadiSpider
from shopscraper.spiders.namshi_spider import NamshiSpider
import os

import argparse


if __name__ == '__main__':

	# define parser to parse arguments from command line input.
	parser = argparse.ArgumentParser(prog='PROG', usage='python start_crawl.py site_name [--all] [--csv]')

	# define argument fields
	parser.add_argument('site_name', nargs='+', help='Set a site name! (e.g. python start_crawler.py souq)')	
	parser.add_argument('--all', help='Don\'t skip a product who was scraped before', dest="all_products", action="store_true")
	parser.add_argument('--csv', help='Create csv file that contains product information scraped by the program', dest="csv", action="store_true")

	# parse arguments
	args = parser.parse_args()

	# parse site name
	if len(args.site_name) == 1:
		site_name = args.site_name[0]
	else:
		parser.print_help()
		exit()

	# parse --all option
	all_products = args.all_products

	# parse --all csv
	csv = args.csv
	
	crawler = CrawlerProcess(get_project_settings())

	if site_name == 'souq':
		crawler.crawl(SouqSpider, all_products=all_products, csv=csv)
	elif site_name == 'wadi':
		crawler.crawl(WadiSpider, all_products=all_products, csv=csv)
	elif site_name == 'namshi':
		crawler.crawl(NamshiSpider, all_products=all_products, csv=csv)
	elif site_name == 'all':
		crawler.crawl(SouqSpider, all_products=all_products, csv=csv)
		crawler.start()
		crawler.crawl(WadiSpider, all_products=all_products, csv=csv)
		crawler.start()
		crawler.crawl(NamshiSpider, all_products=all_products, csv=csv)
	else:
		print "Invalid site name. Please choose one of 'souq', 'wadi' and 'namshi'!"

	crawler.start()


