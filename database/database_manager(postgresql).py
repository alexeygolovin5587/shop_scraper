#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

# get database connection
def getConnection():
	
	con = None

	con = psycopg2.connect(database='shop', user='postgres', password='root') 
	return con

# check whether the given catgory is in database or not
def checkCategory(cur, catgory):
	cur.execute("SELECT * from category where category1='%s' and category2='%s' and category3='%s'" % \
					(catgory[0], catgory[1], catgory[2]))          
	res = cur.fetchone()

	if res is None:
		return False
	return True

# get category list and url list.
def getCategory(con):
	cur = con.cursor()
	cur.execute("SELECT * FROM category")
	
	data = cur.fetchall()

	cur.close()
	
	return data	

# check whether the given product is in database or not
def checkProduct(con, product_url):
	cur = con.cursor()
	cur.execute("SELECT * FROM product WHERE product_url='%s'" % product_url)          
	res = cur.fetchone()
	cur.close()

	return res


	
# check the products have same price.
def checkOriginPrice(con, product_url, price):
	cur = con.cursor()
	cur.execute("SELECT * FROM product WHERE product_url='%s' and price = '%s'" % (product_url, price))          
	res = cur.fetchone()
	cur.close()

	return res


# check the products have same price.
def checkPrice(con, product_url, price):
	cur = con.cursor()
	cur.execute("SELECT * FROM product WHERE product_url='%s' and discounted_price = '%s'" % (product_url, price))          
	res = cur.fetchone()
	cur.close()

	return res

# execute any query that doesn't return the result (like insert, update and delete).
def exe_query(con, query):
	cur = con.cursor()
	cur.execute(query)
	con.commit()
	cur.close()
	

if __name__ == '__main__':
	con = getConnection()
	getCategory(con)
