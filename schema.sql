CREATE DATABASE IF NOT EXISTS cafe_cultural;
USE cafe_cultural;

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    disponible TINYINT(1) NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion VARCHAR(255),
    fecha DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS inscripciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    evento_id INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (evento_id) REFERENCES eventos(id)
);

CREATE TABLE IF NOT EXISTS mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    mensaje TEXT NOT NULL,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO productos (nombre, descripcion, precio, disponible) VALUES
('Café de especialidad', 'Grano de origen, tostado medio', 1200, 1),
('Capuchino', 'Espresso con leche vaporizada', 1500, 1),
('Tarta de limón', 'Porción artesanal', 900, 1),
('Limonada de jengibre', 'Con menta fresca', 1100, 1);

INSERT INTO eventos (titulo, descripcion, fecha) VALUES
('Música en vivo', 'Una noche para disfrutar música y café.', '2026-11-15'),
('Degustación de café', 'Probamos distintos métodos y granos.', '2026-11-22'),
('Tarde de lectura', 'Un encuentro para compartir libros.', '2026-11-29');
