<script setup lang="ts">

import { ref } from 'vue'

const columns = [{
  key: 'cedula',
  label: 'Cedula'
  }, {
  key: 'nombre',
  label: 'Nombre'
}, {
  key: 'hora_entrada',
  label: 'Hora de entrada'
}, {
  key: 'hora_salida',
  label: 'Hora de salida'
}, {
  key: 'marcar_salida',
  label: 'Marcar salida'
}]

const empleados = ref<empleado[]>([
  ]);

interface empleado {
  cedula: number
  nombre: string
  hora_entrada: string
  hora_salida: string
}

const imprimir = (row : empleado) => {
  console.log('hola')
  console.log(row)
}

const registrar_entrada = async() => {
  
  const res = await fetch('http://localhost:5000/test', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      cedula: '123456789',
      fecha: '17/10/2021',
      hora_entrada: new Date().toLocaleTimeString(),
      hora_salida: new Date().toLocaleTimeString()
    })
  })
  

}

const obtener_empleados = async() => {
  
  try{
    const res = await fetch('http://localhost:5000/consultar_empleados_hoy')
    const data = await res.json()
    empleados.value = data
    console.log(data)
    cargando.value = false
    
  } catch (error) {
    console.log(error)
  }
    


}




const cargando = ref(true)

const isOpen = ref(false)

onMounted(() => {
  obtener_empleados()
})


</script>

<template>
  <UTable class="mt-10 ml-14" :rows="empleados" :columns="columns" :loading=cargando
    :loading-state="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Cargando...' }">
    <template #name-data="{ _ }">
    </template>

    <template #marcar_salida-data="{ row }">
      <UButton color="indigo" @click="imprimir(row)">Marcar</UButton>
    </template>
  </UTable>

  <div class="flex justify-center mt-24">
    <UButton label="Registrar entrada" @click="isOpen = true" color="red" />

    <UModal v-model="isOpen" prevent-close>
      <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <div class="flex items-center justify-between">
            <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-black ml-28">
              Ingrese su numero de cédula
            </h3>
            <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1"
              @click="isOpen = false" />
          </div>

          <div class="mt-10">
            <UInput placeholder="Ej: 208490685" color="red" />
          </div>
        </template>
        <div class="flex justify-center">
          <UButton label="Confirmar" color="red" @click="registrar_entrada" />
        </div>
      </UCard>
    </UModal>
  </div>
</template>

