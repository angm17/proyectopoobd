/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.27-MariaDB : Database - proyectopoobd
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`proyectopoobd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `proyectopoobd`;

/*Table structure for table `cartas` */

DROP TABLE IF EXISTS `cartas`;

CREATE TABLE `cartas` (
  `carta` int(11) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `imagen` varchar(255) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1,
  `categoria` int(11) NOT NULL,
  PRIMARY KEY (`carta`),
  KEY `categoria` (`categoria`),
  CONSTRAINT `cartas_ibfk_1` FOREIGN KEY (`categoria`) REFERENCES `categorias` (`categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `categorias` */

DROP TABLE IF EXISTS `categorias`;

CREATE TABLE `categorias` (
  `categoria` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1,
  `valida_edad` tinyint(1) NOT NULL DEFAULT 0,
  `edad_desde` int(11) NOT NULL DEFAULT 0,
  `edad_hasta` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `configuracion` */

DROP TABLE IF EXISTS `configuracion`;

CREATE TABLE `configuracion` (
  `id` tinyint(4) NOT NULL,
  `nombre_aplicacion` varchar(100) NOT NULL DEFAULT '',
  `ruta_imagenes` varchar(100) NOT NULL DEFAULT '',
  `imagen_logo` varchar(100) NOT NULL DEFAULT '',
  `tiempo_por_juego` int(11) DEFAULT NULL,
  `mensaje_ganado` varchar(100) NOT NULL DEFAULT '',
  `mensaje_perdido` varchar(100) NOT NULL DEFAULT '',
  `mensaje_final` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `juego_memoria` */

DROP TABLE IF EXISTS `juego_memoria`;

CREATE TABLE `juego_memoria` (
  `id` int(11) NOT NULL,
  `jugador` int(11) NOT NULL,
  `fecha_inicio` datetime NOT NULL,
  `fecha_fin` datetime NOT NULL,
  `errores` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `jugador` (`jugador`),
  CONSTRAINT `juego_memoria_ibfk_1` FOREIGN KEY (`jugador`) REFERENCES `jugadores` (`jugador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `juego_velocidad_cab` */

DROP TABLE IF EXISTS `juego_velocidad_cab`;

CREATE TABLE `juego_velocidad_cab` (
  `id` int(11) NOT NULL,
  `jugador` int(11) NOT NULL,
  `fecha_inicio` datetime NOT NULL,
  `fecha_fin` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jugador` (`jugador`),
  CONSTRAINT `juego_velocidad_cab_ibfk_1` FOREIGN KEY (`jugador`) REFERENCES `jugadores` (`jugador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `juego_velocidad_det` */

DROP TABLE IF EXISTS `juego_velocidad_det`;

CREATE TABLE `juego_velocidad_det` (
  `id` int(11) NOT NULL,
  `id_cab` int(11) NOT NULL,
  `carta` int(11) NOT NULL,
  `acierto` tinyint(1) NOT NULL DEFAULT 0,
  `fecha_inicio` datetime NOT NULL,
  `fecha_fin` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cab` (`id_cab`),
  KEY `carta` (`carta`),
  CONSTRAINT `juego_velocidad_det_ibfk_1` FOREIGN KEY (`id_cab`) REFERENCES `juego_velocidad_cab` (`id`),
  CONSTRAINT `juego_velocidad_det_ibfk_2` FOREIGN KEY (`carta`) REFERENCES `cartas` (`carta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `jugadores` */

DROP TABLE IF EXISTS `jugadores`;

CREATE TABLE `jugadores` (
  `jugador` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) NOT NULL,
  `tipo_identificacion` char(1) NOT NULL,
  `identificacion` varchar(15) NOT NULL,
  `edad` int(11) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  PRIMARY KEY (`jugador`),
  UNIQUE KEY `identificacion` (`identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
