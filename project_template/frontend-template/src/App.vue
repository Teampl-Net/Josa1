<template>
  <div id="#app">
    <h1>{{ message }}</h1>
    <router-link to="/">HOME</router-link> |  <!-- "welcome" 페이지로 이동 -->
    <router-link to="/welcome">안녕하슈</router-link> |  <!-- "welcome" 페이지로 이동 -->
    <router-view></router-view>  
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

// Composition API 사용
const message = ref('Welcome to Vue 3 + Vite');
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
</style>
