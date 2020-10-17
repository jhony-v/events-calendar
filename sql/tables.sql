DROP DATABASE IF EXISTS events_calendar;
CREATE DATABASE IF NOT EXISTS events_calendar;
USE events_calendar;
-- user table
CREATE TABLE `User`(
    userId BIGINT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    fullName VARCHAR(100) DEFAULT "",
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    userPassword VARCHAR(100) NOT NULL,
    createdDate DATETIME DEFAULT NOW(),
    profileImage VARCHAR(500) DEFAULT "",
    backgroundImage VARCHAR(500) DEFAULT "",
    userDescription VARCHAR(500)
);

