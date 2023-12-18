CREATE DATABASE  IF NOT EXISTS `crud` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `crud`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: crud
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `ssn` bigint NOT NULL,
  `contract_date` date NOT NULL,
  `age` int NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `phone_UNIQUE` (`phone`),
  UNIQUE KEY `ssn_UNIQUE` (`ssn`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'omer','01013767684','38B, hamed abd elazem, el-haram',12345678912345,'2023-12-30',23,'omarhany2k@gmail.com'),(2,'amer','01234567991','38B, hamed abd elazem, el haram',12346675912345,'2023-12-31',24,'omarh2ny3k@gmail.com'),(4,'omar','01013787684','38B, hamed abd el-azem, giza, egypt.',12345666669874,'2023-12-31',23,'omaromar@gmail.com'),(8,'tmim','01013676784','7, khzoet al khandk, Giza, Egypt.',30002156987456,'2021-10-15',24,'tamim@gmail.com'),(9,'ahmad','01022553322','38B, Hamed Abd ELazem, Giza, Egypt.',33225544778811,'2020-06-12',26,'ahmed@gmail.com'),(10,'Medhat','01535546669','12B, El-Moez, Cairo, Egypt.',20508040206050,'2023-12-31',23,'MedhatMeto200@yahoo.com'),(11,'Mamdouh Amar','01214141516','20, Makka, Giza, Egypt.',30356654789512,'2015-06-12',33,'Mamdouh@hotmail.com'),(13,'mazen','01227537152','38B, Hamed, a, Egypt.',11023654011223,'2023-12-02',23,'mazen@gmail.com'),(14,'Momen','01123690205','23, El-Eshreen, Fisal, Giza, Egypt.',30002506014025,'2016-12-31',26,'momengamal@gmail.com'),(15,'Mohamed','01225402501','13B, Elmsaken, Fisal, giza, Egypt.',30001548952156,'2020-12-02',26,'mohamed@gmail.com');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-18 19:04:00
