from pymongo import MongoClient


# get database connection
def getConnection():
	# connect to local server
	client = MongoClient()	

	# connect to remote server
	#client = MongoClient("mongodb://mongodb0.example.net:27019") 

	# use a database named 'shop'
	db = client.shop
	return db

# check whether the given catgory is in database or not
def checkCategory(db, category):
	query = {
		"name": category[2],
		"parent": category[1],
		"ancestors": [category[0], category[1]]
	}

	cursor = db.category.find(query)

	for document in cursor:
			return True
	return False

# get category list and url list.
def getCategory(db):
	return db.category.find()

# check whether the given product is in database or not
def checkProduct(db, product_url):
	query = {"product_url":product_url}

	cursor = db.product.find(query)

	for document in cursor:
			return True
	return False

# check the products have same price.
def checkOriginPrice(db, product_url, price):
	query = {"product_url":product_url, "price":price}

	cursor = db.product.find(query)

	for document in cursor:
			return True
	return False

# check the products have same price.
def checkPrice(db, product_url, price):
	query = {"product_url":product_url, "discounted_price":price}

	cursor = db.product.find(query)

	for document in cursor:
			return True
	return False

# execute any query that doesn't return the result (like insert, update and delete).
def update_db(table, where, data):
	table.update_many(where, {"$set":data})	

if __name__ == '__main__':
	db = getConnection()

	# print checkCategory(db, ['Electronics', 'TV Audio & Video', 'TVp'])
	#update_db(db.product, {"product_url":"http://uae.souq.com/ae-en/lcd-led-dlp-tv/l/"}, {"discounted_price":14.2})
	db.product.insert_one({"pp":"p"})



