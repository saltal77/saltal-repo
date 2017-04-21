CREATE DATABASE  IF NOT EXISTS `salon_saltal` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
USE `salon_saltal`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win32 (AMD64)
--
-- Host: localhost    Database: salon_saltal
-- ------------------------------------------------------
-- Server version	5.7.17-log

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
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car` (
  `id_car` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `color` varchar(128) COLLATE utf8_bin NOT NULL,
  `model` varchar(128) COLLATE utf8_bin NOT NULL,
  `a_type` varchar(128) COLLATE utf8_bin NOT NULL,
  `power` int(11) NOT NULL,
  `fuel` varchar(128) COLLATE utf8_bin NOT NULL,
  `country` varchar(128) COLLATE utf8_bin NOT NULL,
  `price` int(11) NOT NULL,
  `buyed` int(11) NOT NULL,
  PRIMARY KEY (`id_car`),
  KEY `buyed_idx` (`buyed`),
  CONSTRAINT `id_buyer` FOREIGN KEY (`buyed`) REFERENCES `client` (`id_client`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,2005,'серый','Opel','универсал',95,'бензин','Германия',100,1),(2,1998,'золотой','KIA','седан',105,'бензин','Корея',95,2),(3,1999,'синий','Mitsubishi','седан',90,'бензин','Япония',110,6),(4,2010,'фиолетовый','Renault','седан',110,'бензин','Франция',180,1),(6,2002,'красный','Seat','хетчбэк',85,'бензин','Испания',80,5),(8,2013,'желтый','Fiat','седан',110,'бензин','Италия',270,4),(10,2014,'серебряный','Mazda','седан',105,'бензин','Япония',300,1),(11,2010,'белый','Citroen','седан',100,'бензин','Франция',190,1);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `id_client` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) COLLATE utf8_bin NOT NULL,
  `adress` varchar(256) COLLATE utf8_bin NOT NULL,
  `tel` varchar(128) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id_client`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'нет Имени','нет Адреса','нет Телефона'),(2,'Николай Кузнецов','Москва, Проспект Мира 113 -67 ','+7-812-558-9636'),(4,'Александр Перепелкин','Москва, ул. Масловка 22 - 88',' +7-495-277-9885'),(5,'Александр Востриков','Москва, ул. Нагорная 11 - 12',' +7-495-276-7785'),(6,'Валентин Попов','Москва, ул. Светлая 21 - 62',' +7-499-279-9975'),(7,'Дмитрий Павлов','Москва, ул. Осенняя 34 - 42',' +7-495-276-6675');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lorry`
--

DROP TABLE IF EXISTS `lorry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lorry` (
  `id_lorry` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `color` varchar(128) COLLATE utf8_bin NOT NULL,
  `model` varchar(128) CHARACTER SET utf8 NOT NULL,
  `a_type` varchar(128) COLLATE utf8_bin NOT NULL,
  `power` int(11) NOT NULL,
  `fuel` varchar(128) COLLATE utf8_bin NOT NULL,
  `country` varchar(128) COLLATE utf8_bin NOT NULL,
  `price` int(11) NOT NULL,
  `buyed` int(11) NOT NULL,
  `cargo` float NOT NULL,
  PRIMARY KEY (`id_lorry`),
  KEY `id_buyer_idx` (`buyed`),
  CONSTRAINT `id_buyer1` FOREIGN KEY (`buyed`) REFERENCES `client` (`id_client`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lorry`
--

LOCK TABLES `lorry` WRITE;
/*!40000 ALTER TABLE `lorry` DISABLE KEYS */;
INSERT INTO `lorry` VALUES (1,2008,'оранжевый','DAF','грузовик',400,'дизель','Германия',800,4,12.5),(2,2010,'белый','Камаз','грузовик',500,'дизель','Россия',950,1,13),(3,2008,'зеленый','Mersedes','грузовик',550,'дизель','Германия',990,1,14),(5,2008,'синий','Mersedes','грузовик',650,'дизель','Германия',1090,7,15),(6,2009,'коричневый','MAN','грузовик',550,'дизель','Германия',890,5,13),(7,2007,'синий','Renault','грузовик',400,'бензин','Францияия',600,1,11);
/*!40000 ALTER TABLE `lorry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'salon_saltal'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-19 13:47:28
