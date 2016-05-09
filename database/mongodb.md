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

db.category.insert(
	{
		"name":"Fans",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/fan/fans-261/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-fan/",
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
		"name":"Heaters",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/heater/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-heater/",
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
		"name":"Gas Stoves",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/gas-stoves/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-gas_stoves/",
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
		"name":"Water Dispenser",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/water-dispenser/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-water_dispenser/?limit=30",
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
		"name":"Security and Surveillance Systems",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/security-surveillance-system/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-home_security/",
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
		"name":"Air Purifier",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/air-treatment/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-air_purifiers/",
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
		"name":"Telephones",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/telephone/telephones-34/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-landline_phones/",
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
		"name":"Garment Steamers",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/garment-steamer/s/",
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
		"name":"Coolers",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/air-coolers/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-coolers/",
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
		"name":"Sewing and Accessories",
		"parent":"Home and Small Appliances",
		"ancestors":["Electronics", "Home and Small Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/sewing-accessories/l/",
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
		"name":"Ovens",
		"parent":"Large Appliances",
		"ancestors":["Electronics", "Large Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/ovens-ranges/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-ovens_and_otgs/",
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
		"name":"Microwaves",
		"parent":"Large Appliances",
		"ancestors":["Electronics", "Large Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/microwave/microwaves-444/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-small_appliances-microwaves/",
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
		"name":"Dishwashers",
		"parent":"Large Appliances",
		"ancestors":["Electronics", "Large Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/dishwashers/l/",
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
		"name":"Dryers",
		"parent":"Large Appliances",
		"ancestors":["Electronics", "Large Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/dryers/l/",
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
		"name":"Refrigerators & Freezer",
		"parent":"Large Appliances",
		"ancestors":["Electronics", "Large Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/refrigerators-freezers/l/",
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
		"additional_attributes":["Color", "Style"]
	}
);

db.category.insert(
	{
		"name":"Wasing Machine",
		"parent":"Large Appliances",
		"ancestors":["Electronics", "Large Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/washing-machine/large-appliances-256/a-t/s/",
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
		"additional_attributes":["Color", "Loading Type"]
	}
);

db.category.insert(
	{
		"name":"Floor Care",
		"parent":"Large Appliances",
		"ancestors":["Electronics", "Large Appliances"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/floor-care/s/",
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
		"name":"Consoles",
		"parent":"Gaming",
		"ancestors":["Electronics", "Gaming"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/games-console/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-gaming_accessories-gaming_consoles/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Platform"]
	}
);

db.category.insert(
	{
		"name":"Gaming Accessories",
		"parent":"Gaming",
		"ancestors":["Electronics", "Gaming"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/games-console-accessories/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-gaming_accessories-gaming_accessories-controllers/",
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
		"name":"Video Games",
		"parent":"Gaming",
		"ancestors":["Electronics", "Gaming"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/games/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-gaming_accessories-gaming_titles/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Platform"]
	}
);

'''db.category.insert(
	{
		"name":"Video Games",
		"parent":"Gaming",
		"ancestors":["Electronics", "Gaming"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/games/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-gaming_accessories-gaming_titles/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Platform"]
	}
);'''

db.category.insert(
	{
		"name":"Bags and Carry Cases",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/Bag-carrying-Case/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-computer_accessories-laptop_bags_sleeves/?limit=30",
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
		"name":"Barcode Readers",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/barcode-reader/l/",
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
		"name":"Chargers",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/laptop-charger/l/",
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
		"name":"Computer Casing",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/computer-casing/l/",
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
		"name":"Computer Fans",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/compters-fan/l/",
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
		"name":"Computer and Laptop Accessory",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/computer-peripheral/l/",
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
		"additional_attributes":["Accessory Type"]
	}
);

db.category.insert(
	{
		"name":"Hard Drives",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/hard-disk/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-storage_devices-external_hard_drive/?limit=30",
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
		"name":"Keyboards",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/keyboard/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-computer_accessories-keyboards/",
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
		"name":"Memory Cards",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/memory-card/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-storage_devices-memory_cards/",
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
		"name":"Microphones",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/memory-card/l/",
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
		"name":"Motherboard",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/motherboard/l/",
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
		"additional_attributes":["Processor Manufacturer"]
	}
);

db.category.insert(
	{
		"name":"Mouse and Mouse Pads",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/computer-mouse/l/,,http://uae.souq.com/ae-en/mouse-pad/computer---and---laptop-accessories-187/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-gaming_accessories-gaming_accessories-mouse_pads/",
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
		"name":"PC Media Players & Speakers",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/pc-media-player-speaker/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-gaming_accessories-gaming_accessories-mouse_pads/",
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
		"name":"Skin and Decals",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/skins-decals/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_accessories-mobile_cases_covers/?q=skin&ref=suggest,,https://en-ae.wadi.com/electronics-computers_laptops_storage-computer_accessories-laptop_skins/",
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
		"name":"USB Flash Drives",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/mobile-usb-memory/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-storage_devices-pen_drive/",
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
		"name":"USB Hubs",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/usb-hubs/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-computer_accessories-cable_connections/?q=usb%20hub&ref=suggest",
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
		"name":"Card Readers / Writers",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/card-reader-writer/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-computer_accessories/?q=card%20reader&ref=suggest",
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
		"name":"Cooling Pads and Fans",
		"parent":"IT Accessories",
		"ancestors":["Computers, IT & Networking", "IT Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/cooling-pad/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-computer_accessories-cooling_pads_laptop_tables/",
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
		"name":"Computers Monitors",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/computer-monitor/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-desktops_monitors-monitors/",
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
		"name":"CPU",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/cpu-ram/l/",
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
		"additional_attributes":["CPU Speed", "Processor Family"]
	}
);

db.category.insert(
	{
		"name":"Memory Module",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/usb-drive-memory/l/",
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
		"name":"Optical Drives",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/optical-drive/l/",
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
		"name":"Power Supply",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/power-supply/l/",
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
		"name":"Sound Card",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/sound-card/l/",
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
		"name":"Video Cards",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/video-card/l/",
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
		"name":"Webcams",
		"parent":"Computer Parts & Components",
		"ancestors":["Computers, IT & Networking", "Computer Parts & Components"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/webcam/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-computer_accessories-webcams/?limit=30",
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
		"name":"Desktop PCs",
		"parent":"Desktops & Servers",
		"ancestors":["Computers, IT & Networking", "Desktops & Servers"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/computer/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/catalog/?q=desktop&ref=suggest",
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
		"name":"Servers",
		"parent":"Desktops & Servers",
		"ancestors":["Computers, IT & Networking", "Desktops & Servers"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/server/l/",
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
		"name":"Blank CDs",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/blank-cd/l/",
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
		"name":"Blank DVDs",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/blank-dvd/l/",
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
		"name":"Cables",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/cables/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-tv_audio-tv_av_accessories-hdmi_analog_cables/",
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
		"name":"Storage Devices",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/shop-all-categories/c/",
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
		"name":"Docking Stations",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/docking-station/l/",
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
		"name":"Network Card and Adapters",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/network-card-adapter/l/",
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
		"name":"Network Switches",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/network-switch/l/",
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
		"name":"Networking Tools",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/networking-tool/l/",
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
		"name":"Routers",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/router/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-computers_laptops_storage-routers_modems-routers/",
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
		"name":"UPS",
		"parent":"Networking & Accessories",
		"ancestors":["Computers, IT & Networking", "Networking & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/uninterruptible-power-supply-ups/l/",
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
		"name":"3d Printers",
		"parent":"Printers, Scanners, Hardware & Accessories",
		"ancestors":["Computers, IT & Networking", "Printers, Scanners, Hardware & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/3d-printers/l/",
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
		"name":"Printers",
		"parent":"Printers, Scanners, Hardware & Accessories",
		"ancestors":["Computers, IT & Networking", "Printers, Scanners, Hardware & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/printer/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics/?limit=30&q=printers",
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
		"name":"Ink & Toner Cartridges",
		"parent":"Printers, Scanners, Hardware & Accessories",
		"ancestors":["Computers, IT & Networking", "Printers, Scanners, Hardware & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/ink-cartridges/l/",
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
		"name":"Scanners",
		"parent":"Printers, Scanners, Hardware & Accessories",
		"ancestors":["Computers, IT & Networking", "Printers, Scanners, Hardware & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/scanner/l/",
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
		"name":"Printer and Scanner Accessories",
		"parent":"Printers, Scanners, Hardware & Accessories",
		"ancestors":["Computers, IT & Networking", "Printers, Scanners, Hardware & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/printer-scanner-accessories/l/",
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
		"name":"Label Printers",
		"parent":"Printers, Scanners, Hardware & Accessories",
		"ancestors":["Computers, IT & Networking", "Printers, Scanners, Hardware & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/label-printers/l/",
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
		"name":"Computer Software",
		"parent":"Software",
		"ancestors":["Computers, IT & Networking", "Software"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/software/l/",
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
		"name":"Mobile Phones",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/mobile-phone/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_phones-basic_phones/,,https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_phones-smartphones/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Type", "Operating System", "Color"]
	}
);

db.category.insert(
	{
		"name":"Fancy Numbers",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/phone-number-line/l/",
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
		"name":"Screen Protectors",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/screen-protectors/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_accessories-screen_protector_screen_guards/",
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
		"name":"Mobile Phone Accessories",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/mobile-phone-accessories/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_accessories-mobile_cases_covers/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Mobile Accessory Type", "Color"]
	}
);

db.category.insert(
	{
		"name":"Smart Watches",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/smart-watches/l/,,http://uae.souq.com/ae-en/fitness_technology/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_accessories-wearable_devices/?q=smart%20watch&ref=suggest",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Color"]
	}
);

db.category.insert(
	{
		"name":"Tablets",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/tablet/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-tablets/",
					enable: 1
		},
		"namshi_url":{
					url:"",
					enable: 1
		},
		"additional_attributes":["Operating System", "Storage Capacity", "Screen Size", "Color"]
	}
);

db.category.insert(
	{
		"name":"Chargers & Power Banks",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/laptop-charger/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_accessories-cables_chargers/,,https://en-ae.wadi.com/electronics-mobiles_tablets-mobile_accessories-power_banks/",
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
		"name":"Tablet Accessories",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/tablet-accessories/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/electronics-mobiles_tablets-tablet_accessories-tablet_cases_covers/",
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
		"name":"Watch Accessories",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/watch-accessories/l/",
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
		"name":"3D Glasses",
		"parent":"Mobile Phones, Tablets & Accessories",
		"ancestors":["Electronics", "Mobile Phones, Tablets & Accessories"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/3d-glasses/new/a-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"http://uae.souq.com/ae-en/samsung-gear-vr-for-galaxy-note-5-galaxy-s6-edge-plus-galaxy-s6-white-sm-r322nzwax-9630261/i/",
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
		"name":"Diapers",
		"parent":"Baby",
		"ancestors":["Baby and Kids", "Baby"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/watch-accessories/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys-kids-and-baby-baby_and_toddlers-diaper_and_diaper_bags/?limit=30",
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
		"name":"Baby Food",
		"parent":"Baby",
		"ancestors":["Baby and Kids", "Baby"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/baby-food/new/a-c/l/",
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
		"additional_attributes":["Recommended Age"]
	}
);

db.category.insert(
	{
		"name":"Feeding",
		"parent":"Baby",
		"ancestors":["Baby and Kids", "Baby"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/feeding-diapering-bathing/new/a-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys-kids-and-baby-baby_and_toddlers-diaper_and_diaper_bags-baby_feeding/?limit=30",
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
		"name":"Baby Bath & Skin Care",
		"parent":"Baby",
		"ancestors":["Baby and Kids", "Baby"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/baby-bath-skin-care/new/a-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys-kids-and-baby-baby_and_toddlers-baby_bath_and_skin/?limit=30",
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
		"name":"Baby Clothes",
		"parent":"Baby",
		"ancestors":["Baby and Kids", "Baby"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/baby-clothes/new/a-c/l/",
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
		"name":"Baby Safety & health",
		"parent":"Baby",
		"ancestors":["Baby and Kids", "Baby"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/baby-safety-health/new/a-c/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys-kids-and-baby-baby_and_toddlers-diaper_and_diaper_bags-baby_safety_and_health/?limit=30",
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
		"name":"Car Seats",
		"parent":"Baby Gear",
		"ancestors":["Baby and Kids", "Baby Gear"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/car-seats-accessories/baby-gears-331/new/a-t-c/s/",
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
		"name":"Strollers",
		"parent":"Baby Gear",
		"ancestors":["Baby and Kids", "Baby Gear"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/stroller/baby-gears-331/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-baby_and_toddlers-diaper_and_diaper_bags-baby_strollers_and_car_seats/?limit=30",
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
		"name":"Swings",
		"parent":"Baby Gear",
		"ancestors":["Baby and Kids", "Baby Gear"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/baby-swings/baby-gears-331/new/a-t-c/s/",
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
		"name":"Portable Beds & Play Yards",
		"parent":"Baby Gear",
		"ancestors":["Baby and Kids", "Baby Gear"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/baby-swings/baby-gears-331/new/a-t-c/s/",
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
		"name":"Highchairs and Boosters",
		"parent":"Baby Gear",
		"ancestors":["Baby and Kids", "Baby Gear"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/baby-seats-and-chairs/baby-gears-331%7Cnursery-furniture---and---d%C3%A9cor-334/new/a-t-c/s/",
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
		"name":"Electronic and RC Toys",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/drone/toys-24/a-t/s/,,http://uae.souq.com/ae-en/cars/toys-24/a-t/s/,,http://uae.souq.com/ae-en/wltoys-v977-brushless-6ch-3d-rc-helicopter-7209773/i/,,http://uae.souq.com/ae-en/quadcopter/toys-24/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-vehicles_models_and_playsets/,,https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-soft_toys-remote_control_toys/",
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
		"name":"Action Figures",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/ae-toys-cms-action-figures/c/",
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
		"name":"Arts and Craft",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/ae-toys-cms-art-craft/c/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys-kids-and-baby-toys_and_activities-board_games-art_and_crafts/",
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
		"name":"Lego",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/ae-toys-cms-lego-building/c/",
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
		"name":"Baby Toys",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/toys/baby-toys-and-accessories-335/new/a-t-c/s/?sortby=ir_desc",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-baby_and_toddlers-diaper_and_diaper_bags-baby_toys_and_playtime/?limit=30",
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
		"name":"Board Games",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/ae-toys-cms-cards-games-puzzle/c/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-board_games/",
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
		"name":"Dolls",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/dolls/toys-24/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys-kids-and-baby-toys_and_activities-soft_toys-dolls_and_doll_houses/",
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
		"name":"Musical Toys",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/musical-toys/toys-24/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-soft_toys-musical_toys/",
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
		"name":"Educational Toys",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/educational-toys/toys-24/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-soft_toys-educational_and_learning_toys/",
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
		"name":"Bikes, Scooters & Ride-Ons",
		"parent":"Toys",
		"ancestors":["Baby and Kids", "Toys"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/bikes-scooters/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-soft_toys-ride_on_and_scooters/",
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
		"name":"Beach Toys",
		"parent":"Outdoor",
		"ancestors":["Baby and Kids", "Outdoor"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/beach-toys/s/",
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
		"name":"Play Houses",
		"parent":"Outdoor",
		"ancestors":["Baby and Kids", "Outdoor"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/play-house/toys-24%7Coutdoor-play-499/new/a-t-c/s/?sortby=cp_desc",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-board_games-activity_sets/?q=playhouse&ref=suggest",
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
		"name":"Slides & Climbers",
		"parent":"Outdoor",
		"ancestors":["Baby and Kids", "Outdoor"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/slide-or-climb/outdoor-play-499%7Cbaby-toys-and-accessories-335/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/toys_kids_and_baby-toys_and_activities-board_games-activity_sets/?q=slide&ref=suggest",
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
		"name":"School Bags",
		"parent":"Bags",
		"ancestors":["Baby and Kids", "Bags"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/school-bags/l/",
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
		"name":"Cookware",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/cookware/new/a-c/s/",
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
		"name":"Bakeware",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/bakeware/new/a-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-kitchenware-cookware_and_bakeware/?limit=30",
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
		"name":"Dinnerware",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/dinnerware/kitchen-and-dining-316/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-kitchenware-dining_and_serving/",
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
		"name":"Serveware",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/serveware/kitchen-and-dining-316/serveware%7Cserveware-and-trays/new/a-t-6346-c/s/?sortby=cp_desc&",
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
		"name":"Kitchen Tools And Gadgets",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/kitchen-tools-and-gadgets/kitchen-and-dining-316/new/a-t-c/s/",
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
		"name":"Drinkware",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/drinkware/drinkware-509%7Ckitchen-and-dining-316/a-t/s/?sortby=cp_desc",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-kitchenware-bar_and_glassware/,,https://en-ae.wadi.com/home_and_kitchen-kitchenware-tea_and_coffee_serveware/",
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
		"name":"Cooking Utensils",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/utensils/l/",
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
		"name":"Fruit & Vegetables",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/fruit-vegetable-tools/l/",
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
		"name":"Flask",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/flask/kitchen-and-dining-316/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/kitchenware-tiffin_and_flasks/",
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
		"name":"Measuring Tool",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/kitchen-measuring-tools/l/",
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
		"name":"Kitchen Storage",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/kitchen-storage/kitchen-and-dining-316/a-t/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-kitchenware-kitchen_storage/",
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
		"name":"Home Supplies",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/home-supplies/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-household_supplies/?limit=30",
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
		"name":"Table Linens",
		"parent":"Kitchen & Home Supplies",
		"ancestors":["Home", "Kitchen & Home Supplies"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/table-linens/l/",
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
		"name":"Duvet Sets",
		"parent":"Bed And Bath",
		"ancestors":["Home", "Bed And Bath"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/duvet-sets/bedding-sets---and---components-135/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-home_furnishing-bed_linen/?q=duvet&ref=suggest",
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
		"name":"Comforter Sets",
		"parent":"Bed And Bath",
		"ancestors":["Home", "Bed And Bath"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/comforter-sets/bedding-sets---and---components-135/new/a-t-c/s/",
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
		"name":"Bedsheet Sets",
		"parent":"Bed And Bath",
		"ancestors":["Home", "Bed And Bath"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/bedsheet-sets/bedding-sets---and---components-135/new/a-t-c/s/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-home_furnishing-bed_linen/",
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
		"name":"Blankets and Throws",
		"parent":"Bed And Bath",
		"ancestors":["Home", "Bed And Bath"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/blankets-throws/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-home_furnishing-blankets_and_quilts/",
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
		"name":"Pillows, Cushions and Covers",
		"parent":"Bed And Bath",
		"ancestors":["Home", "Bed And Bath"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/pillows/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-home_furnishing-pillow_cushion_and_covers/?limit=30",
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
		"name":"Towels",
		"parent":"Bed And Bath",
		"ancestors":["Home", "Bed And Bath"],
		"souq_url":{
					url:"http://uae.souq.com/ae-en/towels/l/",
					enable: 1
		},
		"wadi_url":{
					url:"https://en-ae.wadi.com/home_and_kitchen-home_furnishing-bath_linen/",
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

