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

/*Data for the table `cartas` */

insert  into `cartas`(`carta`,`descripcion`,`imagen`,`estado`,`categoria`) values (1,'Dwayne Johnson','Actores/DwayneJohnson.png',1,4),(2,'Emma Watson','Actores/EmmaWatson.png',1,4),(3,'Jennifer Aniston','Actores/JenniferAniston.png',1,4),(4,'Johnny Depp','Actores/JohnnyDepp.png',1,4),(5,'Keanu Reeves','Actores/KeanuReeves.png',1,4),(6,'Leonardo DiCaprio','Actores/LeonardoDiCaprio.png',1,4),(7,'Megan Fox','Actores/MeganFox.png',1,4),(8,'Morgan Freeman','Actores/MorganFreeman.png',1,4),(9,'Scarlett Johansson','Actores/ScarlettJohansson.png',1,4),(10,'Will Smith','Actores/WillSmith.png',1,4),(11,'Bob Marley','Cantantes/BobMarley.png',1,0),(12,'Dua Lipa','Cantantes/DuaLipa.png',1,0),(13,'Elvis Presley','Cantantes/ElvisPresley.png',1,0),(14,'Freddie Mercury','Cantantes/FreddieMercury.png',1,0),(15,'Justin Bieber','Cantantes/JustinBieber.png',1,0),(16,'Michael Jackson','Cantantes/MichaelJackson.png',1,0),(17,'Rauw Alejandro','Cantantes/RauwAlejandro.png',1,0),(18,'Shakira','Cantantes/Shakira.png',1,0),(19,'Taylor Swift','Cantantes/TaylorSwift.png',1,0),(20,'The Weekend','Cantantes/TheWeekend.png',1,0),(21,'Catedral de San Basilio','Lugaresturisticos/CatedraldeSanBasilio.png',1,1),(22,'Coliseo de Roma','Lugaresturisticos/ColiseodeRoma.png',1,1),(23,'Cristo Redentor','Lugaresturisticos/CristoRedentor.png',1,1),(24,'Estatua de la Libertad','Lugaresturisticos/EstatuadelaLibertad.png',1,1),(25,'Machu Picchu','Lugaresturisticos/MachuPicchu.png',1,1),(26,'Mitad del Mundo','Lugaresturisticos/MitaddelMundo.png',1,1),(27,'Pailón del Diablo','Lugaresturisticos/PailóndelDiablo.png',1,1),(28,'Taj Mahal','Lugaresturisticos/TajMahal.png',1,1),(29,'Torre de Pisa','Lugaresturisticos/TorredePisa.png',1,1),(30,'Torre Eiffel','Lugaresturisticos/TorreEiffel.png',1,1),(31,'bulbasaur','Pokemones/003bulbasaur.png',1,2),(32,'charmander','Pokemones/004charmander.png',1,2),(33,'squirtle','Pokemones/007squirtle.png',1,2),(34,'butterfree','Pokemones/012butterfree.png',1,2),(35,'spearow','Pokemones/021spearow.png',1,2),(36,'pikachu','Pokemones/025pikachu.png',1,2),(37,'meowth','Pokemones/052meowth.png',1,2),(38,'mr mime','Pokemones/122mrmime.png',1,2),(39,'dragonite','Pokemones/149dragonite.png',1,2),(40,'mewtwo','Pokemones/150mewtwo.png',1,2),(41,'celebi','Pokemones/celebi.png',1,2),(42,'charizard','Pokemones/charizard.png',1,2),(43,'jolteon','Pokemones/jolteon.png',1,2),(44,'lugia','Pokemones/lugia.png',1,2),(45,'mew','Pokemones/mew.png',1,2),(46,'mewtwo','Pokemones/mewtwo.png',1,2),(47,'pikachu','Pokemones/pikachu.png',1,2),(48,'torchic','Pokemones/torchic.png',1,2),(49,'treecko','Pokemones/reecko.png',1,2),(50,'vulpix','Pokemones/vulpix.png',1,2);

/*Table structure for table `categorias` */

DROP TABLE IF EXISTS `categorias`;

CREATE TABLE `categorias` (
  `categoria` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1,
  `valida_edad` tinyint(1) NOT NULL DEFAULT 0,
  `edad_desde` int(11) NOT NULL DEFAULT 0,
  `edad_hasta` int(11) NOT NULL DEFAULT 0,
  `color` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `categorias` */

insert  into `categorias`(`categoria`,`descripcion`,`estado`,`valida_edad`,`edad_desde`,`edad_hasta`,`color`) values (0,'Cantantes',1,0,0,0,'86E8C2'),(1,'Lugares Turísticos',1,0,0,0,'8BE87E'),(2,'Pokemons',1,0,0,0,'BFAEA4'),(3,'Comidas típicas del Ecuador',1,0,0,0,'70CB7C'),(4,'Actores',1,0,0,0,'D09A5C'),(5,'Marvel & DC',1,0,0,0,'9ADCC1');

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

/*Data for the table `configuracion` */

/*Table structure for table `juego_memoria` */

DROP TABLE IF EXISTS `juego_memoria`;

CREATE TABLE `juego_memoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jugador` int(11) NOT NULL,
  `tiempo` char(5) NOT NULL,
  `errores` int(11) NOT NULL DEFAULT 0,
  `puntuacion` decimal(19,0) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jugador` (`jugador`),
  CONSTRAINT `juego_memoria_ibfk_1` FOREIGN KEY (`jugador`) REFERENCES `jugadores` (`jugador`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `juego_memoria` */

insert  into `juego_memoria`(`id`,`jugador`,`tiempo`,`errores`,`puntuacion`) values (3,4,'00:36',15,800),(4,4,'00:42',18,950),(5,4,'01:05',21,1242),(6,4,'00:40',11,1432),(7,4,'01:20',15,875);

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

/*Data for the table `juego_velocidad_cab` */

insert  into `juego_velocidad_cab`(`id`,`jugador`,`fecha_inicio`,`fecha_fin`) values (1,1,'2024-01-13 10:00:00','2024-01-13 10:30:00');

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

/*Data for the table `juego_velocidad_det` */

/*Table structure for table `jugadores` */

DROP TABLE IF EXISTS `jugadores`;

CREATE TABLE `jugadores` (
  `jugador` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) NOT NULL,
  `tipo_identificacion` char(1) NOT NULL,
  `identificacion` varchar(15) NOT NULL,
  `edad` int(11) NOT NULL,
  `fecha_registro` datetime DEFAULT NULL,
  PRIMARY KEY (`jugador`),
  UNIQUE KEY `identificacion` (`identificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `jugadores` */

insert  into `jugadores`(`jugador`,`nombres`,`tipo_identificacion`,`identificacion`,`edad`,`fecha_registro`) values (1,'Miguek','C','fgggdf',29,'2024-01-13 23:12:24'),(4,'Miguel','C','0962869665',30,NULL),(5,'dfdfdf','C','7896541236',18,NULL),(6,'pedro','C','0998555240',30,NULL),(7,'pedritodelospalotes','C','7896547896',53,NULL),(8,'pepitojuanuiti','C','4566544561',24,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
