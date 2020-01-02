<template>
  <div id="info03"></div>
</template>

<script>
    import DataManager from "../DataManager/DataManager";
    export default {
        name: "AppInfo04",
        mounted() {
            this.getData();
        },
        methods:{
            getData(){
                DataManager.Data_Lime100_protocol(0).then(res=>{
                    console.log(res.data);
                    this.Draw(res.data);
                });
            },
            Draw(data){

                let chart = this.$echarts.init(document.getElementById('info03'));

                let    option = {
                    //backgroundColor: '#0a1235',
                    title:{
                        text:'网络传输协议',
                        subtext:'Internet Protocol'
                    },
                    tooltip: {
                        trigger: 'item',
                        //formatter: "{a} <br/>{b} : {c}千万元"
                    },
                    legend: {
                        x: 'center',
                        y: '15%',
                        data: data.map(d=>d.name),
                        icon: 'circle',
                        textStyle: {
                            color: '#7e7e7e',
                        }
                    },
                    calculable: true,
                    series: [{
                        name: '协议',
                        type: 'pie',
                        //起始角度，支持范围[0, 360]
                        startAngle: 0,
                        //饼图的半径，数组的第一项是内半径，第二项是外半径
                        radius: [41, 153.75],
                        //支持设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
                        center: ['50%', '35%'],
                        //是否展示成南丁格尔图，通过半径区分数据大小。可选择两种模式：
                        // 'radius' 面积展现数据的百分比，半径展现数据的大小。
                        //  'area' 所有扇区面积相同，仅通过半径展现数据大小
                        roseType: 'area',
                        //是否启用防止标签重叠策略，默认开启，圆环图这个例子中需要强制所有标签放在中心位置，可以将该值设为 false。
                        avoidLabelOverlap: false,
                        label: {
                            normal: {
                                show: true,
                                //formatter: '{c}千万元'
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        labelLine: {
                            normal: {
                                show: true,
                                length2: 1,
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        data: [{
                            value: data[0].value,
                            name: 'unencryped_jabber',
                            itemStyle: {
                                normal: {
                                    color: '#f845f1'
                                }
                            }
                        },
                            {
                                value: data[1].value,
                                name: 'http',
                                itemStyle: {
                                    normal: {
                                        color: '#ad46f3'
                                    }
                                }
                            },
                            {
                                value: data[2].value,
                                name: 'unknown',
                                itemStyle: {
                                    normal: {
                                        color: '#5045f6'
                                    }
                                }
                            },
                            {
                                value: data[3].value,
                                name: 'ssl',
                                itemStyle: {
                                    normal: {
                                        color: '#4777f5'
                                    }
                                }
                            },
                            {
                                value: data[4].value,
                                name: 'mysql',
                                itemStyle: {
                                    normal: {
                                        color: '#44aff0'
                                    }
                                }
                            },
                            {
                                value: data[5].value,
                                name: 'http_proxy',
                                itemStyle: {
                                    normal: {
                                        color: '#45dbf7'
                                    }
                                }
                            },
                            {
                                value: data[6].value,
                                name: 'ftp_control',
                                itemStyle: {
                                    normal: {
                                        color: '#f6d54a'
                                    }
                                }
                            },
                            {
                                value: data[7].value,
                                name: 'ftp_data',
                                itemStyle: {
                                    normal: {
                                        color: '#f69846'
                                    }
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            },
                            {
                                value: 0,
                                name: "",
                                itemStyle: {
                                    normal: {
                                        color: 'transparent'
                                    }
                                },
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    show: false
                                }
                            }
                        ]
                    }]
                };
                chart.setOption(option);
            }
        }
    }
</script>

<style scoped>
  #info03{
    position: absolute;
    width: 23.5%;
    height: 30%;
    bottom: 0;
  }
</style>
