-- SQL script to create a table users

-- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, 
-- never null (= default will be the first element of the enumeration, here US)


CREATE TABLE IF NOT EXISTS users
(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
	country VARCHAR(2) DEFAULT 'US' NOT NULL, CONSTRAINT chk_Country CHECK (country in ('US', 'CO', 'TN')), 
    PRIMARY KEY(id)
)