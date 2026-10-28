CREATE DATABASE IF NOT EXISTS cafe_cult;
USE cafe_cult;

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

INSERT INTO categorias (nombre) VALUES
('Cafés'),
('Comida');

INSERT INTO productos (nombre, descripcion, precio, id_categoria) VALUES
('Espresso', 'Café intenso y clásico', 2500, 1),
('Café con leche', 'Café acompañado con leche', 3000, 1),
('Capuccino', 'Café con leche y espuma', 3500, 1),
('Medialunas', 'Medialunas de manteca', 1800, 2),
('Tostado', 'Tostado de jamón y queso', 4500, 2),
('Porción de torta', 'Porción de torta del día', 4000, 2);
