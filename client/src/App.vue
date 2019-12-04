<template>
  <div id="app">
    <AppMap></AppMap>
    <AppTimeLine></AppTimeLine>
    <AppRadar></AppRadar>
    <AppCalendar></AppCalendar>
  </div>
</template>

<script>
    import AppMap from "./components/AppMap";
    import AppTimeLine from "./components/AppTimeLine";
    import AppRadar from "./components/AppRadar";
    import AppCalendar from "./components/AppCalendar";
    export default {
        name: 'App',
        components:{
            AppMap,
            AppTimeLine,
            AppRadar,
            AppCalendar
        }
    }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    position: fixed;
    width: 100%;
    height: 100%;
  }
</style>
