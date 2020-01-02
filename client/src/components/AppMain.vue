<template>
  <div id="main"></div>
</template>

<script>
    import '../../static/world'
    import DataManager from "../DataManager/DataManager";
    export default {
        name: "AppMain",
        mounted() {
            this.test();
        },
        methods:{
            test(){
                DataManager.Test().then(res=>{
                    console.log(res.data);
                    this.init_chart(res.data);
                });
            },
            init_chart(data){

                let echarts = this.$echarts;
                let chart = this.$echarts.init(this.$el,'main');

                let graph ={
                    nodes:data.map(d=>{
                        return {
                            "name":d.ip,
                            "value": [d.longitude, d.latitude],
                            "symbolSize": 10,
                            "itemStyle": {
                                "normal": {
                                    "color": "#F58158"
                                }
                            }
                        }
                    }),
                    links: [...Array(50)].map(d=> {
                        let random1 = Math.floor(Math.random()*data.length);
                        let random2 = Math.floor(Math.random()*data.length);
                            return {
                                "fromName": data[random1].ip,
                                "toName": data[random2].ip,
                                "coords": [
                                    [data[random1].longitude, data[random1].latitude],
                                    [data[random2].longitude, data[random2].latitude]
                                ]
                            }
                        }
                    )
                };


                let option = {
                    title: {
                        show:false,
                        text: '全球数字货币交易',
                        left: 'center',
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    //backgroundColor: '#515a6e',
                    legend: {
                        show: false,
                        orient: 'vertical',
                        top: 'bottom',
                        left: 'right',
                        data: ['地点', '线路'],
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    tooltip: {
                        trigger: "item",
                        showDelay: 0,
                        hideDelay: 0,
                        enterable: true,
                        transitionDuration: 0,
                        extraCssText: "z-index:100",
                        formatter: function(params, ticket, callback) {
                            //根据业务自己拓展要显示的内容
                            if(params.seriesType === "effectScatter") {
                                let res = "";
                                let name = params.name;
                                let value = params.value[2];
                                res =
                                    "<span style='color:#fff;'>" +
                                    name +
                                    "</span><br/>交易量：" +
                                    value;
                                return res;
                            }
                        }
                    },
                    geo: {
                        map: 'world',
                        label: {
                            emphasis: {
                                show: false
                            }
                        },
                        zoom: 1.25,
                        roam: true,
                        itemStyle: {
                            normal: {
                                areaColor: '#323c48',
                                borderColor: '#404a59'
                            },
                            emphasis: {
                                areaColor: '#2a333d'
                            }
                        }
                    },
                    series: [{
                        name: '地点',
                        type: 'effectScatter',
                        coordinateSystem: 'geo',
                        zlevel: 2,
                        rippleEffect: {
                            brushType: 'stroke'
                        },
                        symbolSize: 2,
                        showEffectOn: 'render',
                        itemStyle: {
                            normal: {
                                color: '#46bee9'
                            }
                        },
                        data: graph.nodes
                    }, {
                        name: '线路',
                        type: 'lines',
                        coordinateSystem: 'geo',
                        zlevel: 2,
                        large: true,
                        effect: {
                            show: true,
                            period: 8, //箭头指向速度，值越小速度越快
                            trailLength: 0.21, //特效尾迹长度[0,1]值越大，尾迹越长重
                            symbol: "arrow", //箭头图标
                            symbolSize: 5 //图标大小
                        },
                        lineStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0, color: '#58B3CC'
                                }, {
                                    offset: 1, color: '#F58158'
                                }], false),
                                width: .5,
                                opacity: 0.05,
                                curveness: 0.2
                            }
                        },
                        data: graph.links
                    }]
                };

                chart.setOption(option);
            }
        }
    }
</script>

<style scoped>
  #main{
    position: absolute;
    width: 52%;
    height: 69%;
    top: 0;
    left: 24%;
    /*background-color: #5de6ff;*/
  }
</style>
