<template>
  <div class="sidebar">
    <div class="category">
      <div class="business">
        <p class="fontBody">사업 목록</p>
        <button class="edit">편집</button>
      </div>
      <ul class="menu">
        <li v-for="category in dummyData" :key="category.name">
          <span @click="toggleCategory(category.name)">{{ category.name }}</span>
          <ul v-if="isOpenCategory(category.name)">
            <li
              v-for="subCategory in category.subCategories"
              :key="subCategory.name"
              @click="setSelectedSubCategory(subCategory.name)"
              class="subcategory-item"
            >
              {{ subCategory.name }}
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 목업데이터
const dummyData = [
  {
    name: '전체',
    subCategories: [],
  },
  {
    name: '고시원',
    subCategories: [],
  },
  {
    name: '반지하',
    subCategories: [
      { name: '24년 반지하 전수 조사' },
      { name: '24년 반지하 침수 방지 실측 조사' },
      { name: '24년 반지하 침수 방지 설치 조사' },
    ],
  },
  {
    name: '옥탑',
    subCategories: [],
  },
  {
    name: '판자촌',
    subCategories: [],
  },
];

const openCategories = ref(dummyData.reduce((acc, category) => {
  acc[category.name] = false;
  return acc;
}, {}));

const selectedSubCategory = ref(null);

const setSelectedSubCategory = (name) => {
  console.log(`Selected subcategory: ${name}`);
  selectedSubCategory.value = name;
};

const toggleCategory = (name) => {
  openCategories.value[name] = !openCategories.value[name];
};

const isOpenCategory = (name) => openCategories.value[name];
</script>

<style scoped>
.sidebar {
  width: 260px;
  background-color: #f4f6f7;
  padding: 20px;
  padding-top: 40px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.category {
  margin-bottom: 20px;
}

.business {
  display: flex;
}

.fontBody {
  position: absolute;
  font-size: 18px;
  font-weight: bold;
}

.edit {
  margin-left: 70%;
  background-color: transparent; 
  border: none;
  margin-right: 1rem;
  cursor: pointer;
  color: #495057;
  border-bottom: 1px solid #e0e0e0;
  transition: color 0.3s ease;
}

.menu {
  list-style-type: none;
  padding-left: 0;
  padding-top: 10px;
}

.menu > li > span {
  cursor: pointer;
  padding: 10px;
  display: block;
  border-bottom: 1px solid #ddd;
}

.menu > li > span:hover {
  background-color: #e0e0e0;
}

.menu ul {
  list-style-type: none;
  padding-left: 20px;
}

.menu ul li {
  padding: 8px;
  cursor: pointer;
  font-size: 13px;
  color: #555;
}

.menu ul li:hover {
  background-color: #e0e0e0;
}
</style>
