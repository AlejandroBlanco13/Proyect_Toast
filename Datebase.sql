CREATE TABLE empleados (
    cedula VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido1 VARCHAR(50) NOT NULL,
    apellido2 VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL
);
CREATE TABLE asistencia (
    id SERIAL PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL,
    hora_entrada TIME NOT NULL,
    hora_salida TIME,
    FOREIGN KEY (cedula) REFERENCES empleados (cedula),
    UNIQUE (cedula, fecha)
);
INSERT INTO empleados (cedula, nombre, apellido1, apellido2, correo, telefono)
VALUES 
('123456789', 'Juan', 'Pérez', 'Gómez', 'juan.perez@example.com', '555-1234'),
('987654321', 'María', 'López', 'Rodríguez', 'maria.lopez@example.com', '555-5678'),
('456789123', 'Carlos', 'Martínez', 'Fernández', 'carlos.martinez@example.com', '555-8765'),
('654321987', 'Ana', 'García', 'Hernández', 'ana.garcia@example.com', '555-4321');


INSERT INTO asistencia (cedula, fecha, hora_entrada, hora_salida)
VALUES 
('123456789', '2024-07-15', '08:00:00', '17:00:00'),
('987654321', '2024-07-15', '09:00:00', '18:00:00'),
('456789123', '2024-07-15', '07:30:00', '16:30:00'),
('654321987', '2024-07-15', '08:15:00', '17:15:00');

CREATE OR REPLACE FUNCTION ConsultarEmpleadosHoy()
RETURNS TABLE (
    id INT,
    cedula VARCHAR,
    fecha DATE,
    hora_entrada TIME,
    hora_salida TIME,
    nombre VARCHAR,
    apellido1 VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.id,
        a.cedula,
        a.fecha,
        a.hora_entrada,
        a.hora_salida,
        e.nombre,
        e.apellido1
    FROM 
        asistencia a
    JOIN 
        empleados e ON a.cedula = e.cedula
    WHERE 
        a.fecha = CURRENT_DATE;
END;
$$;
INSERT INTO empleados (cedula, nombre, apellido1, apellido2, correo, telefono)
VALUES 
('208460232', 'Alejandro', 'Blanco', 'Barrett', 'alejandroblanco1313@gmail.com', '8304-7436')
INSERT INTO asistencia (cedula, fecha, hora_entrada, hora_salida)
VALUES 
('123456789', '2024-07-17', '08:00:00', '17:00:00')
select * from empleados
DELETE FROM empleados
WHERE cedula = '123456789';