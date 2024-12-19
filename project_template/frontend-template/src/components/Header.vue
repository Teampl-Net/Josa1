<template>
  <div class="commonHeader">
    <div class="commonHeaderContent">
      <h2><a href="#" class="logo"><img alt="Vue logo" src="../assets/logo.svg" width="20"></a> {{ message }}</h2>
      <ul class="menu">
        <li><router-link to="/josaTargetList">조사자</router-link>  </li>
        <li><router-link to="/josaTargetList">조사대상</router-link>  </li>
        <li><router-link to="/josaTargetList">조사업무</router-link> </li>
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
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  box-shadow: 0 0px 30px rgba(0, 0, 0, 0.1);
  line-height: 48px;
  padding: 0 10px;
  background-color: #ffffff;
  z-index: 1000;
}

.commonHeaderContent {
  width: 100%;
  max-width: 1280px;
  line-height: 50px;
  position: relative;
  display: flex;
  align-items: center;
}

h2 {
  margin: 0;
  padding: 0;
}

ul.menu {
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
