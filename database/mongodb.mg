use shop;

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
		"additional_attributes":["Display Size"],
	}
);

db.category.insert(
	{
		"name":"Home Theaters",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/speaker-or-home-theatre/home-theater-systems-12%7Cspeakers-22/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["DVD player / recorder"],
	}
);

db.category.insert(
	{
		"name":"Speakers",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/loud-speaker/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-tv_audio-speakers/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[],
	}
);

db.category.insert(
	{
		"name":"Headphones (In ear)",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/Headphones%20and%20Headsets/in-ear%7Cneckband/new/a-5935-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-tv_audio-headphones_and_earphones-in_ear/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Headphone Type","Connectivity"],
	}
);

db.category.insert(
	{
		"name":"Headphones (On ear)",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/head/headphones---and---headsets-373/headband%7Con-ear/new/a-t-5935-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-tv_audio-headphones_and_earphones-on_ear/?limit=30",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Headphone Type","Connectivity"],
	}
);

db.category.insert(
	{
		"name":"Headphones (Over ear)",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/head/headphones---and---headsets-373/over-ear/new/a-t-5935-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-tv_audio-headphones_and_earphones-over_ear/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Headphone Type","Connectivity"],
	}
);

db.category.insert(
	{
		"name":"TV, AV Accessories",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/tv-cable-or-tv-accessories-or-satellite-accessories-or-media-gateways/tv-and-satellite-accessories-28%7Csatellite-receivers-249%7Ctuners-411%7Cmedia-gateways-407%7Ctv-mounts-374/new/a-t-c/s/?sortby=sr",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-tv_audio-tv_av_accessories/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[],
	}
);

db.category.insert(
	{
		"name":"Mp3 and Media Players",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/mp3-player/new/a-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-tv_audio-portable_audio_players-mp3_media_players/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[],
	}
);

db.category.insert(
	{
		"name":"Musical Instruments and DJ",
		"parent":"TV Audio & Video",
		"ancestors":["Electronics", "TV Audio & Video"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/music/musical-instruments-320%7Cmusic-cds-3%7Cmusical-instruments-parts-456%7Crecording-and-studio-equipment-252/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Instrument Type"],
	}
);

db.category.insert(
	{
		"name":"DSLRS",
		"parent":"Camera",
		"ancestors":["Electronics", "Camera"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/digital-camera/slr-camera/new/a-5778-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-cameras_photography-digital_cameras-dslr_cameras/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Megapixel","Screen Size","Battery Life"],
	}
);

db.category.insert(
	{
		"name":"Point and Shoot",
		"parent":"Camera",
		"ancestors":["Electronics", "Camera"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/digital-camera/point-and-shoot%7Ccompact-camera%7Cpoint---and---shoot-camera/new/a-5778-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Megapixel","Screen Size"]
	}
);

db.category.insert(
	{
		"name":"Action Cameras",
		"parent":"Camera",
		"ancestors":["Electronics", "Camera"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/gopro-or-aee-or-goxtreme-or-qrios-or-dji/digital-cameras-14%7Ccamcorders-15/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-cameras_photography-digital_cameras-sports_and_action_video_cameras/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Megapixel"]
	}
);

db.category.insert(
	{
		"name":"Camcorders",
		"parent":"Camera",
		"ancestors":["Electronics", "Camera"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/camcorder/new/a-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Resolution"]
	}
);

db.category.insert(
	{
		"name":"Lens Or Flash",
		"parent":"Camera",
		"ancestors":["Electronics", "Camera"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/lens-or-flash/interchangeable-lenses-375%7Celectronic-flashes-397/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-cameras_photography-lenses/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-flashes/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Type"]
	}
);

db.category.insert(
	{
		"name":"Camera Accesories",
		"parent":"Camera",
		"ancestors":["Electronics", "Camera"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/camera-camcorder-accessories/new/a-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-cases_bags/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-battery_chargers/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-lens_accessories/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-filters/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-lighting_studio/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-tripods_monopods/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories_camera-remote/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-selfie_sticks/,,https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-photo_printers/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Accessory Type"]
	}
);

db.category.insert(
	{
		"name":"Binoculer And Telescopes",
		"parent":"Camera",
		"ancestors":["Electronics", "Camera"],
		"souq_url":{
					url:"",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-cameras_photography-camera_accessories-binoculars_telescopes/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"",
		"parent":"Laptops and Notebooks",
		"ancestors":["Electronics", "Laptops and Notebooks"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/laptop-notebook/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-laptops/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Storage Capacity", "RAM", "Processor Type", "Color", "Operating System Type", "Screen Size"]
	}
);

db.category.insert(
	{
		"name":"Food Processors Choppers and Blenders",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/processor-or-chopper-or-slicer/food-preparation-392%7Cfood-processors-506%7Celectric-slicers-391/full-size-food-processors%7Cchoppers%7Chand-blenders%7Cmini-food-processor%7Ccountertop-blenders/new/a-t-72-c/s/?sortby=sr&page=1,,http://uae.souq.com/ae-en/electric-slicer/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-choppers_and_blenders/?limit=30,,https://en-ae.wadi.com/home_and_kitchen-small_appliances-food_processors/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Vaccuume Cleaners",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/vacuum-cleaner/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-vacuum_cleaners/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Irons",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/irons/irons-393/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-iron/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Juicer Mixers & Grinders",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/juicer/juice-extractors-384/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-juicer_mixers_and_grinders/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Kettles",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/kettle/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-electric_kettle/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Coffee & Tea Maker",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/coffee-machines-or-hot-beverage-makers-or-kettles/coffee---and---espresso-makers-418/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-coffee_makers/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Power Tools",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/power-tools/power-tools-97/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Type"]
	}
);

db.category.insert(
	{
		"name":"Toasters",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/toaster/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-toasters_and_grills/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Sandwhich Makers",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/sandwich-waffle-makers-grill/l/",
					enable: 1
		},
		"wadi_url":{
					url:"",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"SElectric and Rice Cookers",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/rice-cooker/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-electric_cookers/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

db.category.insert(
	{
		"name":"Deep Friers",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/deep-fryer/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-fryers/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":[]
	}
);

{'additional_attributes': '{"Display Size": 65}',
 'brand': u'Samsung',
 'category_id': ObjectId('572bdcaadf2ff6e18e705a46'),
 'delete_flag': False,
 'disable': False,
 'discounted_price': 5999.0,
 'domain': 'uae.souq.com',
 'img_url': u'/home/king/shop_scraper/shopscraper/spiders/images/item_XL_8323623_7941406.jpg',
 'in_stock': True,
 'name': u'Samsung 65 Inch 4K Ultra HD Flat Smart LED TV - UA65JU6400RXEG',
 'price': 9999.0,
 'sku_product_id': '',
 'url': 'http://uae.souq.com/ae-en/samsung-65-inch-4k-ultra-hd-flat-smart-led-tv-ua65ju6400rxeg-8323623/i/'}

