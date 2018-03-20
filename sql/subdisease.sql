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
-- Table structure for table `disease_subdisease`
--

DROP TABLE IF EXISTS `disease_subdisease`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_subdisease` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `pic_url` varchar(500) NOT NULL,
  `disease_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Disease_subdisease_disease_id_2dccbe70_fk_Disease_disease_id` (`disease_id`),
  CONSTRAINT `Disease_subdisease_disease_id_2dccbe70_fk_Disease_disease_id` FOREIGN KEY (`disease_id`) REFERENCES `disease_disease` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease_subdisease`
--

LOCK TABLES `disease_subdisease` WRITE;
/*!40000 ALTER TABLE `disease_subdisease` DISABLE KEYS */;
INSERT INTO `disease_subdisease` VALUES (1,'犬瘟热','犬瘟热是由犬瘟热病毒引起的一种高度接触性传染病，传染性极强，死亡率可高达80%以上。','static/images/sub_diseases/distemper.jpg',1),(2,'犬细小病毒','犬细小病毒病是犬的一种具有高度接触性传染的烈性传染病，该病症于1977年由Eugster发现，临床上以急性出血性肠炎和心肌炎为特征。','static/images/sub_diseases/parvovirus.jpg',1),(3,'犬传染性肝炎','犬传染性肝炎主要发生在1岁以内的幼犬，成年犬很少发生且多为隐性感染，即使发病也多能耐过。','static/images/sub_diseases/HCC.jpg',1),(4,'犬冠状病毒','犬冠状病毒一年四季均可发生，以冬季多发，病犬是主要的传染原，犬可通过呼吸道、消化道、粪便及污染物传染。该病一但发生，同窝犬同室犬很难控制均可造成感染。','static/images/sub_diseases/CVV.jpg',1),(5,'猫泛白细胞减少症','猫泛白细胞减少症，又称猫瘟热，猫传染性肠炎，是猫的一种急性高度接触性传染病。','istatic/images/sub_diseases/panleukopenia.jpg',1),(6,'猫病毒性病气管炎','猫病毒性病气管炎是猫的上部呼吸道感染性非常强的一种急性传染病,又称为传染性鼻气管炎。','static/images/sub_diseases/tracheitis.jpg',1),(7,'皮肤真菌感染','皮肤真菌病的传播主要是通过动物间的互相接触，或通过污染的物体而传播。在宠物数量较多且较密集的情况下，也可通过空气传播。','static/images/sub_diseases/fungal.jpg',1),(8,'蛔虫病','蛔虫病','',2),(9,'钩虫病','钩虫病','',2),(10,'绦虫病','绦虫病','',2),(11,'球虫病','球虫病','',2),(12,'疥螨虫病','疥螨虫病','',2),(13,'蚤病','蚤病','',2),(14,'口炎','口炎','',3),(15,'肠炎','肠炎','',3),(16,'肠便秘','肠便秘','',3),(17,'胰腺炎','胰腺炎','',3),(18,'肝炎','肝炎','',3),(19,'腹膜炎','腹膜炎','',3),(20,'肛门腺炎','肛门腺炎','',3),(21,'感冒','感冒','',3),(22,'鼻炎','鼻炎','',3),(23,'气管支气管炎','气管支气管炎','',3),(24,'肺炎','肺炎','',3),(25,'心力衰竭','心力衰竭','',3),(26,'尿道感染','尿道感染','',3),(27,'尿结石','尿结石','',3),(28,'膀胱炎','膀胱炎','',3),(29,'肾炎','肾炎','',3),(30,'佝偻病','佝偻病','',3),(31,'有机磷中毒','有机磷中毒','',3),(32,'糖尿病','糖尿病','',3),(33,'耳血肿','耳血肿','',3),(34,'中耳炎','中耳炎','',3),(35,'眼睑内翻','眼睑内翻','',3),(36,'结膜炎','结膜炎','',3),(37,'角膜炎','角膜炎','',3),(38,'外伤','外伤','',4),(39,'外科感染','外科感染','',4),(40,'骨折','骨折','',4),(41,'关节脱位','关节脱位','',4),(42,'湿疹','湿疹','',4),(43,'皮炎','皮炎','',4),(44,'脓皮病','脓皮病','',4),(45,'脱毛症','脱毛症','',4),(46,'趾间囊肿','趾间囊肿','',4),(47,'疝','疝','',4),(48,'阴道炎','阴道炎','',4),(49,'阴道脱出','阴道脱出','',4),(50,'子宫蓄脓','子宫蓄脓','',4),(51,'难产','难产','',4),(52,'乳房炎','乳房炎','',4),(53,'绝育','绝育','',5),(54,'剖腹产','剖腹产','',5),(55,'瞬膜腺增生物切除','瞬膜腺增生物切除','',5),(56,'眼球摘除','眼球摘除','',5),(57,'立耳术','立耳术','',5),(58,'断尾术','断尾术','',5),(59,'犬免疫程序','犬免疫程序','',6),(60,'猫免疫程序','猫免疫程序','',6);
/*!40000 ALTER TABLE `disease_subdisease` ENABLE KEYS */;
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

-- Dump completed on 2018-03-20 15:26:18
