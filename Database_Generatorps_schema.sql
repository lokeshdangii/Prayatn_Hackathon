 

-- Table: rr
CREATE TABLE `rr` (
  `id` int DEFAULT NULL,
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `display_name` varchar(255) DEFAULT NULL,
  `creation_date` timestamp NULL DEFAULT NULL,
  `about_me` text,
  `Gravatar_url` varchar(255) DEFAULT NULL,
  `role` enum('Admin','Moderator','Regular User') DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
;

-- Table: t1
CREATE TABLE `t1` (
  `id` int DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
;