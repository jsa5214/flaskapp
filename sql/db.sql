-- Eliminar BD si existeix
DROP DATABASE IF EXISTS practica;

-- Crear BD
CREATE DATABASE practica CHARACTER SET utf8mb4;
USE practica;

-- Eliminar usuari si existeix
DROP USER IF EXISTS 'joelsansi'@'localhost';

-- Crear usuari
CREATE USER 'joelsansi'@'localhost' IDENTIFIED BY '1234';

-- Donar permisos
GRANT ALL PRIVILEGES ON practica.* TO 'joelsansi'@'localhost';
FLUSH PRIVILEGES;

-- Crear taula
CREATE TABLE nom_email (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL
);

-- Inserir dades de prova
INSERT INTO nom_email (nombre, email) VALUES
('Joan', 'joan@example.com'),
('Maria', 'maria@example.com'),
('Pau', 'pau@example.com');
