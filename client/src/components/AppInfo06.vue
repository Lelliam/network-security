<template>
  <div id="info06"></div>
</template>

<script>

    import DataManager from "../DataManager/DataManager";
    export default {
        name: "AppInfo06",
        mounted() {
            this.getData();
        },
        methods:{
            getData(){
                DataManager.Data_Lime100_port(0).then(res=>{
                    console.log(res.data);
                    this.Draw(res.data);
                });
            },
            Draw(data){
                let echarts = this.$echarts;
                let chart = this.$echarts.init(document.getElementById('info06'));
                let option = {
                    //backgroundColor: '#515a6e',
                    title:{
                        text:'端口使用情况',
                        subtext:'Ports Used'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    grid: {
                        top: '22%',
                        right: '5%',
                        left: '10%',
                        bottom: '15%'
                    },
                    xAxis: [{
                        type: 'category',
                        data: data.map(d=>d.name),
                        axisLine: {
                            lineStyle: {
                                color: 'rgba(150,146,161,0.74)'
                            }
                        },
                        axisLabel: {
                            margin: 10,
                            color: '#9692a1',
                            textStyle: {
                                fontSize: 11
                            },
                        },
                    }],
                    yAxis: [{
                        axisLabel: {
                            formatter: '{value}',
                            color: '#9692a1',
                            textStyle: {
                                fontSize: 11
                            },
                        },
                        axisLine: {
                            show: false,
                            lineStyle: {
                                color: 'rgba(150,146,161,0.74)'
                            }
                        },
                        splitLine: {
                            lineStyle: {
                                color: 'rgba(150,146,161,0.2)'
                            }
                        }
                    }],
                    series: [{
                        name:'端口',
                        type: 'bar',
                        data: data.map(d=>d.value),
                        barWidth: '10px',
                        itemStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0,
                                    color: 'rgba(255,153,39,0.75)' // 0% 处的颜色
                                }, {
                                    offset: 1,
                                    color: 'rgba(234,78,55,0.88)' // 100% 处的颜色
                                }], false),
                                barBorderRadius: [30, 30, 30, 30],
                                shadowColor: 'rgb(255,255,255)',
                                //shadowBlur: 4,
                            }
                        },
                        label: {
                            normal: {
                                show: true,
                                lineHeight: 20,
                                width: 40,
                                height: 30,
                                backgroundColor: 'rgba(207,217,221,0.1)',
                                borderRadius: 300,
                                position: ['-4', '-28'],
                                distance: 1,
                                textStyle:{
                                    color:"#9692a1",
                                    fontSize:9
                                }
                            }
                        }
                    }]
                };
                chart.setOption(option);
            },
        }
    }
</script>

<style scoped>
  #info06{
    position: absolute;
    width: 23.5%;
    height: 30%;
    bottom: 0;
    right: 0;
  }
</style>
