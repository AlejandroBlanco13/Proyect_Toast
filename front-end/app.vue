<script setup lang="ts">




</script>

<template>
  <div>
    <header class="bg-gray-800 p-4">
      <nav class="container mx-auto flex justify-between items-center">
        <div class="text-white text-xl">TOAST CAFÉ</div>
        <ul class="flex space-x-24">
          <li>
            <NuxtLink to="/employers_list" class="text-white hover:underline">Ingreso</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/" class="text-white hover:underline">Lista Empleados</NuxtLink>
          </li>
          <li>
            <NuxtLink to="/" class="text-white hover:underline">Contact</NuxtLink>
          </li>
        </ul>
      </nav>
    </header>
    <NuxtPage />
    <UNotifications />
  </div>
</template>