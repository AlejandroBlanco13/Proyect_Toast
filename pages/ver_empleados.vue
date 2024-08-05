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
            <th class="py-2 px-4 border-b">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(employee, index) in employees" :key="index">
            <td class="py-2 px-4 border-b">{{ employee.nombre }}</td>
            <td class="py-2 px-4 border-b">{{ employee.apellidos }}</td>
            <td class="py-2 px-4 border-b">{{ employee.telefono }}</td>
            <td class="py-2 px-4 border-b">{{ employee.correo }}</td>
            <td class="py-2 px-4 border-b">{{ employee.cedula }}</td>
            <td class="py-2 px-4 border-b">
              <button @click="editarEmpleado(employee.cedula)" class="text-blue-500 hover:text-blue-700 mr-4">Editar Empleado</button>
              <button @click="eliminarEmpleado(employee.cedula)" class="text-red-500 hover:text-red-700">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4 text-center">
        <button @click="agregarEmpleado" class="border border-gray-900 rounded-md py-2 px-4 text-white bg-gray-900 hover:bg-gray-700">Agregar Empleado</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const employees = ref([]);

// Función para obtener los empleados desde el backend
async function fetchEmployees() {
  try {
    const response = await axios.get('http://localhost:3000/api/empleados'); // Cambia la URL según tu backend
    employees.value = response.data; // Asumiendo que la respuesta es un array de empleados
  } catch (error) {
    console.error('Error al obtener empleados:', error);
  }
}

// Llama a fetchEmployees cuando el componente se monta
onMounted(() => {
  fetchEmployees();
});

// Función para editar un empleado
function editarEmpleado(cedula) {
  console.log('Editar empleado con cédula:', cedula);
}

// Función para eliminar un empleado
function eliminarEmpleado(cedula) {
  console.log('Eliminar empleado con cédula:', cedula);
}

// Función para agregar un empleado
function agregarEmpleado() {
  console.log('Agregar nuevo empleado');
}
</script>

<style scoped>
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