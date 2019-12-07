<template>
  <div id="info02"></div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "AppInfo02",
        mounted() {
            this.init_chart();
        },
        methods:{
            init_chart(){
                let echarts = this.$echarts;
                let myChart = this.$echarts.init(document.getElementById('info02'));
                myChart.showLoading();
                $.get('../../static/les-miserables.gexf', function (xml) {
                    myChart.hideLoading();

                    let graph = echarts.dataTool.gexf.parse(xml);
                    let categories = [];
                    for (let i = 0; i < 9; i++) {
                        categories[i] = {
                            name: '类目' + i
                        };
                    }
                    graph.nodes.forEach(function (node) {
                        node.itemStyle = null;
                        node.symbolSize = 10;
                        node.value = node.symbolSize;
                        node.category = node.attributes.modularity_class;
                        // Use random x, y
                        node.x = node.y = null;
                        node.draggable = true;
                    });
                    let option = {
                        //backgroundColor: '#515a6e',
                        title: {
                            show:false,
                            text: 'Les Miserables',
                            subtext: 'Default layout',
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
                        animation: false,
                        series : [
                            {
                                name: 'Les Miserables',
                                type: 'graph',
                                layout: 'force',
                                data: graph.nodes,
                                links: graph.links,
                                categories: categories,
                                roam: true,
                                label: {
                                    normal: {
                                        position: 'right'
                                    }
                                },
                                force: {
                                    repulsion: 100
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
  #info02{
    position: absolute;
    top: 31%;
    width: 23.5%;
    height: 38%;
  }
</style>
