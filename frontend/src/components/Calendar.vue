<template>
  <div>
    <div v-if="loading">
      <Loader />
    </div>
    <div v-else>
      <div v-for="car in cars" :key="car.id" class="car-card">
        <h3>{{ car.name }}</h3>
        <button @click="book(car.id)">Забронировать</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Loader from './Loader.vue'

const cars = ref([])
const loading = ref(true)

async function fetchCars() {
  loading.value = true
  const res = await fetch('/api/cars/')
  cars.value = await res.json()
  loading.value = false
}

async function book(carId) {
  const user = prompt('Ваше имя?')
  const start_time = prompt('Когда забираете машину? (2025-05-01T10:00)')
  const end_time = prompt('Когда вернете машину? (2025-05-01T18:00)')
  
  await fetch('/api/book/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user, car: carId, start_time, end_time })
  })

  alert('Бронирование успешно создано!')
}

onMounted(fetchCars)
</script>

<style scoped>
.car-card {
  margin-bottom: 20px;
  padding: 15px;
  background: #1f1f1f;
  border-radius: 8px;
}
button {
  margin-top: 10px;
  background: #6200ee;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 6px;
}
button:hover {
  background: #3700b3;
}
</style>
