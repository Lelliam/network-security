import Vue from 'vue'
import Router from 'vue-router'

import AppContainer from "../components/AppContainer";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AppContainer',
      component: AppContainer
    }
  ]
})
