CREATE DATABASE urban45_db
    WITH ENCODING = 'UTF8';

\c urban45_db;

-- =============================================================================
-- 1. TABLA: plan_membresia
-- Catálogo de planes que ofrece el gimnasio (Básico, Standard y Premium).
-- =============================================================================
CREATE TABLE plan_membresia (
    id_plan SERIAL PRIMARY KEY,
    nombre_plan VARCHAR(50) NOT NULL UNIQUE,
    precio_mensual NUMERIC(8, 2) NOT NULL CHECK (precio_mensual > 0),
    duracion_dias INTEGER NOT NULL DEFAULT 30 CHECK (duracion_dias > 0),
    descripcion TEXT NOT NULL DEFAULT ''
);

-- =============================================================================
-- 2. TABLA: cliente
-- Socios inscritos en Urban 45 (con DNI y correo únicos).
-- =============================================================================
CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    dni CHAR(8) NOT NULL UNIQUE,
    telefono VARCHAR(15) NOT NULL,
    correo VARCHAR(120) NOT NULL UNIQUE,
    fecha_registro DATE NOT NULL DEFAULT CURRENT_DATE
);

-- =============================================================================
-- 3. TABLA: membresia
-- Suscripciones contratadas que relacionan un cliente con un plan específico.
-- =============================================================================
CREATE TABLE membresia (
    id_membresia SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    id_plan INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'Activa'
        CHECK (estado IN ('Activa', 'Por Vencer', 'Vencida')),
    CONSTRAINT fk_membresia_cliente
        FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        ON DELETE CASCADE,
    CONSTRAINT fk_membresia_plan
        FOREIGN KEY (id_plan) REFERENCES plan_membresia (id_plan)
        ON DELETE RESTRICT,
    CONSTRAINT chk_fechas_membresia
        CHECK (fecha_fin >= fecha_inicio)
);

-- =============================================================================
-- 4. TABLA: rutina_entrenamiento
-- Planes de ejercicios asignados a cada cliente según objetivo y condición.
-- =============================================================================
CREATE TABLE rutina_entrenamiento (
    id_rutina SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    nombre_rutina VARCHAR(100) NOT NULL,
    objetivo_cliente VARCHAR(80) NOT NULL,
    condicion_fisica VARCHAR(50) NOT NULL,
    entrenador_asignado VARCHAR(80) NOT NULL DEFAULT 'Entrenador Urban 45',
    fecha_asignacion DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_rutina_cliente
        FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        ON DELETE CASCADE
);

-- =============================================================================
-- 5. TABLA: progreso_cliente
-- Historial de evaluaciones físicas (peso levantado en kg y repeticiones).
-- =============================================================================
CREATE TABLE progreso_cliente (
    id_progreso SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    peso_levantado_kg NUMERIC(6, 2) NOT NULL CHECK (peso_levantado_kg >= 0),
    repeticiones INTEGER NOT NULL CHECK (repeticiones > 0),
    comentario VARCHAR(200) NOT NULL DEFAULT '',
    CONSTRAINT fk_progreso_cliente
        FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        ON DELETE CASCADE
);

-- =============================================================================
-- 6. TABLA: pago
-- Comprobantes y facturas emitidas por el cobro de membresías.
-- =============================================================================
CREATE TABLE pago (
    id_pago SERIAL PRIMARY KEY,
    id_cliente INTEGER NOT NULL,
    id_membresia INTEGER NULL,
    concepto VARCHAR(120) NOT NULL,
    monto NUMERIC(8, 2) NOT NULL CHECK (monto > 0),
    fecha_pago DATE NOT NULL DEFAULT CURRENT_DATE,
    estado_pago VARCHAR(20) NOT NULL DEFAULT 'Pagado'
        CHECK (estado_pago IN ('Pagado', 'Pendiente')),
    CONSTRAINT fk_pago_cliente
        FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
        ON DELETE CASCADE,
    CONSTRAINT fk_pago_membresia
        FOREIGN KEY (id_membresia) REFERENCES membresia (id_membresia)
        ON DELETE SET NULL
);

-- Índices recomendados para agilizar búsquedas frecuentes
CREATE INDEX idx_cliente_dni ON cliente (dni);
CREATE INDEX idx_membresia_estado ON membresia (estado);
CREATE INDEX idx_pago_estado ON pago (estado_pago);

-- =============================================================================
-- DATOS SEMILLA INICIALES (Basados en las pantallas de prueba de Urban 45)
-- =============================================================================
INSERT INTO plan_membresia (nombre_plan, precio_mensual, duracion_dias, descripcion) VALUES
    ('Básico', 90.00, 30, 'Acceso al área de musculación y cardio en horario regular.'),
    ('Standard', 140.00, 30, 'Musculación, zona de cardio y acceso a clases grupales.'),
    ('Premium', 200.00, 30, 'Acceso total, área funcional, seguimiento de progreso y entrenador.');

INSERT INTO cliente (nombre, apellidos, dni, telefono, correo, fecha_registro) VALUES
    ('David', 'Lachira', '71234501', '987654321', 'da.lachira@email.com', '2026-10-01'),
    ('Odalis', 'Domínguez', '71234502', '912345678', 'odalis@email.com', '2026-10-03'),
    ('Jorge', 'Suárez', '71234503', '961234567', 'jorge.suarez@email.com', '2026-10-05'),
    ('Yarlequé', 'Timaná', '71234504', '930123456', 'yarleque@email.com', '2026-09-20'),
    ('María', 'López', '71234505', '915678234', 'maria.lopez@email.com', '2026-10-08'),
    ('Carlos', 'Fernández', '71234506', '987123654', 'carlos.fernandez@email.com', '2026-10-10'),
    ('Lucía', 'Martínez', '71234507', '951234789', 'lucia.martinez@email.com', '2026-10-12'),
    ('Pedro', 'García', '71234508', '921345678', 'pedro.garcia@email.com', '2026-09-18'),
    ('Elena', 'Torres', '71234509', '912345987', 'elena.torres@email.com', '2026-10-14');

INSERT INTO membresia (id_cliente, id_plan, fecha_inicio, fecha_fin, estado) VALUES
    (1, 3, '2026-10-15', '2026-11-14', 'Activa'),
    (2, 1, '2026-10-18', '2026-11-17', 'Activa'),
    (3, 3, '2026-10-05', '2026-11-04', 'Por Vencer'),
    (4, 1, '2026-09-20', '2026-10-20', 'Vencida'),
    (5, 2, '2026-10-22', '2026-11-21', 'Activa'),
    (6, 3, '2026-10-25', '2026-11-24', 'Activa'),
    (7, 1, '2026-10-04', '2026-11-03', 'Por Vencer'),
    (8, 2, '2026-09-18', '2026-10-18', 'Vencida'),
    (9, 3, '2026-10-28', '2026-11-27', 'Activa');

INSERT INTO rutina_entrenamiento (id_cliente, nombre_rutina, objetivo_cliente, condicion_fisica, entrenador_asignado, fecha_asignacion) VALUES
    (1, 'Fuerza e Hipertrofia Split', 'Aumento de masa muscular', 'Buena', 'Coach Martín Rivas', '2026-10-16'),
    (2, 'Circuito Funcional y Cardio', 'Resistencia y tonificación', 'Media', 'Coach Valeria Gómez', '2026-10-19'),
    (6, 'Fuerza Máxima Progresiva', 'Aumento de masa muscular', 'Buena', 'Coach Martín Rivas', '2026-10-25'),
    (9, 'Acondicionamiento Mixto', 'Fuerza y resistencia', 'Buena', 'Coach Valeria Gómez', '2026-10-28');

INSERT INTO progreso_cliente (id_cliente, fecha, peso_levantado_kg, repeticiones, comentario) VALUES
    (2, '2026-10-25', 50.00, 12, 'Buen progreso esta semana'),
    (6, '2026-10-26', 70.00, 10, 'Mejorar técnica en press de banca'),
    (9, '2026-10-28', 30.00, 15, 'Incrementar peso la próxima sesión'),
    (1, '2026-11-01', 80.00, 8, 'Excelente control de carga en sentadilla');

INSERT INTO pago (id_cliente, id_membresia, concepto, monto, fecha_pago, estado_pago) VALUES
    (1, 1, 'Membresía Premium - Octubre 2026', 200.00, '2026-10-15', 'Pagado'),
    (2, 2, 'Membresía Básico - Octubre 2026', 90.00, '2026-10-18', 'Pagado'),
    (3, 3, 'Membresía Premium - Octubre 2026', 200.00, '2026-10-20', 'Pagado'),
    (5, 5, 'Membresía Standard - Octubre 2026', 140.00, '2026-10-22', 'Pagado'),
    (6, 6, 'Membresía Premium - Octubre 2026', 200.00, '2026-10-25', 'Pagado'),
    (9, 9, 'Membresía Premium - Octubre 2026', 200.00, '2026-10-28', 'Pagado'),
    (4, 4, 'Renovación Plan Básico - Noviembre 2026', 90.00, '2026-11-01', 'Pendiente'),
    (8, 8, 'Renovación Plan Standard - Noviembre 2026', 140.00, '2026-11-02', 'Pendiente');
