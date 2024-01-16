-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 11:14 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `proyectopoobd`
--

-- --------------------------------------------------------

--
-- Table structure for table `cartas`
--

CREATE TABLE `cartas` (
  `carta` INT(11) NOT NULL,
  `descripcion` VARCHAR(50) DEFAULT NULL,
  `imagen` VARCHAR(255) NOT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  `categoria` INT(11) NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cartas`
--

INSERT INTO `cartas` (`carta`, `descripcion`, `imagen`, `estado`, `categoria`) VALUES
(1, 'Dwayne Johnson', 'Actores\\Dwayne Johnson.png', 1, 4),
(2, 'Emma Watson', 'Actores\\Emma Watson.png', 1, 4),
(3, 'Jennifer Aniston', 'Actores\\Jennifer Aniston.png', 1, 4),
(4, 'Johnny Depp', 'Actores\\Johnny Depp.png', 1, 4),
(5, 'Keanu Reeves', 'Actores\\Keanu Reeves.png', 1, 4),
(6, 'Leonardo DiCaprio', 'Actores\\Leonardo DiCaprio.png', 1, 4),
(7, 'Megan Fox', 'Actores\\Megan Fox.png', 1, 4),
(8, 'Morgan Freeman', 'Actores\\Morgan Freeman.png', 1, 4),
(9, 'Scarlett Johansson', 'Actores\\Scarlett Johansson.png', 1, 4),
(10, 'Will Smith', 'Actores\\Will Smith.png', 1, 4),
(11, 'Bob Marley', 'Cantantes\\Bob Marley.png', 1, 0),
(12, 'Dua Lipa', 'Cantantes\\Dua Lipa.png', 1, 0),
(13, 'Elvis Presley', 'Cantantes\\Elvis Presley.png', 1, 0),
(14, 'Freddie Mercury', 'Cantantes\\Freddie Mercury.png', 1, 0),
(15, 'Justin Bieber', 'Cantantes\\Justin Bieber.png', 1, 0),
(16, 'Michael Jackson', 'Cantantes\\Michael Jackson.png', 1, 0),
(17, 'Rauw Alejandro', 'Cantantes\\Rauw Alejandro.png', 1, 0),
(18, 'Shakira', 'Cantantes\\Shakira.png', 1, 0),
(19, 'Taylor Swift', 'Cantantes\\Taylor Swift.png', 1, 0),
(20, 'The Weekend', 'Cantantes\\The Weekend.png', 1, 0),
(21, 'Catedral de San Basilio', 'Lugares turisticos\\Catedral de San Basilio.png', 1, 1),
(22, 'Coliseo de Roma', 'Lugares turisticos\\Coliseo de Roma.png', 1, 1),
(23, 'Cristo Redentor', 'Lugares turisticos\\Cristo Redentor.png', 1, 1),
(24, 'Estatua de la Libertad', 'Lugares turisticos\\Estatua de la Libertad.png', 1, 1),
(25, 'Machu Picchu', 'Lugares turisticos\\Machu Picchu.png', 1, 1),
(26, 'Mitad del Mundo', 'Lugares turisticos\\Mitad del Mundo.png', 1, 1),
(27, 'Pailón del Diablo', 'Lugares turisticos\\Pailón del Diablo.png', 1, 1),
(28, 'Taj Mahal', 'Lugares turisticos\\Taj Mahal.png', 1, 1),
(29, 'Torre de Pisa', 'Lugares turisticos\\Torre de Pisa.png', 1, 1),
(30, 'Torre Eiffel', 'Lugares turisticos\\Torre Eiffel.png', 1, 1),
(31, 'bulbasaur', 'Pokemones\\003 bulbasaur.png', 1, 2),
(32, 'charmander', 'Pokemones\\004 charmander.png', 1, 2),
(33, 'squirtle', 'Pokemones\\007 squirtle.png', 1, 2),
(34, 'butterfree', 'Pokemones\\012 butterfree.png', 1, 2),
(35, 'spearow', 'Pokemones\\021 spearow.png', 1, 2),
(36, 'pikachu', 'Pokemones\\025 pikachu.png', 1, 2),
(37, 'meowth', 'Pokemones\\052 meowth.png', 1, 2),
(38, 'mr mime', 'Pokemones\\122 mr mime.png', 1, 2),
(39, 'dragonite', 'Pokemones\\149 dragonite.png', 1, 2),
(40, 'mewtwo', 'Pokemones\\150 mewtwo.png', 1, 2),
(41, 'celebi', 'Pokemones\\celebi.png', 1, 2),
(42, 'charizard', 'Pokemones\\charizard.png', 1, 2),
(43, 'jolteon', 'Pokemones\\jolteon.png', 1, 2),
(44, 'lugia', 'Pokemones\\lugia.png', 1, 2),
(45, 'mew', 'Pokemones\\mew.png', 1, 2),
(46, 'mewtwo', 'Pokemones\\mewtwo.png', 1, 2),
(47, 'pikachu', 'Pokemones\\pikachu.png', 1, 2),
(48, 'torchic', 'Pokemones\\torchic.png', 1, 2),
(49, 'treecko', 'Pokemones\\reecko.png', 1, 2),
(50, 'vulpix', 'Pokemones\\vulpix.png', 1, 2),
(51, 'Batman', 'Personajes UCM - DC\\Batman.png', 1, 5),
(52, 'Bruja Escarlata', 'Personajes UCM - DC\\Bruja Escarlata.png', 1, 5),
(53, 'Capitan America', 'Personajes UCM - DC\\Capitan America.png', 1, 5),
(54, 'El Guason', 'Personajes UCM - DC\\El Guason.png', 1, 5),
(55, 'Harley Quinn', 'Personajes UCM - DC\\Harley Quinn.png', 1, 5),
(56, 'Hulk', 'Personajes UCM - DC\\Hulk.png', 1, 5),
(57, 'Iron Man', 'Personajes UCM - DC\\Iron Man.png', 1, 5),
(58, 'Mujer Maravilla', 'Personajes UCM - DC\\Mujer Maravilla.png', 1, 5),
(59, 'Superman', 'Personajes UCM - DC\\Superman.png', 1, 5),
(60, 'Viuda Negra', 'Personajes UCM - DC\\Viuda Negra.png', 1, 5),
(61, 'Arroz con Menestra', 'Comidas típicas del Ecuador\\Arroz con Menestra.png', 1, 3),
(62, 'Bolon', 'Comidas típicas del Ecuador\\Bolon.png', 1, 3),
(63, 'Ceviche de pescado', 'Comidas típicas del Ecuador\\Ceviche de pescado.png', 1, 3),
(64, 'Chaulafán', 'Comidas típicas del Ecuador\\Chaulafán.png', 1, 3),
(65, 'Churrasco', 'Comidas típicas del Ecuador\\Churrasco.png', 1, 3),
(66, 'Encebollado', 'Comidas típicas del Ecuador\\Encebollado.png', 1, 3),
(67, 'Fritada', 'Comidas típicas del Ecuador\\Fritada.png', 1, 3),
(68, 'Llapingacho', 'Comidas típicas del Ecuador\\Llapingacho.png', 1, 3),
(69, 'Locro de papa', 'Comidas típicas del Ecuador\\Locro de papa.png', 1, 3),
(70, 'Seco de pollo', 'Comidas típicas del Ecuador\\Seco de pollo.png', 1, 3);

----------------------------------------------------------

--
-- Table structure for table `categorias`
--

CREATE TABLE `categorias` (
  `categoria` INT(11) NOT NULL,
  `descripcion` VARCHAR(50) NOT NULL,
  `estado` TINYINT(1) NOT NULL DEFAULT 1,
  `valida_edad` TINYINT(1) NOT NULL DEFAULT 0,
  `edad_desde` INT(11) NOT NULL DEFAULT 0,
  `edad_hasta` INT(11) NOT NULL DEFAULT 0,
  `color` VARCHAR(10) DEFAULT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categorias`
--

INSERT INTO `categorias` (`categoria`, `descripcion`, `estado`, `valida_edad`, `edad_desde`, `edad_hasta`, `color`) VALUES
(0, 'Cantantes', 1, 0, 0, 0, '86E8C2'),
(1, 'Lugares Turísticos', 1, 0, 0, 0, '8BE87E'),
(2, 'Pokemons', 1, 0, 0, 0, 'BFAEA4'),
(3, 'Comidas típicas del Ecuador', 1, 0, 0, 0, '70CB7C'),
(4, 'Actores', 1, 0, 0, 0, 'D09A5C'),
(5, 'Marvel & DC', 1, 0, 0, 0, '9ADCC1');

-- --------------------------------------------------------

--
-- Table structure for table `configuracion`
--

CREATE TABLE `configuracion` (
  `id` TINYINT(4) NOT NULL,
  `nombre_aplicacion` VARCHAR(100) NOT NULL DEFAULT '',
  `ruta_imagenes` VARCHAR(100) NOT NULL DEFAULT '',
  `imagen_logo` VARCHAR(100) NOT NULL DEFAULT '',
  `tiempo_por_juego` INT(11) DEFAULT NULL,
  `mensaje_ganado` VARCHAR(100) NOT NULL DEFAULT '',
  `mensaje_perdido` VARCHAR(100) NOT NULL DEFAULT '',
  `mensaje_final` VARCHAR(100) NOT NULL DEFAULT ''
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `juego_memoria`
--

CREATE TABLE `juego_memoria` (
  `id` INT(11) NOT NULL,
  `jugador` INT(11) NOT NULL,
  `fecha_inicio` DATETIME NOT NULL,
  `fecha_fin` DATETIME NOT NULL,
  `errores` INT(11) NOT NULL DEFAULT 0
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `juego_velocidad_cab`
--

CREATE TABLE `juego_velocidad_cab` (
  `id` INT(11) NOT NULL,
  `jugador` INT(11) NOT NULL,
  `fecha_inicio` DATETIME NOT NULL,
  `fecha_fin` DATETIME NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `juego_velocidad_cab`
--

INSERT INTO `juego_velocidad_cab` (`id`, `jugador`, `fecha_inicio`, `fecha_fin`) VALUES
(1, 1, '2024-01-13 10:00:00', '2024-01-13 10:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `juego_velocidad_det`
--

CREATE TABLE `juego_velocidad_det` (
  `id` INT(11) NOT NULL,
  `id_cab` INT(11) NOT NULL,
  `carta` INT(11) NOT NULL,
  `acierto` TINYINT(1) NOT NULL DEFAULT 0,
  `fecha_inicio` DATETIME NOT NULL,
  `fecha_fin` DATETIME NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `jugadores`
--

CREATE TABLE `jugadores` (
  `jugador` INT(11) NOT NULL,
  `nombres` VARCHAR(100) NOT NULL,
  `tipo_identificacion` CHAR(1) NOT NULL,
  `identificacion` VARCHAR(15) NOT NULL,
  `edad` INT(11) NOT NULL,
  `fecha_registro` DATETIME NOT NULL
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jugadores`
--

INSERT INTO `jugadores` (`jugador`, `nombres`, `tipo_identificacion`, `identificacion`, `edad`, `fecha_registro`) VALUES
(1, 'Miguek', 'C', '99999', 29, '2024-01-13 23:12:24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cartas`
--
ALTER TABLE `cartas`
  ADD PRIMARY KEY (`carta`),
  ADD KEY `categoria` (`categoria`);

--
-- Indexes for table `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`categoria`);

--
-- Indexes for table `configuracion`
--
ALTER TABLE `configuracion`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `juego_memoria`
--
ALTER TABLE `juego_memoria`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jugador` (`jugador`);

--
-- Indexes for table `juego_velocidad_cab`
--
ALTER TABLE `juego_velocidad_cab`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jugador` (`jugador`);

--
-- Indexes for table `juego_velocidad_det`
--
ALTER TABLE `juego_velocidad_det`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cab` (`id_cab`),
  ADD KEY `carta` (`carta`);

--
-- Indexes for table `jugadores`
--
ALTER TABLE `jugadores`
  ADD PRIMARY KEY (`jugador`),
  ADD UNIQUE KEY `identificacion` (`identificacion`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jugadores`
--
ALTER TABLE `jugadores`
  MODIFY `jugador` INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cartas`
--
ALTER TABLE `cartas`
  ADD CONSTRAINT `cartas_ibfk_1` FOREIGN KEY (`categoria`) REFERENCES `categorias` (`categoria`);

--
-- Constraints for table `juego_memoria`
--
ALTER TABLE `juego_memoria`
  ADD CONSTRAINT `juego_memoria_ibfk_1` FOREIGN KEY (`jugador`) REFERENCES `jugadores` (`jugador`);

--
-- Constraints for table `juego_velocidad_cab`
--
ALTER TABLE `juego_velocidad_cab`
  ADD CONSTRAINT `juego_velocidad_cab_ibfk_1` FOREIGN KEY (`jugador`) REFERENCES `jugadores` (`jugador`);

--
-- Constraints for table `juego_velocidad_det`
--
ALTER TABLE `juego_velocidad_det`
  ADD CONSTRAINT `juego_velocidad_det_ibfk_1` FOREIGN KEY (`id_cab`) REFERENCES `juego_velocidad_cab` (`id`),
  ADD CONSTRAINT `juego_velocidad_det_ibfk_2` FOREIGN KEY (`carta`) REFERENCES `cartas` (`carta`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
