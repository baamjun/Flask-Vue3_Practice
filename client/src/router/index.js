import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import searchView from '../views/searchView.vue'
import hello from '../components/HelloWorld.vue'
import graph from '../views/graph.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: searchView
    },
    {
      path: '/hello',
      name: 'hello',
      component: hello
    },
    {
      path: '/graph',
      name: 'graph',
      component: graph
    },
  ]
})

export default router
