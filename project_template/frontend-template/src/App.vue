<template>
  <div id="#app" class="app-container">
    <div class="main-content">
      <SideBar2 class="sidebar" />
      <div class="content-area">
        <Header />
        <JosaTargeList />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Header from './components/Header.vue';
import JosaTargeList from './components/josaTargeList.vue';
import SideBar from './components/sideBar.vue';
import SideBar2 from './components/sideBar2.vue';

// Composition API 사용
const message = ref('조사데이터 관리시스템');
</script>

<style scoped>
#app{
  padding: 0;

}

.app-container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.main-content {
  display: flex;
  height: 100vh;
  left: 0;
}

.sidebar {
  width: 30%;
  background-color: #f0f0f0;
  border-right: 1px solid #ddd;
}

.content-area {
  flex-grow: 1;
  padding: 20px;
  overflow: auto;
}
</style>