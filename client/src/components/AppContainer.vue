<template>
  <div id="container">
    <Card :style="{margin: '80px 10px 0 10px', background: '#fff', minHeight: '89vh'}">
      <Steps direction="vertical">
        <Step title="01" content="">
        </Step>
        <Step title="02" content="">
        </Step>
        <Step title="03" content="">
        </Step>
        <Step title="04" content="">
        </Step>
        <Step title="05" content="">
        </Step>
      </Steps>
    </Card>
  </div>
</template>

<script>
    export default {
        name: "AppContainer",
        mounted(){
        },
        methods:{
        },
        components:{
        }
    }
</script>

<style>
  #container{
    position: relative;
    width: 100%;
    height: 100%;
  }
  .ivu-card-vertical,
  .ivu-card-body,
  .ivu-steps-main {
    text-align: left;
  }
</style>
