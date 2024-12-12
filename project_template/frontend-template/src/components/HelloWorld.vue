<template>
  <div class="welcome-container">
    <div class="welcome-message">
      <h2 class="greeting">🎉 불금 화이팅!!! 🎉</h2>
      <p class="sub-text">수빈님 김재현 님 오늘도 화이팅!</p>
    </div>
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
.welcome-container {
  font-family: 'Arial', sans-serif;
  background-color: #f8f9fa;
  padding: 2rem;
  text-align: center;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.welcome-message {
  background-color: #ffffff;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.greeting {
  font-size: 2rem;
  color: #007bff;
  font-weight: bold;
  margin: 0;
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
}

@media (max-width: 768px) {
  .welcome-container {
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
  .welcome-container {
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
