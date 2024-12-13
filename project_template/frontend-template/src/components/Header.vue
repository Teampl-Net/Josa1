<template>
  <div class="commonHeader">
    <div class="commonHeaderContent">
      <h2><a href="#" class="logo"><img alt="Vue logo" src="../assets/logo.svg" width="20"></a> {{ message }}</h2>
      <ul class="menu">
        <li><router-link to="/josaTargetList">조사업무</router-link> | </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const message = ref('조사데이터 관리시스템');
</script>

<style scoped>
.commonHeader {
  position: fixed; /* Change from relative to fixed */
  top: 0; /* Align to the top of the page */
  left: 0; /* Ensure it spans the full width */
  width: 100%; /* Full width */
  height: 50px;
  box-shadow: 0 0px 30px rgba(0, 0, 0, 0.1);
  line-height: 48px;
  padding: 0 10px;
  background-color: #ffffff;
  z-index: 1000; /* High z-index to ensure it stays on top */
}

.commonHeaderContent {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  line-height: 50px;
  position: relative;
}

h1 {
  position: absolute;
  top: 0;
  left: 0; /* Adjusted to align with the left side */
}

ul.menu {
  position: absolute;
  top: 0; /* Aligned with the top */
  right: 0; /* Aligned with the right side */
  margin: 0;
  padding: 0;
}

ul.menu li {
  display: inline-block;
  padding: 0 20px;
  list-style: none;
}

a {
  text-decoration: none;
  color: #333;
}
</style>