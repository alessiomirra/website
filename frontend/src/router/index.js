import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/store', 
    name: 'store-page', 
    component: () => import('../views/StorePage.vue')
  }, 
  {
    path: '/about', 
    name: 'about-page', 
    component: () => import('../views/AboutPage.vue')
  }, 
  {
    path: '/store/:slug', 
    name: 'car-details', 
    component: () => import('../views/CarDetails.vue')
  },
  {
    path: '/contact', 
    name: 'contact', 
    component: () => import('../views/ContactPage.vue')
  }, 
  {
    path: '/unsubscribe', 
    name: 'unsubscribe', 
    component: () => import('../views/Unsubscribe.vue')
  },
  {
    path: '/error', 
    name: 'error', 
    component: () => import('../views/Error.vue')
  }, 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  window.scrollTo(0, 0);
  next();
});

export default router
