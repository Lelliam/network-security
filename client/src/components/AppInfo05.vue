<template>
  <div id="info05"></div>
</template>

<script>
    import DataManager from "../DataManager/DataManager";
    export default {
        name: "AppInfo05",
        mounted() {
            this.getData();
        },
        methods:{
            getData(){
              DataManager.Data_lim100(0).then(res=>{
                  this.Draw(res.data);
              });
            },
            Draw(graph){

                let myChart = this.$echarts.init(document.getElementById('info05'));

                //let categories = ['1','2','3','4'];

                graph.nodes.forEach(function (node,i) {
                    node.itemStyle = null;
                    // node.symbolSize = 15;
                    node.symbolSize = node.value;
                    //node.category = '1';
                    // Use random x, y
                    node.x = node.y = null;
                    node.draggable = true;
                });

                let option = {
                    title: {
                        show:true,
                        text: '网络拓扑结构',
                        subtext: 'circular layout',
                        top: '0',
                        left: '0'
                    },
                    tooltip: {},
                    // legend: [{
                    //     show:false,
                    //     // selectedMode: 'single',
                    //     data: categories
                    // }],
                    animation: false,
                    series : [{
                        name: 'circular layout',
                        zoom:.9,
                        type: 'graph',
                        layout: 'circular',
                        data: graph.nodes,
                        links: graph.links,
                        //categories: categories,
                        roam: true,
                        itemStyle:{
                        },
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
