<template>
  <div id="time_line"></div>
</template>

<script>
    import DataManager from "../DataManager/DataManager";
    export default {
        name: "AppTimeLine",
        mounted() {
            this.Update();
        },
        methods:{
            getData(start){
                DataManager.Data_Lime100_length(start).then(res=>{
                    console.log(res.data);
                    this.Draw(res.data);
                });
            },
            Draw(data){

                let echarts = this.$echarts;
                let chart = this.$echarts.init(document.getElementById('time_line'));

                let color = ['#1a9bfc', '#99da69', '#e32f46', '#7049f0', '#fa704d', '#01babc', ];

                let option = {
                    //backgroundColor: '#515a6e',
                    // legend: {
                    //     show:false,
                    //     top: 20,
                    //     itemGap:5,
                    //     itemWidth:5,
                    //     textStyle: {
                    //         color: '#fff',
                    //         fontSize: '10'
                    //     },
                    //     data: ''
                    // },
                    title: {
                        show:false,
                        text: "负面言论分领域趋势",
                        textStyle: {
                            color: '#fff',
                            fontSize: '22',
                            fontWeight: 'normal',
                        },
                        subtextStyle: {
                            color: '#90979c',
                            fontSize: '16',

                        },
                    },
                    tooltip: {
                        show:true,
                        trigger: "axis",
                        axisPointer: { // 坐标轴指示器，坐标轴触发有效
                            type: 'line', // 默认为直线，可选为：'line' | 'shadow'
                            lineStyle: {
                                color: '#57617B'
                            }
                        },
                        //formatter: '{b}<br />{a0}: {c0}%<br />{a1}: {c1}%<br />{a2}: {c2}%<br />{a3}: {c3}%<br />{a4}: {c4}%<br />{a5}: {c5}%',
                        backgroundColor: 'rgba(0,0,0,0.7)', // 背景
                        padding: [8, 10], //内边距
                        extraCssText: 'box-shadow: 0 0 3px rgba(255, 255, 255, 0.4);', //添加阴影
                    },
                    grid: {
                        borderWidth: 0,
                        left:"5%",
                        width:"90%",
                        top: "10%",
                        bottom: "10%",
                        textStyle: {
                            color: "#43393e"
                        }
                    },
                    xAxis: [{
                        type: "category",
                        axisLine: {
                            show: false,
                            lineStyle: {
                                color: '#9692a1'
                            }
                        },
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: '#9692a1',
                                width:.2
                            }
                        },
                        boundaryGap: false, //坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样
                        axisTick: {
                            show: false
                        },
                        splitArea: {
                            show: false
                        },
                        axisLabel: {
                            inside: false,
                            textStyle: {
                                color: '#43393e',
                                fontWeight: 'normal',
                                fontSize: '12',
                            },
                        },
                        data: data.map(d=>d.date),
                    }],
                    yAxis: {
                        type: 'value',
                        axisTick: {
                            show: false
                        },
                        axisLine: {
                            show: false,
                            lineStyle: {
                                color: '#9692a1',
                            }
                        },
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: '#9692a1',
                                width:.2
                            }
                        },
                        axisLabel: {
                            textStyle: {
                                color: '#9692a1',
                                fontWeight: 'normal',
                                fontSize: '12',
                            },
                            //formatter: '{value}%',
                        },
                    },
                    series: [{
                        name: '总流量',
                        type: "line",
                        symbolSize: 3,//标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为20，高为10[ default: 4 ]
                        symbol: 'circle',//标记的图形。ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
                        smooth: true, //是否平滑曲线显示
                        showSymbol: false, //是否显示 symbol, 如果 false 则只有在 tooltip hover 的时候显示
                        areaStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                    offset: 0,
                                    color: 'rgba(255,134,20,0.4)'
                                }, {
                                    offset: 0.8,
                                    color: 'rgb(73,238,255,.01)'
                                }], false),
                                // shadowColor: 'rgba(255,255,255, 0.1)',
                                //shadowBlur: 10,
                                opacity:0.3,
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#ff8614',
                                lineStyle: {
                                    width: .5,
                                    type: 'solid' //'dotted'虚线 'solid'实线
                                },
                                borderColor: '#FFF', //图形的描边颜色。支持的格式同 color
                                borderWidth: 8 ,//描边线宽。为 0 时无描边。[ default: 0 ]
                                barBorderRadius: 0,
                                label: {
                                    show: false,
                                },
                                opacity:0.5,
                            }
                        },
                        data: data
                    }],
                };

                chart.setOption(option);
            },
            Update(){
                //let i = 0;
                //setInterval(()=>{
                    this.getData(0);
               /// },1000)
            }
        }
    }
</script>

<style scoped>
  #time_line{
    position: absolute;
    width: 52%;
    left: 24%;
    height: 30%;
    bottom: 0;
  }
</style>
