<template>
    <div class="flex justify-center items-start min-h-screen mt-20">
      <div class="w-full max-w-4xl">
        <h2 class="text-2xl font-semibold mb-4 text-center text-gray-900">Lista de Empleados</h2>
        <table class="min-w-full bg-white border">
          <thead>
            <tr>
              <th class="py-2 px-4 border-b">Nombre</th>
              <th class="py-2 px-4 border-b">Apellidos</th>
              <th class="py-2 px-4 border-b">Número de Teléfono</th>
              <th class="py-2 px-4 border-b">Correo</th>
              <th class="py-2 px-4 border-b">Cédula</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(employee, index) in employees" :key="index">
              <td class="py-2 px-4 border-b">{{ employee.name }}</td>
              <td class="py-2 px-4 border-b">{{ employee.surname }}</td>
              <td class="py-2 px-4 border-b">{{ employee.phone }}</td>
              <td class="py-2 px-4 border-b">{{ employee.email }}</td>
              <td class="py-2 px-4 border-b">{{ employee.cedula }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // Lista de empleados predefinida
  const employees = ref([
    { name: 'Juan', surname: 'Pérez', phone: '123-456-7890', email: 'juan.perez@example.com', cedula: '12345678' },
    { name: 'María', surname: 'García', phone: '234-567-8901', email: 'maria.garcia@example.com', cedula: '23456789' },
    { name: 'Carlos', surname: 'Rodríguez', phone: '345-678-9012', email: 'carlos.rodriguez@example.com', cedula: '34567890' }
  ]);
  </script>
  
  <style scoped>
  /* Agregar estilos adicionales si es necesario */
  table {
    border-collapse: collapse;
    width: 100%;
  }
  
  th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }
  
  th {
    background-color: #f2f2f2;
  }
  </style>