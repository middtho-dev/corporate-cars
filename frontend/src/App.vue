<template>
  <div class="app dark">
    <h1>Календарь бронирования</h1>
    <Calendar />
  </div>
</template>

<script setup>
import Calendar from './components/Calendar.vue'
</script>

<style>
body {
  margin: 0;
  background: #121212;
  color: white;
  font-family: Arial, sans-serif;
}
.app {
  padding: 20px;
}
</style>
