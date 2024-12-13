<template>
  <div id="sidebar">
    <h3>사업목록</h3>
    <ul class="business-list">
      <li>고시원</li>
      <li>반지하</li>
      <li>옥탑방</li>
      <li>판자촌</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const businesses = ref([
  '고시원',
  '반지하',
  '옥탑방',
  '판자촌'
]);

</script>

<style scoped>
.sidebar {
  width: 20%;
  height: 100%;
  background-color: #f0f0f0;
  padding: 20px;
  box-sizing: border-box;
  border-right: 1px solid #ddd;
}

h3 {
  text-align: left;
  color: black;
  margin-bottom: 15px;
  border-bottom: 2px solid #333;
  padding-bottom: 10px;
}

.business-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.business-list li {
  padding: 10px;
  border-bottom: 1px solid #e0e0e0;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.business-list li:hover {
  background-color: #e0e0e0;
}
</style>