-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `OlympicOccurrence`
--

DROP TABLE IF EXISTS `OlympicOccurrence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `OlympicOccurrence` (
  `id` int NOT NULL,
  `winning_country` int DEFAULT NULL,
  `host_countries` varchar(255) DEFAULT NULL,
  `year` int NOT NULL,
  `season_participated` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OlympicOccurrence`
--

LOCK TABLES `OlympicOccurrence` WRITE;
/*!40000 ALTER TABLE `OlympicOccurrence` DISABLE KEYS */;
INSERT INTO `OlympicOccurrence` VALUES (1,123,'USA, Canada',2020,'Summer'),(2,456,'Brazil',2016,'Winter'),(3,456,'China',2024,'Summer'),(4,321,'Russia',2018,'Winter'),(5,654,'France, Germany',2022,'Winter');
/*!40000 ALTER TABLE `OlympicOccurrence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `athlete`
--

DROP TABLE IF EXISTS `athlete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `athlete` (
  `athlete_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(255) NOT NULL,
  `country_id` int NOT NULL,
  `height` int NOT NULL,
  `weight` int NOT NULL,
  `cid` int NOT NULL,
  `sid` int NOT NULL,
  PRIMARY KEY (`athlete_id`),
  KEY `cid` (`cid`),
  KEY `sid` (`sid`),
  CONSTRAINT `athlete_ibfk_1` FOREIGN KEY (`cid`) REFERENCES `coach` (`COACH_ID`),
  CONSTRAINT `athlete_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `sports` (`sport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `athlete`
--

LOCK TABLES `athlete` WRITE;
/*!40000 ALTER TABLE `athlete` DISABLE KEYS */;
INSERT INTO `athlete` VALUES (6,'John Doe','1990-05-15','Male',1,180,75,101,1),(7,'Jasmith','1999-02-22','Female',2,155,56,102,2),(8,'Robert Johnson','1992-03-10','Male',3,175,70,103,3),(9,'Emily White','1995-11-25','Female',4,160,55,104,4),(10,'Michael Brown','1985-07-18','Male',5,185,80,105,1);
/*!40000 ALTER TABLE `athlete` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `athlete_medals`
--

DROP TABLE IF EXISTS `athlete_medals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `athlete_medals` (
  `A_ID` int NOT NULL,
  `O_ID` int NOT NULL,
  `Medals_Received` int NOT NULL,
  KEY `A_ID` (`A_ID`),
  KEY `O_ID` (`O_ID`),
  CONSTRAINT `athlete_medals_ibfk_1` FOREIGN KEY (`A_ID`) REFERENCES `athlete` (`athlete_id`),
  CONSTRAINT `athlete_medals_ibfk_2` FOREIGN KEY (`O_ID`) REFERENCES `OlympicOccurrence` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `athlete_medals`
--

LOCK TABLES `athlete_medals` WRITE;
/*!40000 ALTER TABLE `athlete_medals` DISABLE KEYS */;
INSERT INTO `athlete_medals` VALUES (6,3,1),(7,3,2),(8,4,3),(9,4,1),(10,5,1);
/*!40000 ALTER TABLE `athlete_medals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coach`
--

DROP TABLE IF EXISTS `coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coach` (
  `COACH_ID` int NOT NULL,
  `NAME` varchar(255) NOT NULL,
  `GENDER` varchar(255) NOT NULL,
  `EXPERTISE_IN` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`COACH_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coach`
--

LOCK TABLES `coach` WRITE;
/*!40000 ALTER TABLE `coach` DISABLE KEYS */;
INSERT INTO `coach` VALUES (101,'Coach Smith','Male','Swimming'),(102,'Coach Johnson','Female','Gymnastics'),(103,'Coach Brown','Male','Skiing'),(104,'Coach Williams','Female','Basketball'),(105,'Coach Davis','Male','Athletics'),(106,'Coach Garcia','Female','Volleyball'),(107,'Coach Martinez','Male','Weightlifting'),(108,'Coach Taylor','Female','Tennis'),(109,'Coach Robinson','Male','Cycling');
/*!40000 ALTER TABLE `coach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `country_code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`country_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES ('10','Germany'),('11','India'),('12','Nepal'),('13','tibet'),('15','srilanka'),('16','italy'),('17','Russia'),('18','Afghanisthan'),('2','Canada'),('20','Korea'),('4','China'),('5','Russia'),('6','Australia'),('7','France'),('8','Japan'),('9','Italy');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ranking`
--

DROP TABLE IF EXISTS `ranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ranking` (
  `o_id` int NOT NULL,
  `country_id` int NOT NULL,
  `rank` int NOT NULL,
  KEY `o_id` (`o_id`),
  CONSTRAINT `ranking_ibfk_1` FOREIGN KEY (`o_id`) REFERENCES `OlympicOccurrence` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ranking`
--

LOCK TABLES `ranking` WRITE;
/*!40000 ALTER TABLE `ranking` DISABLE KEYS */;
INSERT INTO `ranking` VALUES (1,6,1),(1,7,2),(1,8,3),(2,6,4),(2,7,1),(2,9,3),(2,10,2),(3,7,3),(3,9,1),(3,8,4),(3,10,2),(4,8,3),(4,9,2),(4,10,1),(5,6,3),(5,7,2),(5,8,1),(5,9,5),(5,10,4);
/*!40000 ALTER TABLE `ranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sports`
--

DROP TABLE IF EXISTS `sports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sports` (
  `sport_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `category` varchar(255) DEFAULT NULL,
  `decision_makers` varchar(255) DEFAULT NULL,
  `record` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sports`
--

LOCK TABLES `sports` WRITE;
/*!40000 ALTER TABLE `sports` DISABLE KEYS */;
INSERT INTO `sports` VALUES (1,'Swimming','Water','Coach Smith','World Record Holder'),(2,'Gymnastics','Indoor','Coach Johnson','Olympic Gold Medalist'),(3,'Skiing','Winter','Coach Brown','National Champion'),(4,'Basketball','Indoor','Coach Williams','NBA All-Star'),(5,'Athletics','Outdoor','Coach Davis','Olympic Record Holder'),(6,'Volleyball','Indoor','Coach Garcia','World Championship Winner'),(7,'Weightlifting','Indoor','Coach Martinez','Olympic Gold Medalist'),(8,'Tennis','Outdoor','Coach Taylor','Grand Slam Winner'),(9,'Cycling','Outdoor','Coach Robinson','Tour de France Winner');
/*!40000 ALTER TABLE `sports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `torch`
--

DROP TABLE IF EXISTS `torch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `torch` (
  `colour` varchar(255) NOT NULL,
  `length` varchar(255) NOT NULL,
  `composition` varchar(255) NOT NULL,
  `fuel` varchar(255) NOT NULL,
  `manufacturer` varchar(255) NOT NULL,
  `o_id` int NOT NULL,
  KEY `o_id` (`o_id`),
  CONSTRAINT `torch_ibfk_1` FOREIGN KEY (`o_id`) REFERENCES `OlympicOccurrence` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `torch`
--

LOCK TABLES `torch` WRITE;
/*!40000 ALTER TABLE `torch` DISABLE KEYS */;
INSERT INTO `torch` VALUES ('Green','Short','Fiber','Electric','LMN Torches',3),('Yellow','Medium','Metal','Gas','OPQ Torches',4),('Purple','Long','Plastic','Kerosene','RST Torches',5),('Blue','Short','Fiber','Electric','XYZ Torches',1),('Red','Medium','Metal','Gas','ABC Torches',2);
/*!40000 ALTER TABLE `torch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tournament_winner`
--

DROP TABLE IF EXISTS `tournament_winner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tournament_winner` (
  `T_ID` int DEFAULT NULL,
  `A_ID` int DEFAULT NULL,
  `result` tinyint(1) NOT NULL,
  KEY `A_ID` (`A_ID`),
  KEY `T_ID` (`T_ID`),
  CONSTRAINT `tournament_winner_ibfk_1` FOREIGN KEY (`A_ID`) REFERENCES `athlete` (`athlete_id`),
  CONSTRAINT `tournament_winner_ibfk_2` FOREIGN KEY (`T_ID`) REFERENCES `tournaments` (`tournament_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tournament_winner`
--

LOCK TABLES `tournament_winner` WRITE;
/*!40000 ALTER TABLE `tournament_winner` DISABLE KEYS */;
INSERT INTO `tournament_winner` VALUES (5,7,1),(6,6,0),(7,8,1),(8,9,0),(9,10,0);
/*!40000 ALTER TABLE `tournament_winner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tournaments`
--

DROP TABLE IF EXISTS `tournaments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tournaments` (
  `tournament_id` int NOT NULL AUTO_INCREMENT,
  `duration` varchar(255) NOT NULL,
  `result` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `S_ID` int DEFAULT NULL,
  `O_ID` int DEFAULT NULL,
  PRIMARY KEY (`tournament_id`),
  KEY `O_ID` (`O_ID`),
  KEY `S_ID` (`S_ID`),
  CONSTRAINT `tournaments_ibfk_1` FOREIGN KEY (`O_ID`) REFERENCES `OlympicOccurrence` (`id`),
  CONSTRAINT `tournaments_ibfk_2` FOREIGN KEY (`S_ID`) REFERENCES `sports` (`sport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tournaments`
--

LOCK TABLES `tournaments` WRITE;
/*!40000 ALTER TABLE `tournaments` DISABLE KEYS */;
INSERT INTO `tournaments` VALUES (5,'2 weeks','Gold Medal Match','2023-01-04',5,3),(6,'3 weeks','Germany Wins','2023-01-05',6,4),(7,'1 week','Australia Wins','2023-01-06',7,5),(8,'10 days','Japan Wins','2016-07-21',8,2),(9,'2 weeks','Italy Wins','2022-12-31',9,1);
/*!40000 ALTER TABLE `tournaments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-03  5:08:55
