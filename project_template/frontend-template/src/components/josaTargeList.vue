<template>
  <div class="josaTargetList-container">
    <div class="josaTargetList-message">
      <p class="greeting">조사 업무 목록</p>
      <hr/>
    </div>
    <hr/>
    <div class="additional-info">
      <p>우리 팀에 새로운 에너지가 들어와서 너무 기쁩니다!</p>
      <p>앞으로 함께 성장하고 멋진 일들을 만들어가요.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
/* 전체 컨테이너 스타일 */
.josaTargetList-container {
  display: block; /* Change from flex to block */
  font-family: 'Arial', sans-serif;
  padding: 2rem;
  text-align: left; /* Change from center to left */
  width: 100%; /* Ensure full width */
}

.josaTargetList-message {
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  width: 100%; /* Ensure full width */
}

.greeting {
  font-size: 1.5rem;
  color: #343a40;
  font-weight: bold;
}

.sub-text {
  font-size: 1.2rem;
  color: #343a40;
  margin-top: 0.5rem;
}

.additional-info {
  font-size: 1.1rem;
  color: #495057;
  line-height: 1.6;
  width: 100%; /* Ensure full width */
}

@media (max-width: 768px) {
  .josaTargetList-container {
    padding: 1rem;
  }
  
  .greeting {
    font-size: 1.6rem;
  }
  
  .sub-text {
    font-size: 1rem;
  }
  
  .additional-info {
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .josaTargetList-container {
    padding: 0.5rem;
  }
  
  .greeting {
    font-size: 1.4rem;
  }
  
  .sub-text {
    font-size: 0.9rem;
  }
  
  .additional-info {
    font-size: 0.9rem;
  }
}
</style>
