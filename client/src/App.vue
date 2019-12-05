<template>
  <div id="app">
    <APPLayout></APPLayout>
  </div>
</template>

<script>

    import APPLayout from "./components/APPLayout";

    export default {
        name: 'App',
        components: {
            APPLayout
        }
    }
</script>

<style>
  html,body{
    font-family: "Helvetica Neue";
    overflow: hidden;
    -moz-user-select:none;/*火狐*/
    -webkit-user-select:none;/*webkit浏览器*/
    -ms-user-select:none;/*IE10*/
    -khtml-user-select:none;/*早期浏览器*/
    user-select:none;
  }
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>
