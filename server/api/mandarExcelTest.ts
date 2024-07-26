
import nodemailer from "nodemailer";
import dotenv from "dotenv";


dotenv.config();

export default defineEventHandler(async () => {
  // Configura el transporte de nodemailer
  const transporter = nodemailer.createTransport({
    service: "gmail", // Puedes usar otros servicios como 'hotmail', 'yahoo', etc.
    auth: {
      user: process.env.correo, // Reemplaza con tu correo
      pass: process.env.contrasena, // Reemplaza con tu contraseña
    },
  });

  // Configura los detalles del correo
  const mailOptions = {
    from: process.env.correo, // Reemplaza con tu correo
    to: "noni45100@hotmail.com", // Reemplaza con el correo del destinatario
    subject: "Tilines insanos",
    text: "Contenido del correo en texto plano",
    html: "<p>Contenido del correo en HTML</p>", // Opcional: contenido en HTML
  };

  try {
    // Envía el correo
    const info = await transporter.sendMail(mailOptions);
    console.log("Correo enviado: " + info.response);
  } catch (error) {
    console.error("Error al enviar el correo: " + error);
  }
});