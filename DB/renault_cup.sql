CREATE DATABASE IF NOT EXISTS Copa_Renault;
USE Copa_Renault;

CREATE TABLE `usuarios` (
  `dni` varchar(20) UNIQUE PRIMARY KEY NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `actividad` varchar(50) NOT NULL,
  `escuela` varchar(50) NOT NULL
);

CREATE TABLE `encargados` (
  `dni` varchar(20) PRIMARY KEY NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL
);

CREATE TABLE `escuelas` (
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `cant_equipos` int(10)
);

CREATE TABLE `jugadores` (
  `dni` varchar(20) PRIMARY KEY NOT NULL,
  `dorsal` int(10) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `deporte` varchar(50) NOT NULL
);

CREATE TABLE `equipos` (
  `cant_jugadores` int NOT NULL,
  `encargado` varchar(100) NOT NULL,
  `escuela` varchar(100) NOT NULL
);