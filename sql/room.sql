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
-- Table structure for table `navigation_room`
--

DROP TABLE IF EXISTS `navigation_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `navigation_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `desc` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  `pic_url` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `video_url` varchar(1000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `navigation_room`
--

LOCK TABLES `navigation_room` WRITE;
/*!40000 ALTER TABLE `navigation_room` DISABLE KEYS */;
INSERT INTO `navigation_room` VALUES (1,'前台','包括接待挂号、导医咨询、病历档案发出与回收、收费等。','',''),(2,'档案室','包括病例档案的合理保存与数据统计等。','',''),(3,'免疫室','包括为健康宠物接种疫苗的流程，对常见并发症的处理流程，对常见免疫相关问题的解答等。','',''),(4,'化验室','包括对送检样本的预处理，对相应样本进行血常规、血液生化、电解质、血气、血凝指标、激素指标、尿常规、微生物学检查、药敏、皮肤刮片、粪便检查、传染病检查等检查操作流程。','',''),(5,'影像室','包括X线检查、B超检查以及CT、MRI检查。如X线检查：X光机的结构功能介绍、全身各部位的摆位、拍摄条件的选择、拍摄流程、洗片的操作流程。B超检查：扫查探头的选择、全身各个部位扫查的摆位、腹部扫查流程。','',''),(6,'专科检查室','包括对眼科、骨科、神经科、心脏科等专科疾病的检查，如眼科（检眼镜检查、眼压检查、裂隙灯检查、眼底检查、泪液分泌量检查等）、心脏科检查（心脏听诊、心电图检查等）、神经学检查（步态检查、各种反射检查等）等。','',''),(7,'处置室','包括口服投药、换药、清洗耳道、挤肛门腺、修剪指甲、鼻饲管放置、灌肠、安乐死等基本处置操作流程。','',''),(8,'药房','包括对各种药物的存放要求、处方的审核流程、药物的发放流程、常见药物的使用说明等。','',''),(9,'注射室','包括静脉注射、皮下注射、肌肉注射、局部封闭注射的操作流程，常见问题的处理方法，输液泵、加热垫的使用方法，注射室的消毒流程。','',''),(10,'手术准备室','包括术前对宠物进行麻前给药、注射麻醉、吸入麻醉的流程，保定、剃毛、消毒的流程，常见手术器械的介绍，手术器械包的准备、灭菌流程，手术人员的消毒、穿戴手术衣流程等。','',''),(11,'手术室','包括手术室的布局介绍，手术室消毒流程，手术无菌要求，常规手术、特殊手等的操作规范。','',''),(12,'住院部','包括对需要住院的病例进行护理分级，不同护理级别的要求，住院部的工作流程，住院部的消毒流程等。','',''),(13,'病理剖检室','包括对病死动物剖解的流程，病理剖检室的消毒流程，病历剖检过程的人员要求，病理剖检过程中的人道关怀。','','');
/*!40000 ALTER TABLE `navigation_room` ENABLE KEYS */;
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

-- Dump completed on 2018-03-23  0:26:52
