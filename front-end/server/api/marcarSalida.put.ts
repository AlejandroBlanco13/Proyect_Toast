import { PrismaClient } from "@prisma/client";
import { formatISO, parseISO } from "date-fns";

const prisma = new PrismaClient();
export default defineEventHandler(async (event) => {
  try {
    const cedulaEmpleado = await readBody(event);
    const response = await fetch(
      "http://worldtimeapi.org/api/timezone/America/Costa_Rica",
      {
        method: "GET",
        headers: {
          "Cache-Control": "no-cache",
        },
      }
    );
    //Obtener la fecha y hora actual
    const data = await response.json();

    const dateTime = data.datetime.toString();

    const fechaISO = parseISO(dateTime);

    const fechaString = formatISO(fechaISO, { representation: "date" });

    var horaEntradaString = dateTime.split("T")[1].split(".")[0];

    horaEntradaString = horaEntradaString.toString();

    //Formatear la fecha a "ISOString"
    const fechaHoraString = `${fechaString}T${horaEntradaString}`;
    const fechaHora = new Date(fechaHoraString);
    fechaHora.setHours(fechaHora.getHours() - 6);

    await prisma.asistencia.updateMany({
      where: {
        cedula: cedulaEmpleado.cedula,
        fecha: fechaHora.toISOString(),
      },
      data: {
        hora_salida: fechaHora.toISOString(),
      },
    });

    return { message: "Salida registrada" };
  } catch (error) {
    console.error("Error executing query", error);
    return { error: "Error executing query" };
  } finally {
    await prisma.$disconnect();
  }
});
