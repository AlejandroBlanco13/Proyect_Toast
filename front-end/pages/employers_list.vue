<script setup lang="ts">

import { ref } from 'vue'

const tableConfig = {
  wrapper: 'relative overflow-x-auto bg-white border border-gray-300', // Fondo blanco y borde gris claro para el contenedor
  base: 'min-w-full table-fixed border-collapse', // Border-collapse para compartir bordes
  divide: 'divide-y divide-gray-200 dark:divide-gray-700', // Líneas divisorias grises
  thead: 'relative bg-gray-800 border-b border-gray-300', // Fondo oscuro para el encabezado con borde inferior gris claro
  tbody: 'divide-y divide-gray-200 dark:divide-gray-800', // Líneas divisorias grises en el cuerpo
  caption: 'sr-only',
  tr: {
    base: 'border-b border-gray-200 dark:border-gray-700', // Borde inferior gris claro para cada fila
    selected: 'bg-gray-100 dark:bg-gray-800/50', // Fondo gris claro para filas seleccionadas
    active: 'hover:bg-gray-100 dark:hover:bg-gray-800/50 cursor-pointer', // Fondo gris claro al pasar el cursor
  },
  th: {
    base: 'text-left rtl:text-right border border-gray-300', // Borde alrededor de las celdas del encabezado
    padding: 'px-4 py-3.5',
    color: 'text-white', // Texto blanco para el encabezado
    font: 'font-semibold',
    size: 'text-sm',
    bg: 'bg-gray-800' // Fondo gris oscuro para el encabezado
  },
  td: {
    base: 'whitespace-nowrap border border-gray-300', // Borde alrededor de las celdas del cuerpo
    padding: 'px-4 py-4',
    color: 'text-gray-900 dark:text-gray-400', // Texto gris oscuro para el cuerpo
    font: '',
    size: 'text-sm',
    bg: 'bg-white' // Fondo blanco para las celdas del cuerpo
  },
  checkbox: {
    padding: 'ps-4',
  },
  loadingState: {
    wrapper: 'flex flex-col items-center justify-center flex-1 px-6 py-14 sm:px-14',
    label: 'text-sm text-center text-gray-900 dark:text-white',
    icon: 'w-6 h-6 mx-auto text-gray-400 dark:text-gray-500 mb-4 animate-spin',
  },
  emptyState: {
    wrapper: 'flex flex-col items-center justify-center flex-1 px-6 py-14 sm:px-14',
    label: 'text-sm text-center text-gray-900 dark:text-white',
    icon: 'w-6 h-6 mx-auto text-gray-400 dark:text-gray-500 mb-4',
  },
  progress: {
    wrapper: 'absolute inset-x-0 -bottom-[0.5px] p-0',
  },
  default: {
    sortAscIcon: 'i-heroicons-bars-arrow-up-20-solid',
    sortDescIcon: 'i-heroicons-bars-arrow-down-20-solid',
    sortButton: {
      icon: 'i-heroicons-arrows-up-down-20-solid',
      trailing: true,
      square: true,
      color: 'gray',
      variant: 'ghost',
      class: '-m-1.5',
    },
    checkbox: {
      color: 'primary',
    },
    progress: {
      color: 'primary',
      animation: 'carousel',
    },
    loadingState: {
      icon: 'i-heroicons-arrow-path-20-solid',
      label: 'Loading...',
    },
    emptyState: {
      icon: 'i-heroicons-circle-stack-20-solid',
      label: 'No items.',
    },
  },
};



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
  class: string
}


const registrar_entrada = async() => {
  
  const res = await fetch('http://localhost:5000/registrar_entrada', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      cedula: cedulaInput.value,
      fecha: new Date().toLocaleDateString('en-US', { month: '2-digit', day: '2-digit', year: 'numeric' }),
      hora_entrada: new Date().toLocaleTimeString(),
    })
  })
  const data = await res.json()
  console.log(data)
  if (!data.error) {
    await obtener_empleados()
    toast.add({
      title: 'Bienvenido! '+ empleados.value[empleados.value.length - 1].nombre,
    })
    errorCedula.value = 'blue'
    isOpen.value = false
    cedulaInput.value = ''
  }
  else{
    errorCedula.value = 'red'
  }
  
}

const obtener_empleados = async() => {
  
  try{
    const res = await fetch('http://localhost:5000/consultar_empleados_hoy')
    const data = await res.json()

    data.forEach((empleado: empleado) => {
      if (empleado.hora_salida !== 'En trabajo'){     
        empleado.class = 'bg-green-200 '
      }
      else{
        empleado.class = 'bg-red-200'
      }
    })
    empleados.value = data
    console.log(data)
    cargando.value = false
    
  } catch (error) {
    console.log(error)
  }

}



const marcar_salida = async(row: empleado) => {

  cargando.value = true
  console.log(row)
  const res = await fetch('http://localhost:5000/marcar_salida', {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      cedula: row.cedula,
      fecha: new Date().toLocaleDateString('en-US', { month: '2-digit', day: '2-digit', year: 'numeric' }),
      hora_salida: new Date().toLocaleTimeString()
    })
  })
  const data = await res.json()
  console.log(data)
  obtener_empleados()
  cargando.value = false
}

const cargando = ref(true)
const isOpen = ref(false)
const cedulaInput = ref('')
const toast = useToast()
const errorCedula = ref('blue')

onMounted(() => {
  obtener_empleados()
})


</script>

<template>
  <UTable class="mt-10 mx-14" :rows="empleados" :columns="columns" :loading=cargando
    :loading-state="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Cargando...' }"
    :ui = "tableConfig">
    <template #name-data="{ _ }">
    </template>

    <template #marcar_salida-data="{ row }">

      <UButton color="indigo" @click="marcar_salida(row)" :disabled="row.hora_salida !== 'En trabajo'">Marcar</UButton>
    </template>
  </UTable>

  <div class="flex justify-center mt-24">
    <UButton label="Registrar entrada" @click="isOpen = true" color="blue" />

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
            <UFormGroup v-slot="{ error }" label="Email" :error="errorCedula === 'red' && 'Cédula no encontrada'">
              <UInput placeholder="Ej: 208490685" :color="errorCedula" id="cedula" v-model="cedulaInput"
                :trailing-icon="error ? 'i-heroicons-exclamation-triangle-20-solid' : undefined" />
            </UFormGroup>
          </div>
        </template>
        <div class="flex justify-center">
          <UButton label="Confirmar" color="blue" @click="registrar_entrada" />
        </div>

      </UCard>
    </UModal>
  </div>
</template>

