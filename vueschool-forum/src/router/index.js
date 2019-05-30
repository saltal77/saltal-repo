import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/PageHome'
import PageThreadShow from '@/pages/PageThreadShow'
import PageNotFound from '@/pages/NotFound'
import Forum from '@/pages/PageForum'
import Category from '@/pages/PageCategory'
import Profile from '@/pages/PageProfile'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/forum/:id',
      name: 'Forum',
      component: Forum,
      props: true,
    },
    {
      path: '/category/:id',
      name: 'Category',
      component: Category,
      props: true,
    },
    {
      path: '/thread/:id',
      name: 'PageThreadShow',
      component: PageThreadShow,
      props: true,
    },
    {
      path: '/me',
      name: 'Profile',
      component: Profile,
      props: true,
    },
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound,
      //redirect: { name: 'Home'}
    },
  ],
  mode: 'history',
})
