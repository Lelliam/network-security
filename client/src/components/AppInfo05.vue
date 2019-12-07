<template>
  <div id="info05"></div>
</template>

<script>
    import $ from 'jquery'
    import '../../static/dataTool'
    export default {
        name: "AppInfo05",
        mounted() {
            this.init_chart();
        },
        methods:{
            init_chart(){
                let echarts = this.$echarts;
                let myChart = this.$echarts.init(document.getElementById('info05'));
                myChart.showLoading();
                $.get('../../static/les-miserables.gexf', function (xml) {
                    myChart.hideLoading();

                    let graph =new echarts.dataTool.gexf.parse(xml);
                    let categories = [];
                    for (let i = 0; i < 9; i++) {
                        categories[i] = {
                            name: '类目' + i
                        };
                    }
                    graph.nodes.forEach(function (node) {
                        node.itemStyle = null;
                        node.value = node.symbolSize;
                        node.symbolSize /= 1.5;
                        node.label = {
                            normal: {
                                show: node.symbolSize >10,
                                textStyle:{
                                    'fontSize':10
                                }
                            }
                        };
                        node.category = node.attributes.modularity_class;
                    });
                    let option = {
                        //backgroundColor: '#515a6e',
                        title: {
                            show:false,
                            text: 'Les Miserables',
                            subtext: 'Circular layout',
                            top: 'bottom',
                            left: 'right'
                        },
                        tooltip: {},
                        legend: [{
                            show:false,
                            // selectedMode: 'single',
                            data: categories.map(function (a) {
                                return a.name;
                            })
                        }],
                        animationDurationUpdate: 1500,
                        animationEasingUpdate: 'quinticInOut',
                        series : [
                            {
                                name: 'Les Miserables',
                                type: 'graph',
                                layout: 'circular',
                                circular: {
                                    rotateLabel: true
                                },
                                data: graph.nodes,
                                links: graph.links,
                                categories: categories,
                                roam: true,
                                label: {
                                    normal: {
                                        position: 'right',
                                        formatter: '192.188.88.09'
                                    }
                                },
                                lineStyle: {
                                    normal: {
                                        color: 'source',
                                        curveness: 0.3
                                    }
                                }
                            }
                        ]
                    };

                    myChart.setOption(option);
                }, 'xml');
            }
        }
    }
</script>

<style scoped>
  #info05{
    position: absolute;
    width: 23.5%;
    height: 48%;
    right: 0;
    top: 21%;
  }
</style>
