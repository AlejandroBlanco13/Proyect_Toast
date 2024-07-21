<script setup lang="ts">
const value = ref('')
</script>

<template>
  <div class="flex justify-center items-start min-h-screen mt-20"> <!-- Contenedor centrado con margen superior -->
    <UFormGroup label="Formulario de Registro" hint="Opcional">
      <div class="space-y-4"> <!-- Espacio entre los campos -->
        <div class="relative w-64">
          <input type="text" placeholder="Nombre" class="pl-10 border rounded-md py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline w-full" />
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 18.364A4 4 0 117.464 16 3.975 3.975 0 015.12 18.364zM17 10.001v5.042a2.986 2.986 0 01-.879 2.121 2.986 2.986 0 01-2.121.879H6.121a2.986 2.986 0 01-2.121-.879A2.986 2.986 0 013.121 15V10a2.986 2.986 0 01.879-2.121A2.986 2.986 0 016.121 7h8.879a2.986 2.986 0 012.121.879A2.986 2.986 0 0117 10z" />
            </svg>
          </div>
        </div>
        <div class="relative w-64">
          <input type="text" placeholder="Apellidos" class="pl-10 border rounded-md py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline w-full" />
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 18.364A4 4 0 117.464 16 3.975 3.975 0 015.12 18.364zM17 10.001v5.042a2.986 2.986 0 01-.879 2.121 2.986 2.986 0 01-2.121.879H6.121a2.986 2.986 0 01-2.121-.879A2.986 2.986 0 013.121 15V10a2.986 2.986 0 01.879-2.121A2.986 2.986 0 016.121 7h8.879a2.986 2.986 0 012.121.879A2.986 2.986 0 0117 10z" />
            </svg>
          </div>
        </div>
        <div class="relative w-64">
          <input type="text" placeholder="Número de Teléfono" class="pl-10 border rounded-md py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline w-full" />
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 18.364A4 4 0 117.464 16 3.975 3.975 0 015.12 18.364zM17 10.001v5.042a2.986 2.986 0 01-.879 2.121 2.986 2.986 0 01-2.121.879H6.121a2.986 2.986 0 01-2.121-.879A2.986 2.986 0 013.121 15V10a2.986 2.986 0 01.879-2.121A2.986 2.986 0 016.121 7h8.879a2.986 2.986 0 012.121.879A2.986 2.986 0 0117 10z" />
            </svg>
          </div>
        </div>
        <div class="relative w-64">
          <input type="text" placeholder="Correo" class="pl-10 border rounded-md py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline w-full" />
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 18.364A4 4 0 117.464 16 3.975 3.975 0 015.12 18.364zM17 10.001v5.042a2.986 2.986 0 01-.879 2.121 2.986 2.986 0 01-2.121.879H6.121a2.986 2.986 0 01-2.121-.879A2.986 2.986 0 013.121 15V10a2.986 2.986 0 01.879-2.121A2.986 2.986 0 016.121 7h8.879a2.986 2.986 0 012.121.879A2.986 2.986 0 0117 10z" />
            </svg>
          </div>
        </div>
        <div class="relative w-64">
          <input type="text" placeholder="Cedula" class="pl-10 border rounded-md py-2 px-3 text-gray-700 focus:outline-none focus:shadow-outline w-full" />
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 18.364A4 4 0 117.464 16 3.975 3.975 0 015.12 18.364zM17 10.001v5.042a2.986 2.986 0 01-.879 2.121 2.986 2.986 0 01-2.121.879H6.121a2.986 2.986 0 01-2.121-.879A2.986 2.986 0 013.121 15V10a2.986 2.986 0 01.879-2.121A2.986 2.986 0 016.121 7h8.879a2.986 2.986 0 012.121.879A2.986 2.986 0 0117 10z" />
            </svg>
          </div>
        </div>
      </div>
    </UFormGroup>
  </div>
</template>

