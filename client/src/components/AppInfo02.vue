<template>
  <div id="info02"></div>
</template>

<script>
    import DataManager from "../DataManager/DataManager";
    export default {
        name: "AppNodeLink",
        mounted() {
            this.getData();
        },
        methods:{
            getData(){
                DataManager.Data_lim100(0).then(res=>{
                    console.log(res.data);
                    this.Draw(res.data)
                });
            },
            Draw(graph){
                let myChart = this.$echarts.init(document.getElementById('info02'));
                let categories = [0,1,2,3,4,5];
                graph.nodes.forEach(function (node) {
                    node.itemStyle = {
                        normal: {
                            color:'#ff6267'
                        }
                    };
                    node.symbolSize = 15;
                    node.category = Math.floor(Math.random()*5);
                    // Use random x, y
                    node.x = node.y = null;
                    node.draggable = true;
                });

                console.log(graph.nodes);
                let option = {
                    title: {
                        show:true,
                        text: '网络拓扑结构',
                        subtext: 'force layout',
                        top: '0',
                        left: '0'
                    },
                    tooltip: {},
                    legend: [{
                        show:false,
                        // selectedMode: 'single',
                        data: categories.map(function (a) {
                            return a;
                        })
                    }],
                    animation: false,
                    series : [{
                        name: 'Les Miserables',
                        zoom:.4,
                        type: 'graph',
                        layout: 'force',
                        data: graph.nodes,
                        links: graph.links,
                        categories: categories,
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
  #info02{
    position: absolute;
    top: 31%;
    width: 23.5%;
    height: 38%;
  }
</style>
