import Vue from 'vue'
import Router from 'vue-router'
import VisualizationIndex from '@/components/VisualizationIndex'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Visualization',
      component: VisualizationIndex
    }
  ]
})
