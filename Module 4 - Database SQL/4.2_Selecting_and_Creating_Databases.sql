CREATE DATABASE `education`; #Back ticks 
SHOW DATABASES;
Drop Database `education`;

#Defense statements
DROP DATABASE IF EXISTS `education`;

CREATE DATABASE IF NOT EXISTS `education`;

#Selecting Database
USE `education`;

## A character SET is used to define the characters that are legal in a string
SET NAMES UTF8MB4;
SET character_set_client = UTF8MB4;

#Creating a table
CREATE TABLE `Colleges` (
	`CollegeID` int NOT NULL,
    `Name` 		varchar(20) NOT NULL,
    `Students`	int NULL,
    `City` 		varchar(15) NULL,
    `Region`	varchar(15) NULL,
    `Country` 	varchar(15) NULL
) engine= InnoDB default charset= utf8mb4 collate= utf8mb4_0900_ai_ci;

#List of the tables in the databases
SHOW TABLES;

#Drop tables, defense statements
DROP TABLE IF EXISTS `colleges`;

#Adding a primary key
CREATE TABLE `Colleges` (
	`CollegeID` int NOT NULL AUTO_INCREMENT,
	`Name` 		varchar(20) NOT NULL,
    `Students`	int NULL,
    `City` 		varchar(15) NULL,
    `Region`	varchar(15) NULL,
    `Country` 	varchar(15) NULL,
    PRIMARY KEY (`CollegeID`)
) engine= InnoDB default charset= utf8mb4 collate= utf8mb4_0900_ai_ci;

#Database Datatypes 
## Character Types are the best choice when having leading zeros, such as ZIP Codes

#Indexing a database
DROP TABLE IF EXISTS `colleges`;

CREATE TABLE `Colleges` (
	`CollegeID` int NOT NULL AUTO_INCREMENT,
	`Name` 		varchar(20) NOT NULL,
    `Students`	int NULL,
    `City` 		varchar(15) NULL,
    `Region`	varchar(15) NULL,
    `Country` 	varchar(15) NULL,
    PRIMARY KEY (`CollegeID`),
    INDEX `CollegeID` (`CollegeID` ASC),
    INDEX `NAME` (`NAME` ASC)
) engine= InnoDB default charset= utf8mb4 collate= utf8mb4_0900_ai_ci;

#Adding Data to `Colleges` Databases
INSERT INTO `Colleges` VALUES(1,'MIT', 11, 'Cambridge', 'MA', 'USA');
INSERT INTO `Colleges` VALUES(2,'Brown', 9, 'Providence', 'RI', 'USA');
INSERT INTO `Colleges` VALUES(3,'Darmouth', 6, 'Hanover', 'NH', 'USA');
INSERT INTO `Colleges` VALUES
(4, 'Harvard', 20, 'Cambridge', 'MA', 'USA'),
(5, 'Stanford', 15, 'Stanford', 'CA', 'USA'),
(6, 'Yale', 12, 'New Haven', 'CT', 'USA'),
(7, 'Princeton', 10, 'Princeton', 'NJ', 'USA'),
(8, 'Columbia', 14, 'New York', 'NY', 'USA'),
(9, 'UChicago', 13, 'Chicago', 'IL', 'USA'),
(10, 'UPenn', 16, 'Philadelphia', 'PA', 'USA'),
(11, 'Caltech', 8, 'Pasadena', 'CA', 'USA'),
(12, 'Duke', 7, 'Durham', 'NC', 'USA'),
(13, 'Johns Hopkins', 9, 'Baltimore', 'MD', 'USA'),
(14, 'Northwestern', 11, 'Evanston', 'IL', 'USA'),
(15, 'Cornell', 10, 'Ithaca', 'NY', 'USA'),
(16, 'Rice', 5, 'Houston', 'TX', 'USA'),
(17, 'Vanderbilt', 6, 'Nashville', 'TN', 'USA'),
(18, 'Notre Dame', 7, 'Notre Dame', 'IN', 'USA'),
(19, 'Georgetown', 8, 'Washington', 'DC', 'USA'),
(20, 'Emory', 6, 'Atlanta', 'GA', 'USA');

SELECT * FROM Colleges;

#Creating a Students table
CREATE TABLE `Students` (
	`StudentID` int NOT NULL AUTO_INCREMENT,
    `FirstName` varchar(20) NOT NULL, 
    `LastName` varchar(20) NOT NULL,
    `BirthDate` date NOT NULL,
    `Email` varchar(255) NOT NULL,
    `City` varchar(15) NULL,
    `Region` varchar(15) NULL,
    `Country` varchar(15) NULL, 
    `CollegeID` int,
    PRIMARY KEY (`StudentID`),
    FOREIGN KEY (`CollegeID`) REFERENCES `Colleges`(`CollegeID`),
    INDEX `CollegeID` (`CollegeID` ASC),
    INDEX `LastName` (`LastName` ASC),
    INDEX `Email` (`Email` ASC)
) engine= InnoDB default charset= utf8mb4 collate= utf8mb4_0900_ai_ci;

#Adding data to `Students` Table
INSERT INTO `Students` (FirstName, LastName, BirthDate, Email, City, Region, Country, CollegeID) VALUES
('John', 'Doe', '2000-01-01', 'john.doe@example.com', 'Cambridge', 'MA', 'USA', 1),
('Jane', 'Smith', '2001-02-02', 'jane.smith@example.com', 'Providence', 'RI', 'USA', 2),
('Alice', 'Johnson', '2002-03-03', 'alice.johnson@example.com', 'Hanover', 'NH', 'USA', 3),
('Bob', 'Brown', '2000-04-04', 'bob.brown@example.com', 'Cambridge', 'MA', 'USA', 4),
('Charlie', 'Davis', '2001-05-05', 'charlie.davis@example.com', 'Stanford', 'CA', 'USA', 5),
('Diana', 'Miller', '2002-06-06', 'diana.miller@example.com', 'New Haven', 'CT', 'USA', 6),
('Eve', 'Wilson', '2000-07-07', 'eve.wilson@example.com', 'Princeton', 'NJ', 'USA', 7),
('Frank', 'Moore', '2001-08-08', 'frank.moore@example.com', 'New York', 'NY', 'USA', 8),
('Grace', 'Taylor', '2002-09-09', 'grace.taylor@example.com', 'Chicago', 'IL', 'USA', 9),
('Hank', 'Anderson', '2000-10-10', 'hank.anderson@example.com', 'Philadelphia', 'PA', 'USA', 10),
('Ivy', 'Thomas', '2001-11-11', 'ivy.thomas@example.com', 'Pasadena', 'CA', 'USA', 11),
('Jack', 'Jackson', '2002-12-12', 'jack.jackson@example.com', 'Durham', 'NC', 'USA', 12),
('Karen', 'White', '2000-01-13', 'karen.white@example.com', 'Baltimore', 'MD', 'USA', 13),
('Leo', 'Harris', '2001-02-14', 'leo.harris@example.com', 'Evanston', 'IL', 'USA', 14),
('Mia', 'Martin', '2002-03-15', 'mia.martin@example.com', 'Ithaca', 'NY', 'USA', 15),
('Nina', 'Lee', '2000-04-16', 'nina.lee@example.com', 'Houston', 'TX', 'USA', 16),
('Oscar', 'Walker', '2001-05-17', 'oscar.walker@example.com', 'Nashville', 'TN', 'USA', 17),
('Paul', 'Hall', '2002-06-18', 'paul.hall@example.com', 'Notre Dame', 'IN', 'USA', 18),
('Quinn', 'Allen', '2000-07-19', 'quinn.allen@example.com', 'Washington', 'DC', 'USA', 19),
('Rose', 'Young', '2001-08-20', 'rose.young@example.com', 'Atlanta', 'GA', 'USA', 20),
('Sam', 'King', '2002-09-21', 'sam.king@example.com', 'Cambridge', 'MA', 'USA', 1),
('Tina', 'Scott', '2000-10-22', 'tina.scott@example.com', 'Providence', 'RI', 'USA', 2),
('Uma', 'Green', '2001-11-23', 'uma.green@example.com', 'Hanover', 'NH', 'USA', 3),
('Victor', 'Adams', '2002-12-24', 'victor.adams@example.com', 'Cambridge', 'MA', 'USA', 4),
('Wendy', 'Baker', '2000-01-25', 'wendy.baker@example.com', 'Stanford', 'CA', 'USA', 5),
('Xander', 'Carter', '2001-02-26', 'xander.carter@example.com', 'New Haven', 'CT', 'USA', 6),
('Yara', 'Evans', '2002-03-27', 'yara.evans@example.com', 'Princeton', 'NJ', 'USA', 7),
('Zane', 'Foster', '2000-04-28', 'zane.foster@example.com', 'New York', 'NY', 'USA', 8),
('Amy', 'Gonzalez', '2001-05-29', 'amy.gonzalez@example.com', 'Chicago', 'IL', 'USA', 9),
('Brian', 'Hughes', '2002-06-30', 'brian.hughes@example.com', 'Philadelphia', 'PA', 'USA', 10),
('Cathy', 'James', '2000-07-31', 'cathy.james@example.com', 'Pasadena', 'CA', 'USA', 11),
('David', 'Kelly', '2001-08-01', 'david.kelly@example.com', 'Durham', 'NC', 'USA', 12),
('Ella', 'Lewis', '2002-09-02', 'ella.lewis@example.com', 'Baltimore', 'MD', 'USA', 13),
('Fred', 'Martinez', '2000-10-03', 'fred.martinez@example.com', 'Evanston', 'IL', 'USA', 14),
('Gina', 'Nelson', '2001-11-04', 'gina.nelson@example.com', 'Ithaca', 'NY', 'USA', 15),
('Harry', 'Ortiz', '2002-12-05', 'harry.ortiz@example.com', 'Houston', 'TX', 'USA', 16),
('Iris', 'Perez', '2000-01-06', 'iris.perez@example.com', 'Nashville', 'TN', 'USA', 17),
('Jake', 'Ramirez', '2001-02-07', 'jake.ramirez@example.com', 'Notre Dame', 'IN', 'USA', 18),
('Kara', 'Sanchez', '2002-03-08', 'kara.sanchez@example.com', 'Washington', 'DC', 'USA', 19),
('Liam', 'Turner', '2000-04-09', 'liam.turner@example.com', 'Atlanta', 'GA', 'USA', 20);

SELECT * FROM Students;

#Update and Delete Data
SELECT * FROM Colleges;

## When trying to not use safe mode
Set SQL_SAFE_UPDATES = 0;
UPDATE Colleges SET Country= 'U.S.';

#Update a row based on a condition
UPDATE Colleges
SET Country = 'USA'
WHERE Region = 'MA';

#Delete some of the rows in the table
DELETE FROM Colleges 
WHERE Name = 'Darmouth';

DROP TABLES IF EXISTS `Students`;
DROP TABLE IF EXISTS `Colleges`;
DROP DATABASE IF EXISTS `education`;