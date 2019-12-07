<template>
  <div id="info01"></div>
</template>

<script>
    export default {
        name: "AppInfo01",
        mounted() {
            this.init_chart();
        },
        methods:{
            init_chart(){
                let getVirtulData = (year) => {
                    let echarts = this.$echarts;
                    year = year || '2017';
                    let date = +echarts.number.parseDate(year + '-01-01');
                    let end = +echarts.number.parseDate((+year + 1) + '-01-01');
                    let dayTime = 3600 * 24 * 1000;
                    let data = [];
                    for (let time = date; time < end; time += dayTime) {
                        data.push([
                            echarts.format.formatTime('yyyy-MM-dd', time),
                            Math.floor(Math.random() * 10000)
                        ]);
                    }
                    return data;
                }

                let data = getVirtulData(2016);

                let chart = this.$echarts.init(document.getElementById('info01'));

                let option = {
                    //backgroundColor: '#515a6e',
                    title: {
                        top: 30,
                        text: '数据纯属虚构',
                        subtext: '数据纯属虚构',
                        left: 'center',
                        textStyle: {
                            color: '#323c48'
                        }
                    },
                    tooltip : {
                        trigger: 'item'
                    },
                    legend: {
                        top: '30',
                        left: '10',
                        data:['数据', 'TOP12'],
                        textStyle: {
                            color: '#323c48'
                        }
                    },
                    calendar: [{
                        top: 100,
                        left: '17%',
                        range: ['2016-01-01', '2016-04-30'],
                        splitLine: {
                            show: true,
                            lineStyle: {
                                color: '#9692a1',
                                width: 2,
                                type: 'solid'
                            }
                        },
                        yearLabel: {
                            formatter: '{start}  1st',
                            textStyle: {
                                color: '#323c48'
                            }
                        },
                        monthLabel: {
                            textStyle: {
                                color: '#323c48'
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#323c48',
                                borderWidth: 1,
                                borderColor: '#101e2c'
                            }
                        }
                    }],
                    series : [
                        {
                            name: '数据',
                            type: 'scatter',
                            coordinateSystem: 'calendar',
                            data: data,
                            symbolSize: function (val) {
                                return val[1] / 500;
                            },
                            itemStyle: {
                                normal: {
                                    color: '#ddb926'
                                }
                            }
                        },
                        {
                            name: 'TOP12',
                            type: 'effectScatter',
                            coordinateSystem: 'calendar',
                            data: data.sort(function (a, b) {
                                return b[1] - a[1];
                            }).slice(0, 12),
                            symbolSize: function (val) {
                                return val[1] / 500;
                            },
                            showEffectOn: 'render',
                            rippleEffect: {
                                brushType: 'stroke'
                            },
                            hoverAnimation: true,
                            itemStyle: {
                                normal: {
                                    color: '#f4e925',
                                    shadowBlur: 10,
                                    shadowColor: '#333'
                                }
                            },
                            zlevel: 1
                        }
                    ]
                };

                chart.setOption(option);
            }
        }
    }
</script>

<style scoped>
  #info01{
    position: absolute;
    width: 23.5%;
    height: 30%;
  }
</style>
