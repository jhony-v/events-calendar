DROP DATABASE IF EXISTS events_calendar;
CREATE DATABASE IF NOT EXISTS events_calendar;
USE events_calendar;

CREATE TABLE `User`(
    userId INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    fullName VARCHAR(100) DEFAULT "",
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    userPassword VARCHAR(100) NOT NULL,
    createdDate DATETIME DEFAULT NOW(),
    profileImage VARCHAR(500) DEFAULT "",
    backgroundImage VARCHAR(500) DEFAULT "",
    userDescription VARCHAR(500)
);

CREATE TABLE `Event`(
    eventId INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    title VARCHAR(100) NOT NULL,
    `description` VARCHAR(200),
    eventImage VARCHAR(500),
    startDate DATETIME NOT NULL,
    endDate DATETIME NOT NULL,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    eventCategoryId INT,
    createdByUserId INT
);


CREATE TABLE EventAction(
    eventActionId INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    title VARCHAR(100) NOT NULL,
    `description` VARCHAR(200),
    eventActionImage VARCHAR(500),
    eventId INT NOT NULL
);

CREATE TABLE EventCategory(
    eventCategoryId INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    title VARCHAR(30) NOT NULL
);

CREATE TABLE UserIncludedEvent(
    userId INT,
    eventId INT,
    UNIQUE KEY(userId,eventId)
);

-- ------------------------------------- foreign keys -----------------------------------------------


ALTER TABLE `Event` ADD FOREIGN KEY (eventCategoryId) REFERENCES EventCategory(eventCategoryId) ON DELETE CASCADE;
ALTER TABLE `Event` ADD FOREIGN KEY (createdByUserId) REFERENCES `User`(userId) ON DELETE CASCADE ;
ALTER TABLE EventAction ADD  FOREIGN KEY (eventId) REFERENCES `Event`(eventId);
ALTER TABLE UserIncludedEvent ADD FOREIGN KEY (userId) REFERENCES `User`(userId) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE UserIncludedEvent ADD FOREIGN KEY (eventId) REFERENCES `Event`(eventId) ON DELETE CASCADE ON UPDATE CASCADE;
