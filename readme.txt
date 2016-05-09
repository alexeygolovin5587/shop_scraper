- About the new version

You can see mongodb insert commands for 150 categories in database/mongodb.mg
Please run these commands,b before running spiders.


1. Description

	It's a demo version of scraping souq.com with only one category.
	But it has the main structure of a project.

2. Run

	In shopscraper/, run:
	$ python start_crawler.py souq

	- running options

		--all: the program scraped all products, even if a product is in the database. (first scrapping mode1)
		--csv: save scraped data in csv file

	I use the following sample data in this demo.

	db.category.insert(
		{
			"name":"TV",
			"parent":"TV Audio & Video",
			"ancestors":["Electronics", "TV Audio & Video"],
			"souq_url":{
						url:"http://uae.souq.com/ae-en/lcd-led-dlp-tv/l/",
						enable: 1
			},
			"wadi_url":{
						url:"https://en-ae.wadi.com/electronics-tv_audio-televisions",
						enable: 1
			},
			"namshi_url":{
						url:"",
						enable: 1
			},
			"additional_attributes":"Display Size",
		}
	)

3. Result

	In shopscraper/data/, you can see 'souq_category.csv', 'wadi_category.csv' and 'namshi_category.csv' which have their category list.
