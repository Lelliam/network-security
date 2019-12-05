<template>
  <div id="layout">
    <div id="slide-mask" @mouseover="sliderStatus=true"></div>
    <Drawer title="功能选择" placement="left" :closable="sliderStatus" v-model="sliderStatus">
      <Menu active-name="1-2" theme="light" width="auto">
        <router-link  to="/function01" >
          <MenuItem name="1-1">
            <Icon type="ios-navigate"></Icon>
            <span>测试功能</span>
          </MenuItem>
        </router-link>
        <router-link  to="/function02" >
          <MenuItem name="1-2">
            <Icon type="ios-search"></Icon>
            <span>测试功能</span>
          </MenuItem>
        </router-link>
        <router-link  to="/function03" >
          <MenuItem name="1-3">
            <Icon type="ios-settings"></Icon>
            <span>测试功能</span>
          </MenuItem>
        </router-link>
        <router-link  to="/function04" >
          <MenuItem name="1-4">
            <Icon type="ios-settings"></Icon>
            <span>测试功能</span>
          </MenuItem>
        </router-link>
        <router-link  to="/function05" >
          <MenuItem name="1-5">
            <Icon type="ios-settings"></Icon>
            <span>测试功能</span>
          </MenuItem>
        </router-link>
      </Menu>
    </Drawer>
    <Layout>
      <Header :style="{position: 'fixed', width: '100%'}">
        <h2 class="layout-title">Data&nbsp;&nbsp;&nbsp;Visualization&nbsp;&nbsp;&nbsp;System</h2>
      </Header>
      <Content>
        <router-view></router-view>
        <!--        <AppContainer></AppContainer>-->
      </Content>
      <Footer class="layout-footer-center">2019-2020 &copy; DATA-VIS</Footer>
    </Layout>
  </div>
</template>

<script>
    import AppContainer from "./AppContainer";
    import router from '../router/index'
    export default {
        name: "APPLayout",
        data(){
            return {
                sliderStatus:false
            }
        },
        methods:{
        },
        components: {
            AppContainer
        }
        ,router
    }
</script>

<style scoped>

  @import "../common/fonts/font.css";

  a{
    color:#666
  }

  .ivu-menu-light.ivu-menu-vertical
  .ivu-menu-item-active:not(.ivu-menu-submenu):after {
    background-color: #515a6e;
  }

  .layout{
    background: #f5f7f9;
    position: relative;
    overflow: hidden;
  }
  .layout-title{
    font-family: Monoton;
    height: 60px;
    line-height: 60px;
    color: #FFFFFF;
    font-size: 28px;
    font-weight: 100;
  }
  .layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
  }
  .menu-icon{
    transition: all .3s;
  }
  .rotate-icon{
    transform: rotate(-90deg);
  }

  .menu-item span{
    display: inline-block;
    overflow: hidden;
    width: 69px;
    text-overflow: ellipsis;
    white-space: nowrap;
    vertical-align: bottom;
    transition: width .2s ease .2s;
  }
  .menu-item i{
    transform: translateX(0px);
    transition: font-size .2s ease, transform .2s ease;
    vertical-align: middle;
    font-size: 16px;
  }

  .collapsed-menu span{
    width: 0;
    transition: width .2s ease;
  }
  .collapsed-menu i{
    transform: translateX(5px);
    transition: font-size .2s ease .2s, transform .2s ease .2s;
    vertical-align: middle;
    font-size: 32px;
  }
  .ivu-breadcrumb{
    text-align: left;
  }
  #slide-mask{
    position: absolute;
    z-index: 999;
    width: 10px;
    height: 100%;
  }
  .ivu-layout-footer{
    padding: 10px 10px;
  }

</style>
