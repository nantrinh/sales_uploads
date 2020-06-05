#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;

    CREATE TABLE sales(
    	id serial PRIMARY KEY,
    	customer_name VARCHAR (250) NOT NULL,
    	description VARCHAR (250),
    	price MONEY NOT NULL,
    	quantity INT NOT NULL,
    	merchant_name VARCHAR (250) NOT NULL,
    	merchant_address VARCHAR (250) NOT NULL,
        date DATE NOT NULL DEFAULT CURRENT_DATE, 
    	created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

    INSERT INTO sales (customer_name, description, price, quantity, merchant_name, merchant_address) VALUES
      ('Customer 1', 'apples', 1.50, 3, 'Apple seller', '123 Hello World'),
      ('Customer 2', 'oranges', 3.01, 4, 'Orange Seller', '456 Hello World'),
      ('Customer 3', 'pineapple', 2.00, 2, 'Pineapple Seller', '789 Something Lane'),
      ('A lovely cat', 'chicken noodle soup', 10000.00, 5, 'Warm Things', '80 Firefly Hill');
EOSQL