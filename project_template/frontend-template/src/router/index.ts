import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import HellowWorld from '../components/HelloWorld.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/welcome',
    name: 'welcome',
    component: HellowWorld
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
