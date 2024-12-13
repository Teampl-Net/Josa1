import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import HellowWorld from '../components/HelloWorld.vue';
import josaTargetList from '../components/josaTargeList.vue';

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
  ,
  {
    path: '/josaTargetList',
    name: 'josaTargetList',
    component: josaTargetList
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
