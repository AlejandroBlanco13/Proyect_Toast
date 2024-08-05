<style>
  body {
    height: 100vh;
    overflow: hidden;
  }
  
  .scrollable-container {
    height: 100%;
    overflow-y: auto;
  }
</style>

<script setup lang="ts">
const value = ref('')
</script>

<template>
  <div class="scrollable-container">
    <div class="flex justify-center items-start min-h-screen mt-20">
      <UFormGroup label="Formulario de Registro" hint="Obligatorio">
        <div class="space-y-4">
          <div class="relative w-64">
            <input type="text" placeholder="Nombre" class="pl-10 border border-gray-900 rounded-md py-2 px-3 text-white bg-gray-900 focus:outline-none focus:shadow-outline w-full" />
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 18.364A4 4 0 117.464 16 3.975 3.975 0 015.12 18.364zM17 10.001v5.042a2.986 2.986 0 01-.879 2.121 2.986 2.986 0 01-2.121.879H6.121a2.986 2.986 0 01-2.121-.879A2.986 2.986 0 013.121 15V10a2.986 2.986 0 01.879-2.121A2.986 2.986 0 016.121 7h8.879a2.986 2.986 0 012.121.879A2.986 2.986 0 0117 10z" />
              </svg>
            </div>
          </div>
          <div class="relative w-64">
            <input type="text" placeholder="Apellidos" class="pl-10 border border-gray-900 rounded-md py-2 px-3 text-white bg-gray-900 focus:outline-none focus:shadow-outline w-full" />
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 18.364A4 4 0 117.464 16 3.975 3.975 0 015.12 18.364zM17 10.001v5.042a2.986 2.986 0 01-.879 2.121 2.986 2.986 0 01-2.121.879H6.121a2.986 2.986 0 01-2.121-.879A2.986 2.986 0 013.121 15V10a2.986 2.986 0 01.879-2.121A2.986 2.986 0 016.121 7h8.879a2.986 2.986 0 012.121.879A2.986 2.986 0 0117 10z" />
              </svg>
            </div>
          </div>
          <div class="relative w-64">
            <input type="text" placeholder="Número de Teléfono" class="pl-10 border border-gray-900 rounded-md py-2 px-3 text-white bg-gray-900 focus:outline-none focus:shadow-outline w-full" />
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10a1 1 0 011-1h1a1 1 0 000-2H4a1 1 0 100-2h1a1 1 0 000-2H4a1 1 0 00-.707.293A1 1 0 003 4v1a1 1 0 01-2 0V4a1 1 0 012-2h4a1 1 0 010 2H6a1 1 0 000 2h2a1 1 0 010 2H6a1 1 0 000 2h1a1 1 0 010 2H4a1 1 0 01-1-1z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 8h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6a1 1 0 011-1zm4 8a1 1 0 100-2h-2a1 1 0 000 2h2z" />
              </svg>
            </div>
          </div>
          <div class="relative w-64">
            <input type="text" placeholder="Correo" class="pl-10 border border-gray-900 rounded-md py-2 px-3 text-white bg-gray-900 focus:outline-none focus:shadow-outline w-full" />
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 2a4 4 0 00-4 4v2a4 4 0 00-4 4v2a4 4 0 004 4h2a4 4 0 004-4v-2a4 4 0 004-4V6a4 4 0 00-4-4h-2zM6 10V8h2V6h2v2h2v2H8v2H6v-2H4v-2h2z" />
              </svg>
            </div>
          </div>
          <div class="relative w-64">
            <input type="text" placeholder="Cédula" class="pl-10 border border-gray-900 rounded-md py-2 px-3 text-white bg-gray-900 focus:outline-none focus:shadow-outline w-full" />
            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
              <svg class="h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 10v4m0 4v2m4-10v2m0 4v2m4-10v2m0 4v2m4-10v2m0 4v2" />
              </svg>
            </div>
          </div>
          <div class="relative w-64 mt-6">
            <button class="border border-gray-900 rounded-md py-2 px-3 text-white bg-gray-900 focus:outline-none focus:shadow-outline w-full hover:bg-gray-700">
              Agregar Empleado
            </button>
          </div>
        </div>
      </UFormGroup>
    </div>
  </div>
</template>
