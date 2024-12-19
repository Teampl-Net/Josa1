<template>
  <div class="josaTargetList-container">
    <div class="josaTargetList-header">
      <div class="header-left">
        <i class="icon-list"></i>
        <span class="business">조사 업무 목록</span>
      </div>
      <div class="header-right">
        <span>조사 업무 관리 > 조사 업무 목록</span>
      </div>
    </div>

    <!-- 탭 필터링 -->
    <div class="josaTargetList-status">
      <div class="status-tabs">
        <button 
          :class="['tab-button', { active: currentStatus === 'ongoing' }]" 
          @click="filterTasks('ongoing')">진행중</button>
        <button 
          :class="['tab-button', { active: currentStatus === 'completed' }]" 
          @click="filterTasks('completed')">완료</button>
        <button 
          :class="['tab-button', { active: currentStatus === 'all' }]" 
          @click="filterTasks('all')">전체</button>
      </div>
      <div class="status-manage">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="업무명 검색"
          class="search-input"
        />
        <button class="add" @click="DialogPortal">업무추가</button>
      </div>
    </div>
    
    <!-- 테이블 구간 -->
    <div class="task-table-container">
      <table class="task-table" v-if="filteredTasks.length > 0">
        <thead>
          <tr>
            <th>No.</th>
            <th>조사업무명</th>
            <th>기간</th>
            <th>대상</th>
            <th>조사자</th>
            <th>할당</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(task, index) in filteredTasks" :key="index">
            <td>{{ task.no }}</td>
            <td>{{ task.name }}</td>
            <td>{{ task.dueDate }}</td>
            <td>{{ task.target }}</td>
            <td>{{ task.charge }}</td>
            <td><a href="#" class="link">{{ task.match }}</a></td>
          </tr>
        </tbody>
      </table>
      <p v-else>데이터를 불러오는 중입니다...</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DialogPortal } from 'radix-vue';
import { ref, onMounted, computed } from 'vue';
const tasks = ref<any[]>([]);

const currentStatus = ref<'all' | 'ongoing' | 'completed'>('all');
const searchQuery = ref(''); // 검색어 상태 추가

// 필터링된 작업
const filteredTasks = computed(() => {
  const statusFiltered = currentStatus.value === 'all'
    ? tasks.value
    : tasks.value.filter(task => task.status === currentStatus.value);

  // 검색어로 추가 필터링
  return statusFiltered.filter(task => 
    task.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

// 목업데이터
const fetchDummyData = () => {
  setTimeout(() => {
    tasks.value = [
      { no: 1, name: '반지하 침수 방지 실측 조사', dueDate: '2024-12-15', target: '20000 / 28000건 (71%)', charge: '150명', match: '확인', status: 'ongoing' },
      { no: 2, name: '반지하 전수 조사', dueDate: '2025-01-10', target: '100000 / 200000건 (50%)', charge: '200명', match: '확인', status: 'completed' },
      { no: 3, name: '반지하 침수 방지 설치 조사', dueDate: '2025-02-01', target: '12000 / 15000건 (80%)', charge: '100명', match: '확인', status: 'ongoing' }
    ];
    filterTasks(currentStatus.value); 
  }, 1000); 
};

const filterTasks = (status: 'all' | 'ongoing' | 'completed') => {
  currentStatus.value = status;
};

onMounted(() => {
  fetchDummyData();
});
</script>

<style scoped>
/* 컨테이너 스타일 */
.josaTargetList-container {
  font-family: 'Arial', sans-serif;
  padding: 2rem;
}

.josaTargetList-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  font-size: 14px;
  color: #495057;
}

.josaTargetList-header .header-left {
  display: flex;
  align-items: center;
}

.josaTargetList-header .header-left i {
  font-size: 16px;
  margin-right: 0.5rem;
}

.business {
  font-size: 16px;
  font-weight: 700;
}

.josaTargetList-header .header-right {
  font-size: 12px;
  color: #868e96;
}

/* 탭 스타일 */

.josaTargetList-status {
  display: flex;
}

.status-manage {
  display: flex;
  align-items: center;
  margin-left: auto;
}

.search-input {
  padding: 0.5rem;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  font-size: 14px;
  width: 200px;
}

.search-input::placeholder {
  color: #868e96;
}


.status-tabs {
  display: flex;
  border-bottom: 2px solid #e9ecef;
  margin-bottom: 1rem;
}

.tab-button {
  padding: 0.5rem 1.5rem;
  background: none;
  border: none;
  color: #495057;
  cursor: pointer;
  font-size: 14px;
  font-weight: bold;
  transition: color 0.3s, border-bottom 0.3s;
}

.tab-button:hover {
  color: #007bff;
}

.tab-button.active {
  color: #007bff;
  border-bottom: 3px solid #007bff;
}

/* 테이블 스타일 */
.task-table-container {
  overflow-x: auto;
}

.task-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 14px;
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
}

.task-table th, .task-table td {
  padding: 0.75rem;
  border: 1px solid #dee2e6;
}

.task-table th {
  background-color: #e9ecef;
  color: #495057;
}

.task-table tbody tr:nth-child(odd) {
  background-color: #f8f9fa;
}

.task-table .link {
  color: #007bff;
  text-decoration: none;
}

.task-table .link:hover {
  text-decoration: underline;
}

/* 반응형 스타일 */
@media (max-width: 768px) {
  .josaTargetList-container {
    padding: 1rem;
  }

  .status-tabs {
    flex-wrap: wrap;
  }
}
</style>
