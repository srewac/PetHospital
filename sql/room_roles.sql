-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: pet_hospital
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `navigation_room_roles`
--

DROP TABLE IF EXISTS `navigation_room_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `navigation_room_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `room_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Navigation_room_roles_room_id_role_id_b3440555_uniq` (`room_id`,`role_id`),
  KEY `Navigation_room_roles_role_id_f3cff54f_fk_Navigation_role_id` (`role_id`),
  CONSTRAINT `Navigation_room_roles_role_id_f3cff54f_fk_Navigation_role_id` FOREIGN KEY (`role_id`) REFERENCES `navigation_role` (`id`),
  CONSTRAINT `Navigation_room_roles_room_id_fbb1aa91_fk_Navigation_room_id` FOREIGN KEY (`room_id`) REFERENCES `navigation_room` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `navigation_room_roles`
--

LOCK TABLES `navigation_room_roles` WRITE;
/*!40000 ALTER TABLE `navigation_room_roles` DISABLE KEYS */;
INSERT INTO `navigation_room_roles` VALUES (28,1,1),(2,2,1),(26,3,2),(27,3,3),(33,4,2),(34,4,3),(23,6,3),(29,11,3),(24,12,2),(25,12,3);
/*!40000 ALTER TABLE `navigation_room_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'pet_hospital'
--

--
-- Dumping routines for database 'pet_hospital'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-23  0:27:12
