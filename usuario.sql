/*
CREATE DATABASE Ejem01;
CREATE USER 'newuser'@'usr_pyapps' IDENTIFIED BY 'verso2708';
GRANT ALL PRIVILEGES ON Ejem01.* TO 'usr_pyapps'@'localhost';
FLUSH PRIVILEGES;

*/
CREATE TABLE usuario (
	id tinyint AUTO_INCREMENT PRIMARY KEY,
	tipo tinyint NOT NULL,
	nick VARCHAR (128) NOT NULL,
	password VARCHAR (128) NOT NULL,
	registrado DATETIME NOT NULL
)ENGINE=InnoDB;

INSERT INTO usuario VALUES (NULL,0,"admin",sha2("PROGRAII2022",256),now());
