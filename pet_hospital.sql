CREATE DATABASE  IF NOT EXISTS `pet_hospital` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `pet_hospital`;
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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add role',1,'add_role'),(2,'Can change role',1,'change_role'),(3,'Can delete role',1,'delete_role'),(4,'Can add room',2,'add_room'),(5,'Can change room',2,'change_room'),(6,'Can delete room',2,'delete_room'),(7,'Can add room_ role',3,'add_room_role'),(8,'Can change room_ role',3,'change_room_role'),(9,'Can delete room_ role',3,'delete_room_role'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add user_test',5,'add_user_test'),(14,'Can change user_test',5,'change_user_test'),(15,'Can delete user_test',5,'delete_user_test'),(16,'Can add usertest',6,'add_usertest'),(17,'Can change usertest',6,'change_usertest'),(18,'Can delete usertest',6,'delete_usertest'),(19,'Can add usertest_question',7,'add_usertest_question'),(20,'Can change usertest_question',7,'change_usertest_question'),(21,'Can delete usertest_question',7,'delete_usertest_question'),(22,'Can add choice',8,'add_choice'),(23,'Can change choice',8,'change_choice'),(24,'Can delete choice',8,'delete_choice'),(25,'Can add question',9,'add_question'),(26,'Can change question',9,'change_question'),(27,'Can delete question',9,'delete_question'),(28,'Can add test',10,'add_test'),(29,'Can change test',10,'change_test'),(30,'Can delete test',10,'delete_test'),(31,'Can add test paper',11,'add_testpaper'),(32,'Can change test paper',11,'change_testpaper'),(33,'Can delete test paper',11,'delete_testpaper'),(34,'Can add test paper_ question',12,'add_testpaper_question'),(35,'Can change test paper_ question',12,'change_testpaper_question'),(36,'Can delete test paper_ question',12,'delete_testpaper_question'),(37,'Can add disease',13,'add_disease'),(38,'Can change disease',13,'change_disease'),(39,'Can delete disease',13,'delete_disease'),(40,'Can add disease example',14,'add_diseaseexample'),(41,'Can change disease example',14,'change_diseaseexample'),(42,'Can delete disease example',14,'delete_diseaseexample'),(43,'Can add general process',15,'add_generalprocess'),(44,'Can change general process',15,'change_generalprocess'),(45,'Can delete general process',15,'delete_generalprocess'),(46,'Can add process',16,'add_process'),(47,'Can change process',16,'change_process'),(48,'Can delete process',16,'delete_process'),(49,'Can add sub disease',17,'add_subdisease'),(50,'Can change sub disease',17,'change_subdisease'),(51,'Can delete sub disease',17,'delete_subdisease'),(52,'Can add log entry',18,'add_logentry'),(53,'Can change log entry',18,'change_logentry'),(54,'Can delete log entry',18,'delete_logentry'),(55,'Can add permission',19,'add_permission'),(56,'Can change permission',19,'change_permission'),(57,'Can delete permission',19,'delete_permission'),(58,'Can add group',20,'add_group'),(59,'Can change group',20,'change_group'),(60,'Can delete group',20,'delete_group'),(61,'Can add user',21,'add_user'),(62,'Can change user',21,'change_user'),(63,'Can delete user',21,'delete_user'),(64,'Can add content type',22,'add_contenttype'),(65,'Can change content type',22,'change_contenttype'),(66,'Can delete content type',22,'delete_contenttype'),(67,'Can add session',23,'add_session'),(68,'Can change session',23,'change_session'),(69,'Can delete session',23,'delete_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$A4esXVE1VDXN$DaHdyZoqq3avLBJl4B1whGP++iksNI8GloTHEh9CZPk=','2018-03-15 06:29:35.015583',1,'admin','','','',1,1,'2018-03-15 06:24:09.386760');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disease_disease`
--

DROP TABLE IF EXISTS `disease_disease`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_disease` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease_disease`
--

LOCK TABLES `disease_disease` WRITE;
/*!40000 ALTER TABLE `disease_disease` DISABLE KEYS */;
INSERT INTO `disease_disease` VALUES (1,'传染病'),(2,'寄生虫病'),(3,'内科'),(4,'外产科疾病'),(5,'常用手术'),(6,'免疫');
/*!40000 ALTER TABLE `disease_disease` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disease_diseaseexample`
--

DROP TABLE IF EXISTS `disease_diseaseexample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_diseaseexample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `sub_disease_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Disease_diseaseexamp_sub_disease_id_f3575f8e_fk_Disease_s` (`sub_disease_id`),
  CONSTRAINT `Disease_diseaseexamp_sub_disease_id_f3575f8e_fk_Disease_s` FOREIGN KEY (`sub_disease_id`) REFERENCES `disease_subdisease` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease_diseaseexample`
--

LOCK TABLES `disease_diseaseexample` WRITE;
/*!40000 ALTER TABLE `disease_diseaseexample` DISABLE KEYS */;
/*!40000 ALTER TABLE `disease_diseaseexample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disease_generalprocess`
--

DROP TABLE IF EXISTS `disease_generalprocess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_generalprocess` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `sub_disease_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Disease_generalproce_sub_disease_id_3bec997e_fk_Disease_s` (`sub_disease_id`),
  CONSTRAINT `Disease_generalproce_sub_disease_id_3bec997e_fk_Disease_s` FOREIGN KEY (`sub_disease_id`) REFERENCES `disease_subdisease` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease_generalprocess`
--

LOCK TABLES `disease_generalprocess` WRITE;
/*!40000 ALTER TABLE `disease_generalprocess` DISABLE KEYS */;
/*!40000 ALTER TABLE `disease_generalprocess` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disease_process`
--

DROP TABLE IF EXISTS `disease_process`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_process` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `pic_url` varchar(500) NOT NULL,
  `video_url` varchar(500) NOT NULL,
  `disease_example_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Disease_process_disease_example_id_6dd95e41_fk_Disease_d` (`disease_example_id`),
  CONSTRAINT `Disease_process_disease_example_id_6dd95e41_fk_Disease_d` FOREIGN KEY (`disease_example_id`) REFERENCES `disease_diseaseexample` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease_process`
--

LOCK TABLES `disease_process` WRITE;
/*!40000 ALTER TABLE `disease_process` DISABLE KEYS */;
/*!40000 ALTER TABLE `disease_process` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `disease_subdisease` VALUES (1,'犬瘟热','犬瘟热是由犬瘟热病毒引起的一种高度接触性传染病，传染性极强，死亡率可高达80%以上。','img/sub_diseases/distemper.jpg',1),(2,'犬细小病毒','犬细小病毒病是犬的一种具有高度接触性传染的烈性传染病，该病症于1977年由Eugster发现，临床上以急性出血性肠炎和心肌炎为特征。','img/sub_diseases/parvovirus.jpg',1),(3,'犬传染性肝炎','犬传染性肝炎主要发生在1岁以内的幼犬，成年犬很少发生且多为隐性感染，即使发病也多能耐过。','img/sub_diseases/HCC.jpg',1),(4,'犬冠状病毒','犬冠状病毒一年四季均可发生，以冬季多发，病犬是主要的传染原，犬可通过呼吸道、消化道、粪便及污染物传染。该病一但发生，同窝犬同室犬很难控制均可造成感染。','img/sub_diseases/CVV.jpg',1),(5,'猫泛白细胞减少症','猫泛白细胞减少症，又称猫瘟热，猫传染性肠炎，是猫的一种急性高度接触性传染病。','img/sub_diseases/panleukopenia.jpg',1),(6,'猫病毒性病气管炎','猫病毒性病气管炎是猫的上部呼吸道感染性非常强的一种急性传染病,又称为传染性鼻气管炎。','img/sub_diseases/tracheitis.jpg',1),(7,'皮肤真菌感染','皮肤真菌病的传播主要是通过动物间的互相接触，或通过污染的物体而传播。在宠物数量较多且较密集的情况下，也可通过空气传播。','img/sub_diseases/fungal.jpg',1),(8,'蛔虫病','蛔虫病','',2),(9,'钩虫病','钩虫病','',2),(10,'绦虫病','绦虫病','',2),(11,'球虫病','球虫病','',2),(12,'疥螨虫病','疥螨虫病','',2),(13,'蚤病','蚤病','',2),(14,'口炎','口炎','',3),(15,'肠炎','肠炎','',3),(16,'肠便秘','肠便秘','',3),(17,'胰腺炎','胰腺炎','',3),(18,'肝炎','肝炎','',3),(19,'腹膜炎','腹膜炎','',3),(20,'肛门腺炎','肛门腺炎','',3),(21,'感冒','感冒','',3),(22,'鼻炎','鼻炎','',3),(23,'气管支气管炎','气管支气管炎','',3),(24,'肺炎','肺炎','',3),(25,'心力衰竭','心力衰竭','',3),(26,'尿道感染','尿道感染','',3),(27,'尿结石','尿结石','',3),(28,'膀胱炎','膀胱炎','',3),(29,'肾炎','肾炎','',3),(30,'佝偻病','佝偻病','',3),(31,'有机磷中毒','有机磷中毒','',3),(32,'糖尿病','糖尿病','',3),(33,'耳血肿','耳血肿','',3),(34,'中耳炎','中耳炎','',3),(35,'眼睑内翻','眼睑内翻','',3),(36,'结膜炎','结膜炎','',3),(37,'角膜炎','角膜炎','',3),(38,'外伤','外伤','',4),(39,'外科感染','外科感染','',4),(40,'骨折','骨折','',4),(41,'关节脱位','关节脱位','',4),(42,'湿疹','湿疹','',4),(43,'皮炎','皮炎','',4),(44,'脓皮病','脓皮病','',4),(45,'脱毛症','脱毛症','',4),(46,'趾间囊肿','趾间囊肿','',4),(47,'疝','疝','',4),(48,'阴道炎','阴道炎','',4),(49,'阴道脱出','阴道脱出','',4),(50,'子宫蓄脓','子宫蓄脓','',4),(51,'难产','难产','',4),(52,'乳房炎','乳房炎','',4),(53,'绝育','绝育','',5),(54,'剖腹产','剖腹产','',5),(55,'瞬膜腺增生物切除','瞬膜腺增生物切除','',5),(56,'眼球摘除','眼球摘除','',5),(57,'立耳术','立耳术','',5),(58,'断尾术','断尾术','',5),(59,'犬免疫程序','犬免疫程序','',6),(60,'猫免疫程序','猫免疫程序','',6);
/*!40000 ALTER TABLE `disease_subdisease` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-03-15 06:32:49.213437','1','admin1@example.com',1,'[{\"added\": {}}]',4,1),(2,'2018-03-15 06:33:18.200550','2','admin2.example.cpm',1,'[{\"added\": {}}]',4,1),(3,'2018-03-15 06:33:20.259953','2','admin2.example.cpm',2,'[]',4,1),(4,'2018-03-15 06:33:45.580458','3','admin3.example.com',1,'[{\"added\": {}}]',4,1),(5,'2018-03-15 06:35:02.904022','4','intern1.test.com',1,'[{\"added\": {}}]',4,1),(6,'2018-03-15 06:35:31.946378','5','intern2@test.com',1,'[{\"added\": {}}]',4,1),(7,'2018-03-15 06:35:41.508324','4','intern1@test.com',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,1),(8,'2018-03-15 06:36:00.864271','2','admin2@example.cpm',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,1),(9,'2018-03-15 06:36:07.366569','3','admin3@example.com',2,'[{\"changed\": {\"fields\": [\"email\"]}}]',4,1),(10,'2018-03-15 06:40:05.185173','1','传染病',1,'[{\"added\": {}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u761f\\u70ed\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u7ec6\\u5c0f\\u75c5\\u6bd2\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u4f20\\u67d3\\u6027\\u809d\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u51a0\\u72b6\\u75c5\\u6bd2\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u732b\\u6cdb\\u767d\\u7ec6\\u80de\\u51cf\\u5c11\\u75c7\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u732b\\u75c5\\u6bd2\\u6027\\u75c5\\u6c14\\u7ba1\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u76ae\\u80a4\\u771f\\u83cc\\u611f\\u67d3\"}}]',13,1),(11,'2018-03-15 06:40:08.853849','1','传染病',2,'[]',13,1),(12,'2018-03-15 06:40:57.515916','2','寄生虫病',1,'[{\"added\": {}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u86d4\\u866b\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u94a9\\u866b\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u7ee6\\u866b\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u7403\\u866b\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u75a5\\u87a8\\u866b\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u86a4\\u75c5\"}}]',13,1),(13,'2018-03-15 06:43:58.973005','3','内科',1,'[{\"added\": {}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u53e3\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u80a0\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u80a0\\u4fbf\\u79d8\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u80f0\\u817a\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u809d\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u8179\\u819c\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u809b\\u95e8\\u817a\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u611f\\u5192\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u9f3b\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u6c14\\u7ba1\\u652f\\u6c14\\u7ba1\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u80ba\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5fc3\\u529b\\u8870\\u7aed\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5c3f\\u9053\\u611f\\u67d3\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5c3f\\u7ed3\\u77f3\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u8180\\u80f1\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u80be\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u4f5d\\u507b\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u6709\\u673a\\u78f7\\u4e2d\\u6bd2\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u7cd6\\u5c3f\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u8033\\u8840\\u80bf\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u4e2d\\u8033\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u773c\\u7751\\u5185\\u7ffb\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u7ed3\\u819c\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u89d2\\u819c\\u708e\"}}]',13,1),(14,'2018-03-15 06:45:52.761634','4','外产科疾病',1,'[{\"added\": {}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5916\\u4f24\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5916\\u79d1\\u611f\\u67d3\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u9aa8\\u6298\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5173\\u8282\\u8131\\u4f4d\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u6e7f\\u75b9\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u76ae\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u8113\\u76ae\\u75c5\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u8131\\u6bdb\\u75c7\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u8dbe\\u95f4\\u56ca\\u80bf\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u759d\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u9634\\u9053\\u708e\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u9634\\u9053\\u8131\\u51fa\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5b50\\u5bab\\u84c4\\u8113\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u96be\\u4ea7\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u4e73\\u623f\\u708e\"}}]',13,1),(15,'2018-03-15 06:46:35.074131','5','常用手术',1,'[{\"added\": {}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u7edd\\u80b2\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u5256\\u8179\\u4ea7\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u77ac\\u819c\\u817a\\u589e\\u751f\\u7269\\u5207\\u9664\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u773c\\u7403\\u6458\\u9664\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u7acb\\u8033\\u672f\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u65ad\\u5c3e\\u672f\"}}]',13,1),(16,'2018-03-15 06:47:07.000479','6','免疫',1,'[{\"added\": {}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u514d\\u75ab\\u7a0b\\u5e8f\"}}, {\"added\": {\"name\": \"sub disease\", \"object\": \"\\u732b\\u514d\\u75ab\\u7a0b\\u5e8f\"}}]',13,1),(17,'2018-03-15 06:54:02.847804','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u761f\\u70ed\", \"fields\": [\"pic_url\"]}}]',13,1),(18,'2018-03-15 06:55:15.742192','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u761f\\u70ed\", \"fields\": [\"desc\"]}}]',13,1),(19,'2018-03-15 07:01:26.036398','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u7ec6\\u5c0f\\u75c5\\u6bd2\", \"fields\": [\"desc\", \"pic_url\"]}}]',13,1),(20,'2018-03-15 07:02:40.459655','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u4f20\\u67d3\\u6027\\u809d\\u708e\", \"fields\": [\"desc\", \"pic_url\"]}}]',13,1),(21,'2018-03-15 07:05:29.799882','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u72ac\\u51a0\\u72b6\\u75c5\\u6bd2\", \"fields\": [\"desc\", \"pic_url\"]}}]',13,1),(22,'2018-03-15 07:09:46.862126','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u732b\\u6cdb\\u767d\\u7ec6\\u80de\\u51cf\\u5c11\\u75c7\", \"fields\": [\"desc\", \"pic_url\"]}}]',13,1),(23,'2018-03-15 07:12:14.637156','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u732b\\u75c5\\u6bd2\\u6027\\u75c5\\u6c14\\u7ba1\\u708e\", \"fields\": [\"desc\", \"pic_url\"]}}]',13,1),(24,'2018-03-15 07:14:57.504992','1','传染病',2,'[{\"changed\": {\"name\": \"sub disease\", \"object\": \"\\u76ae\\u80a4\\u771f\\u83cc\\u611f\\u67d3\", \"fields\": [\"desc\", \"pic_url\"]}}]',13,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (18,'admin','logentry'),(20,'auth','group'),(19,'auth','permission'),(21,'auth','user'),(22,'contenttypes','contenttype'),(13,'Disease','disease'),(14,'Disease','diseaseexample'),(15,'Disease','generalprocess'),(16,'Disease','process'),(17,'Disease','subdisease'),(1,'Navigation','role'),(2,'Navigation','room'),(3,'Navigation','room_role'),(23,'sessions','session'),(8,'Test','choice'),(9,'Test','question'),(10,'Test','test'),(11,'Test','testpaper'),(12,'Test','testpaper_question'),(4,'User','user'),(6,'User','usertest'),(7,'User','usertest_question'),(5,'User','user_test');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Disease','0001_initial','2018-03-15 06:10:48.269174'),(2,'Navigation','0001_initial','2018-03-15 06:10:48.581675'),(3,'Test','0001_initial','2018-03-15 06:10:49.668855'),(4,'User','0001_initial','2018-03-15 06:10:50.435548'),(5,'contenttypes','0001_initial','2018-03-15 06:10:50.498088'),(6,'auth','0001_initial','2018-03-15 06:10:51.592260'),(7,'admin','0001_initial','2018-03-15 06:10:51.857914'),(8,'admin','0002_logentry_remove_auto_add','2018-03-15 06:10:51.857914'),(9,'contenttypes','0002_remove_content_type_name','2018-03-15 06:10:52.029807'),(10,'auth','0002_alter_permission_name_max_length','2018-03-15 06:10:52.129416'),(11,'auth','0003_alter_user_email_max_length','2018-03-15 06:10:52.223178'),(12,'auth','0004_alter_user_username_opts','2018-03-15 06:10:52.238838'),(13,'auth','0005_alter_user_last_login_null','2018-03-15 06:10:52.332565'),(14,'auth','0006_require_contenttypes_0002','2018-03-15 06:10:52.332565'),(15,'auth','0007_alter_validators_add_error_messages','2018-03-15 06:10:52.348236'),(16,'auth','0008_alter_user_username_max_length','2018-03-15 06:10:52.551380'),(17,'auth','0009_alter_user_last_name_max_length','2018-03-15 06:10:52.629471'),(18,'sessions','0001_initial','2018-03-15 06:10:52.707604');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('xnd0rr1zyruzsyme7rktolihb8v012cc','MjdiNDNjODdiODRkMDkyN2RhZDk2ZmI2ZDJhZmU0Yjc5MTkyMGNiZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MjUxNDNhZWE4NzhmYmM2NzhhOGQyOGU0NjU0ZGNmMDFmNTA5OWNjIn0=','2018-03-29 06:29:35.019596');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `navigation_role`
--

DROP TABLE IF EXISTS `navigation_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `navigation_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `navigation_role`
--

LOCK TABLES `navigation_role` WRITE;
/*!40000 ALTER TABLE `navigation_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `navigation_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `navigation_room`
--

DROP TABLE IF EXISTS `navigation_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `navigation_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `pic_url` varchar(500) NOT NULL,
  `video_url` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `navigation_room`
--

LOCK TABLES `navigation_room` WRITE;
/*!40000 ALTER TABLE `navigation_room` DISABLE KEYS */;
/*!40000 ALTER TABLE `navigation_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `navigation_room_role`
--

DROP TABLE IF EXISTS `navigation_room_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `navigation_room_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `room_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Navigation_room_role_role_id_00333d8d_fk_Navigation_role_id` (`role_id`),
  KEY `Navigation_room_role_room_id_b83cf8b1_fk_Navigation_room_id` (`room_id`),
  CONSTRAINT `Navigation_room_role_role_id_00333d8d_fk_Navigation_role_id` FOREIGN KEY (`role_id`) REFERENCES `navigation_role` (`id`),
  CONSTRAINT `Navigation_room_role_room_id_b83cf8b1_fk_Navigation_room_id` FOREIGN KEY (`room_id`) REFERENCES `navigation_room` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `navigation_room_role`
--

LOCK TABLES `navigation_room_role` WRITE;
/*!40000 ALTER TABLE `navigation_room_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `navigation_room_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_choice`
--

DROP TABLE IF EXISTS `test_choice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(100) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Test_choice_question_id_93a1b026_fk_Test_question_id` (`question_id`),
  CONSTRAINT `Test_choice_question_id_93a1b026_fk_Test_question_id` FOREIGN KEY (`question_id`) REFERENCES `test_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_choice`
--

LOCK TABLES `test_choice` WRITE;
/*!40000 ALTER TABLE `test_choice` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_choice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_question`
--

DROP TABLE IF EXISTS `test_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(1000) NOT NULL,
  `score` int(11) NOT NULL,
  `sub_disease_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Test_question_sub_disease_id_8ec4d7d5_fk_Disease_subdisease_id` (`sub_disease_id`),
  CONSTRAINT `Test_question_sub_disease_id_8ec4d7d5_fk_Disease_subdisease_id` FOREIGN KEY (`sub_disease_id`) REFERENCES `disease_subdisease` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_question`
--

LOCK TABLES `test_question` WRITE;
/*!40000 ALTER TABLE `test_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_test`
--

DROP TABLE IF EXISTS `test_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `duration` int(11) NOT NULL,
  `close_time` datetime(6) NOT NULL,
  `test_paper_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Test_test_test_paper_id_c21e05f1_fk_Test_testpaper_id` (`test_paper_id`),
  CONSTRAINT `Test_test_test_paper_id_c21e05f1_fk_Test_testpaper_id` FOREIGN KEY (`test_paper_id`) REFERENCES `test_testpaper` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_test`
--

LOCK TABLES `test_test` WRITE;
/*!40000 ALTER TABLE `test_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_testpaper`
--

DROP TABLE IF EXISTS `test_testpaper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_testpaper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `disease_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Test_testpaper_disease_id_e89b3eee_fk_Disease_disease_id` (`disease_id`),
  CONSTRAINT `Test_testpaper_disease_id_e89b3eee_fk_Disease_disease_id` FOREIGN KEY (`disease_id`) REFERENCES `disease_disease` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_testpaper`
--

LOCK TABLES `test_testpaper` WRITE;
/*!40000 ALTER TABLE `test_testpaper` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_testpaper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_testpaper_question`
--

DROP TABLE IF EXISTS `test_testpaper_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_testpaper_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `testpaper_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Test_testpaper_question_question_id_519358f5_fk_Test_question_id` (`question_id`),
  KEY `Test_testpaper_quest_testpaper_id_0bed4fe5_fk_Test_test` (`testpaper_id`),
  CONSTRAINT `Test_testpaper_quest_testpaper_id_0bed4fe5_fk_Test_test` FOREIGN KEY (`testpaper_id`) REFERENCES `test_testpaper` (`id`),
  CONSTRAINT `Test_testpaper_question_question_id_519358f5_fk_Test_question_id` FOREIGN KEY (`question_id`) REFERENCES `test_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_testpaper_question`
--

LOCK TABLES `test_testpaper_question` WRITE;
/*!40000 ALTER TABLE `test_testpaper_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_testpaper_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user`
--

DROP TABLE IF EXISTS `user_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(16) NOT NULL,
  `name` varchar(30) NOT NULL,
  `authority` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user`
--

LOCK TABLES `user_user` WRITE;
/*!40000 ALTER TABLE `user_user` DISABLE KEYS */;
INSERT INTO `user_user` VALUES (1,'admin1@example.com','admin1','admin1',1),(2,'admin2@example.cpm','admin2','admin2',1),(3,'admin3@example.com','admin3','admin3',1),(4,'intern1@test.com','intern1','intern1',0),(5,'intern2@test.com','intern2','intern2',0);
/*!40000 ALTER TABLE `user_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user_test`
--

DROP TABLE IF EXISTS `user_user_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `User_user_test_test_id_87548491_fk_Test_test_id` (`test_id`),
  KEY `User_user_test_user_id_5045dd59_fk_User_user_id` (`user_id`),
  CONSTRAINT `User_user_test_test_id_87548491_fk_Test_test_id` FOREIGN KEY (`test_id`) REFERENCES `test_test` (`id`),
  CONSTRAINT `User_user_test_user_id_5045dd59_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_test`
--

LOCK TABLES `user_user_test` WRITE;
/*!40000 ALTER TABLE `user_user_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_user_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_usertest`
--

DROP TABLE IF EXISTS `user_usertest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_usertest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `User_usertest_test_id_263c7926_fk_Test_test_id` (`test_id`),
  KEY `User_usertest_user_id_0c119812_fk_User_user_id` (`user_id`),
  CONSTRAINT `User_usertest_test_id_263c7926_fk_Test_test_id` FOREIGN KEY (`test_id`) REFERENCES `test_test` (`id`),
  CONSTRAINT `User_usertest_user_id_0c119812_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usertest`
--

LOCK TABLES `user_usertest` WRITE;
/*!40000 ALTER TABLE `user_usertest` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_usertest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_usertest_question`
--

DROP TABLE IF EXISTS `user_usertest_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_usertest_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `usertest_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `User_usertest_question_question_id_66685bea_fk_Test_question_id` (`question_id`),
  KEY `User_usertest_question_usertest_id_64803da1_fk_User_usertest_id` (`usertest_id`),
  CONSTRAINT `User_usertest_question_question_id_66685bea_fk_Test_question_id` FOREIGN KEY (`question_id`) REFERENCES `test_question` (`id`),
  CONSTRAINT `User_usertest_question_usertest_id_64803da1_fk_User_usertest_id` FOREIGN KEY (`usertest_id`) REFERENCES `user_usertest` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usertest_question`
--

LOCK TABLES `user_usertest_question` WRITE;
/*!40000 ALTER TABLE `user_usertest_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_usertest_question` ENABLE KEYS */;
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

-- Dump completed on 2018-03-15 15:52:47
