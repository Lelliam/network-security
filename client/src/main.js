// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Resource from 'vue-resource'
import echarts from 'echarts'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';

Vue.config.productionTip = false;

Vue.use(Resource);
Vue.prototype.$echarts = echarts;
Vue.use(ViewUI);


Vue.http.options.root = 'http://localhost:3000/';
Vue.http.options.emulateJson = true;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  //router,
  components: { App },
  template: '<App/>'
});
