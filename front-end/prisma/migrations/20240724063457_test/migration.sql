-- CreateTable
CREATE TABLE "asistencia" (
    "id" SERIAL NOT NULL,
    "cedula" VARCHAR(20) NOT NULL,
    "fecha" VARCHAR(20) NOT NULL,
    "hora_entrada" VARCHAR(50) NOT NULL,
    "hora_salida" VARCHAR(50),

    CONSTRAINT "asistencia_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "empleados" (
    "cedula" VARCHAR(20) NOT NULL,
    "nombre" VARCHAR(50) NOT NULL,
    "apellido1" VARCHAR(50) NOT NULL,
    "apellido2" VARCHAR(50) NOT NULL,
    "correo" VARCHAR(100) NOT NULL,
    "telefono" VARCHAR(20) NOT NULL,

    CONSTRAINT "empleados_pkey" PRIMARY KEY ("cedula")
);

-- CreateIndex
CREATE UNIQUE INDEX "asistencia_cedula_fecha_key" ON "asistencia"("cedula", "fecha");

-- AddForeignKey
ALTER TABLE "asistencia" ADD CONSTRAINT "asistencia_cedula_fkey" FOREIGN KEY ("cedula") REFERENCES "empleados"("cedula") ON DELETE NO ACTION ON UPDATE NO ACTION;
