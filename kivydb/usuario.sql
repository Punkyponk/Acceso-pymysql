CREATE DATABASE Ejem01;
CREATE USER 'user_pyapps'@'localhost' IDENTIFIED BY 'zqFXVf88jdNv4bhr';
GRANT ALL PRIVILEGES ON Ejem01.* TO 'user_pyapps'@'localhost';
FLUSH PRIVILEGES;

USE Ejem01;
CREATE TABLE usuario (
	id tinyint(3) AUTO_INCREMENT PRIMARY KEY,
	tipo tinyint(2) NOT NULL,
	nick varchar(128) UNIQUE NOT NULL,
	password varchar(128) NOT NULL,
	registrado datetime NOT NULL
)ENGINE=InnoDB;

INSERT INTO usuario VALUES (null,0,"super",sha2("PROGRAII2022",256),now());
