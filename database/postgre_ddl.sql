CREATE TABLE Category (
    ID            SERIAL      PRIMARY KEY,
    Category1    	VARCHAR(50) not null,
    Category2     VARCHAR(50) not null,
    Category3     VARCHAR(50) not null,
    Souq_url  TEXT,
	Wadi_url  TEXT,
	Namshi_url  TEXT,
	Extra_field VARCHAR(200)
);

CREATE TABLE Product (
    ID            			SERIAL      PRIMARY KEY,
    Product_name    		VARCHAR(200),
    Brand_name		     	VARCHAR(100),
	Product_url			TEXT,
	Image_url			TEXT,
    SKU_Product_ID     	VARCHAR(50),
    Price  							VARCHAR(50),
	Discounted_price		VARCHAR(50),
	In_stock						BOOLEAN not null default FALSE,
	Domain							VARCHAR(50),
	Disable							BOOLEAN not null default FALSE,
	Delete_flag					BOOLEAN not null default FALSE,
	Category_id					INT not null
);

CREATE TABLE Additional_Attribute (
    ID            SERIAL      PRIMARY KEY,
    Name    			VARCHAR(100) not null,
    Value				  TEXT,
	Product_id		INT not null
);
