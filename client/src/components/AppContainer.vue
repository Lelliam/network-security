<template>

  <div id="main_container">
    <Card id="card" :style="{margin: '80px 10px 0 10px', background: '#fff', minHeight: '89vh'}">
      <div id="container">
        <AppMain></AppMain>
        <AppTimeLine></AppTimeLine>
        <AppInfo01></AppInfo01>
        <AppInfo02></AppInfo02>
        <AppInfo03></AppInfo03>
        <AppInfo04></AppInfo04>
        <AppInfo05></AppInfo05>
        <AppInfo06></AppInfo06>
      </div>
    </Card>
  </div>
</template>

<script>

    import AppMain from './AppMain';
    import AppTimeLine from "./AppTimeLine";
    import AppInfo01 from "./AppInfo01";
    import AppInfo02 from "./AppInfo02";
    import AppInfo03 from "./AppInfo03";
    import AppInfo04 from "./AppInfo04";
    import AppInfo05 from "./AppInfo05";
    import AppInfo06 from "./AppInfo06";

    export default {
        name: "AppContainer",
        mounted(){
        },
        methods:{
        },
        components:{
            AppMain,
            AppTimeLine,
            AppInfo01,
            AppInfo02,
            AppInfo03,
            AppInfo04,
            AppInfo05,
            AppInfo06
        }
    }
</script>

<style scoped>
  #main_container{
    position: relative;
    width: 100%;
    height: 100%;
  }

  #container{
    position: absolute;
    width: 100%;
    height: 100%;
  }
</style>
