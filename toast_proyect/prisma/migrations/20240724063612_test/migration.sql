/*
  Warnings:

  - The `hora_salida` column on the `asistencia` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - Changed the type of `fecha` on the `asistencia` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.
  - Changed the type of `hora_entrada` on the `asistencia` table. No cast exists, the column would be dropped and recreated, which cannot be done if there is data, since the column is required.

*/
-- AlterTable
ALTER TABLE "asistencia" DROP COLUMN "fecha",
ADD COLUMN     "fecha" DATE NOT NULL,
DROP COLUMN "hora_entrada",
ADD COLUMN     "hora_entrada" TIME(6) NOT NULL,
DROP COLUMN "hora_salida",
ADD COLUMN     "hora_salida" TIME(6);

-- CreateIndex
CREATE UNIQUE INDEX "asistencia_cedula_fecha_key" ON "asistencia"("cedula", "fecha");
