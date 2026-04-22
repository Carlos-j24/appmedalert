-- ============================================
-- BASE DE DATOS: MEDALERT
-- ============================================

CREATE DATABASE medalert;

-- Usar la base de datos
USE medalert;

-- ============================================
-- TABLA: usuarios
-- ============================================

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- TABLA: medicos
-- ============================================

CREATE TABLE medicos (
    id_medico INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    telefono VARCHAR(20)
);

-- ============================================
-- TABLA: medicamentos
-- ============================================

CREATE TABLE medicamentos (
    id_medicamento INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    tipo VARCHAR(50),
    estado VARCHAR(20) DEFAULT 'activo',
    
    FOREIGN KEY (id_usuario) 
    REFERENCES usuarios(id_usuario)
    ON DELETE CASCADE
);

-- ============================================
-- TABLA: horarios
-- ============================================

CREATE TABLE horarios (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    id_medicamento INT NOT NULL,
    hora TIME NOT NULL,
    frecuencia VARCHAR(50),
    
    FOREIGN KEY (id_medicamento)
    REFERENCES medicamentos(id_medicamento)
    ON DELETE CASCADE
);

-- ============================================
-- TABLA: recordatorios
-- ============================================

CREATE TABLE recordatorios (
    id_recordatorio INT AUTO_INCREMENT PRIMARY KEY,
    id_horario INT NOT NULL,
    fecha DATETIME NOT NULL,
    estado VARCHAR(20) DEFAULT 'pendiente',
    
    FOREIGN KEY (id_horario)
    REFERENCES horarios(id_horario)
    ON DELETE CASCADE
);

-- ============================================
-- TABLA: historial_medicamento
-- ============================================

CREATE TABLE historial_medicamento (
    id_historial INT AUTO_INCREMENT PRIMARY KEY,
    id_recordatorio INT NOT NULL,
    fecha_confirmacion DATETIME,
    observacion TEXT,
    
    FOREIGN KEY (id_recordatorio)
    REFERENCES recordatorios(id_recordatorio)
    ON DELETE CASCADE
);

-- ============================================
-- TABLA: citas_medicas
-- ============================================

CREATE TABLE citas_medicas (
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_medico INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    motivo TEXT,
    estado VARCHAR(20) DEFAULT 'programada',
    
    FOREIGN KEY (id_usuario)
    REFERENCES usuarios(id_usuario)
    ON DELETE CASCADE,
    
    FOREIGN KEY (id_medico)
    REFERENCES medicos(id_medico)
    ON DELETE CASCADE
);