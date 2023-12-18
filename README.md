# Employee-CRUD-Console-APP
Fully Validated (From Scratch) CRUD (Create, Read, Update &amp; Delete) Application using MySQL Database

## To Run the Application
### Paste This code to MySQL WorkBench
```
CREATE DATABASE  IF NOT EXISTS `crud` 
USE `crud`;

CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `ssn` bigint NOT NULL,
  `contract_date` date NOT NULL,
  `age` int NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `phone_UNIQUE` (`phone`),
  UNIQUE KEY `ssn_UNIQUE` (`ssn`),
  UNIQUE KEY `email_UNIQUE` (`email`)
)
```
### Ensure to Change the connection Config To your Device's Configuration
#### in the First Code Block
```
# Establish a connection to the MySQL database with the specified parameters.
connection_config = {
    'host': 'localhost',
    'password': '1234',
    'user': 'root',
    'database': 'crud'
}
```
## Run the Script

#### 📧 Contact: [omarhany2k@gmail.com](omarhany2k@gmail.com)


