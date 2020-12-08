-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: eventbrite
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `categoria_eventos`
--

DROP TABLE IF EXISTS `categoria_eventos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria_eventos` (
  `id` int NOT NULL,
  `nombre_categoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria_eventos`
--

LOCK TABLES `categoria_eventos` WRITE;
/*!40000 ALTER TABLE `categoria_eventos` DISABLE KEYS */;
INSERT INTO `categoria_eventos` VALUES (1,'Party'),(2,'Sports'),(3,'School'),(4,'Work'),(5,'Social');
/*!40000 ALTER TABLE `categoria_eventos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entradas`
--

DROP TABLE IF EXISTS `entradas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entradas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idPedido` int NOT NULL,
  `idEvento` int NOT NULL,
  `estado` varchar(50) NOT NULL,
  `numEntrada` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idPedido_idx` (`idPedido`),
  KEY `idEvento_idx` (`idEvento`),
  CONSTRAINT `idEvento` FOREIGN KEY (`idEvento`) REFERENCES `eventos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `idPedido` FOREIGN KEY (`idPedido`) REFERENCES `pedidos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entradas`
--

LOCK TABLES `entradas` WRITE;
/*!40000 ALTER TABLE `entradas` DISABLE KEYS */;
INSERT INTO `entradas` VALUES (1,35,2,'No canjeado',73),(2,34,2,'No canjeado',73),(3,34,2,'No canjeado',74),(4,47,2,'No canjeado',75),(5,47,2,'No canjeado',76),(6,48,2,'No canjeado',77),(7,48,2,'No canjeado',78),(8,49,2,'No canjeado',79),(9,49,2,'No canjeado',80),(10,50,2,'No canjeado',81),(11,50,2,'No canjeado',82),(12,50,2,'No canjeado',83),(13,50,2,'No canjeado',84),(14,50,2,'No canjeado',85),(15,52,2,'No canjeado',86),(16,52,2,'No canjeado',87),(17,52,2,'No canjeado',88),(18,52,2,'No canjeado',89),(19,52,2,'No canjeado',90),(23,54,2,'No canjeado',91),(24,54,2,'No canjeado',92),(25,54,2,'No canjeado',93),(26,54,2,'No canjeado',94),(27,54,2,'No canjeado',95),(28,56,2,'No canjeado',96),(29,57,7,'No canjeado',1),(30,57,7,'No canjeado',2),(31,58,7,'No canjeado',3),(32,58,7,'No canjeado',4),(33,58,7,'No canjeado',5);
/*!40000 ALTER TABLE `entradas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventos`
--

DROP TABLE IF EXISTS `eventos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `valorEntrada` double NOT NULL,
  `capacidad` int NOT NULL,
  `disponibilidad` int NOT NULL,
  `pais` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `idCategoria` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idUsuario_idx` (`idUsuario`),
  KEY `idCategoria_idx` (`idCategoria`),
  CONSTRAINT `idCategoria` FOREIGN KEY (`idCategoria`) REFERENCES `categoria_eventos` (`id`),
  CONSTRAINT `idUsuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventos`
--

LOCK TABLES `eventos` WRITE;
/*!40000 ALTER TABLE `eventos` DISABLE KEYS */;
INSERT INTO `eventos` VALUES (2,1,'party','2020-11-30','00:00:00','Ven xd',2.25,100,4,'ESA','Arm','Barrio nuevo',1),(7,14,'Concierto de KISS','2020-12-25','18:00:00','Compra tus entradas para ver a KISS',10,200,195,'El Salvador','San Salvador','Estadio Cuscatlán',1),(8,8,'Platzi Fest','2020-12-20','13:00:00','A great event',2,150,150,'El Salvador','Santa tecla','Colegio Citalá',5),(9,15,'Matrimonio de Sofía','2020-12-27','16:00:00','Estás invitado al matrimonio de mi hiija Sofía',0,50,50,'El Salvador','San Salvador','Catedral Metropolitana',5);
/*!40000 ALTER TABLE `eventos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monedero`
--

DROP TABLE IF EXISTS `monedero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monedero` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idEvent` int NOT NULL,
  `idUser` int NOT NULL,
  `monto` double NOT NULL,
  `descontado` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idUsuario_idx` (`idUser`),
  KEY `idEvento_idx` (`idEvent`),
  CONSTRAINT `idEvent` FOREIGN KEY (`idEvent`) REFERENCES `eventos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `idUser` FOREIGN KEY (`idUser`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monedero`
--

LOCK TABLES `monedero` WRITE;
/*!40000 ALTER TABLE `monedero` DISABLE KEYS */;
INSERT INTO `monedero` VALUES (1,2,1,2.025,0.225),(4,7,14,27,3),(5,8,8,0,0),(6,9,15,0,0);
/*!40000 ALTER TABLE `monedero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_evento` int NOT NULL,
  `id_usuario` int NOT NULL,
  `idBankTarjeta` int NOT NULL,
  `cantidadEntradas` int NOT NULL,
  `total` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idEvento_idx` (`id_evento`),
  KEY `idUsuario_idx` (`id_usuario`),
  KEY `id_tarjeta_idx` (`idBankTarjeta`),
  CONSTRAINT `id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `id_evento` FOREIGN KEY (`id_evento`) REFERENCES `eventos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos`
--

LOCK TABLES `pedidos` WRITE;
/*!40000 ALTER TABLE `pedidos` DISABLE KEYS */;
INSERT INTO `pedidos` VALUES (31,2,1,1,12,27),(32,2,1,2,15,33.75),(33,2,1,1,3,6.75),(34,2,1,2,2,4.5),(35,2,1,1,4,9),(36,2,1,2,1,2.25),(37,2,1,3,5,11.25),(38,2,1,1,6,13.5),(39,2,1,2,7,15.75),(40,2,1,3,8,18),(41,2,1,1,9,20.25),(42,2,1,2,3,6.75),(43,2,1,3,3,6.75),(44,2,1,2,4,9),(45,2,1,3,4,9),(46,2,1,2,2,4.5),(47,2,1,1,2,4.5),(48,2,1,1,2,4.5),(49,2,1,1,2,4.5),(50,2,1,1,5,11.25),(51,2,7,1,5,11.25),(52,2,7,1,5,11.25),(54,2,8,20,5,11.25),(56,2,14,21,1,2.25),(57,7,8,20,2,20),(58,7,15,23,3,30);
/*!40000 ALTER TABLE `pedidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarjetadecredito`
--

DROP TABLE IF EXISTS `tarjetadecredito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarjetadecredito` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numeroTarjeta` varchar(50) NOT NULL,
  `codigoSeguridad` varchar(50) NOT NULL,
  `vencimiento` date NOT NULL,
  `idOwner` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idOwner_idx` (`idOwner`),
  CONSTRAINT `idOwner` FOREIGN KEY (`idOwner`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarjetadecredito`
--

LOCK TABLES `tarjetadecredito` WRITE;
/*!40000 ALTER TABLE `tarjetadecredito` DISABLE KEYS */;
INSERT INTO `tarjetadecredito` VALUES (1,'12547','482','2021-03-01',1),(7,'121212121212','753','2023-07-01',7),(11,'147952368741','145','2029-08-01',7),(14,'123123123456','154','2029-01-01',10),(15,'197836452789','125','2031-05-01',12),(16,'125436951478','001','2020-03-01',5),(21,'159753698745','597','2035-05-01',14),(22,'756987841256','888','2031-06-01',15),(23,'789654587896','564','2035-06-01',15);
/*!40000 ALTER TABLE `tarjetadecredito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pais` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `userName` varchar(50) NOT NULL,
  `contrasenna` varchar(50) NOT NULL,
  `correo` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'ESA','Arm','rene03','xd','r@r'),(2,'GUA','Prin','famo','xdxd','f@f'),(3,'HON','Prin','mac','123','m@m'),(4,'NIC','Prin','js','ymc','j@j'),(5,'SV','Sonso','rene04','xd','re@re.com'),(7,'Bichopolis','Chilena','Serrene7','python','7@7.com'),(8,'El Salvador','Santa Tecla','matakiller','killer87','mat@gmail.com'),(9,'SV','arm','ders','dfdff','ddfdf'),(10,'SV','ARM','pep','14RM','pep@pep'),(11,'ESP','Cat','mou','as','mou@mou'),(12,'SV','ST','flow','14RM','fl@fl'),(13,'ESA','GOTTHAM','Xopxsam','siu','sirve@gmail.com'),(14,'Honduras','Tegucigalpa','FelipeSexto','RockRoll','feli@pe.com'),(15,'Nicargua','Managua','RossBoss','BoxyTer55','Boss@hotmail.com');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'eventbrite'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 17:05:28
