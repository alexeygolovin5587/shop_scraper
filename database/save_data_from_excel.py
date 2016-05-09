from database_manager import *
		

# read basic information for scraping from 'Product Attributes - Product Attributes.csv' and save them into database
def saveData():
	
	# open 'Product Attributes - Product Attributes.csv' file
	with open('Product Attributes - Product Attributes.csv', 'rb') as f:
		lines = f.readlines()
	
	# get database connection
	con = getConnection()
	cur = con.cursor()  
	index = 2
	# save data into database
	for line in lines[1:]:
		line = line.encode('utf8')
		elements = line.split(',')
		
		if len(elements) < 10:
			continue
		checked = checkCategory(cur, [elements[0], elements[1], elements[2]])
		# if the category in database, skip this category to save.
		if checked is True:
			continue
	
		# get string of additional fields seperated by comma.
		extra_field = ""
		if len(elements) >= 12:
			extra_field = ','.join([field.strip() for field in elements[12:] if field is not ''])
		
		index += 1
		# insert data into category
		query = "INSERT INTO category (category1, category2, category3, souq_url, wadi_url, namshi_url, extra_field) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (elements[0], elements[1], convertSpecialCharactertoNormal(elements[2]), convertSpecialCharactertoNormal(elements[3]), elements[4], elements[5], extra_field)

		cur.execute(query)   

		print query
		
			
	con.commit()

# convert ' character into random string
def convertSpecialCharactertoNormal(str_val):
	return str_val.replace('\'', 'weerweerwrwe')

if __name__ == '__main__':
	saveData()
	

