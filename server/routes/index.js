let express = require('express');
let router = express.Router();
let faker = require('faker');
let sql_operation = require("./operation");
let d3 = require('d3');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get("/query", function(req, res, next) {
  sql_operation.query(req.query.sql,data=>{
    res.send(data);
  });
});

router.get('/test', function(req, res, next) {
  let num = 100;
  let data = [];
  while (num--){
    data.push({
      ip:faker.internet.ip(),
      latitude:faker.address.latitude(),
      longitude:faker.address.longitude()
    });
  }
  res.send(data);
});

router.get("/data_lim100", function(req, res, next) {
  sql_operation.query(`select * from networkdata_store limit ${req.query.start},${req.query.start+100}`,data=>{

    let nodes = [];
    let links = [];

    data.forEach(d=>{
      if(nodes.findIndex(t=> t.name === d.source_ip) === -1){
        nodes.push({name:d.source_ip,value:1});
      }
      else{
        nodes[nodes.findIndex(t=> t.name === d.source_ip)].value++;
      }
      if(nodes.findIndex(t=> t.name === d.destination_ip) === -1){
        nodes.push({name:d.destination_ip,value:1});
      }
      else{
        nodes[nodes.findIndex(t=> t.name === d.destination_ip)].value++;
      }

      let flag = true;

      links.forEach(t=>{
        if(t.source === d.source_ip && t.target === d.destination_ip){
          flag = false;
          t.value++;
        }
      });

      if(flag)
        links.push({
          source:d.source_ip,
          target:d.destination_ip,
          value:1
        });
    });
    res.send({nodes:nodes,links:links});
  });
});

router.get("/data_lim100_port", function(req, res, next) {
  sql_operation.query(`select * from networkdata_store limit ${req.query.start},${req.query.start+100}`,data=>{
    res.send(d3.nest().key(d=>d.destination_port).entries(data).map(d=>{
      return {
        name:d.key,
        value:d.values.length
      }
    }));
  });
});

router.get("/data_lim100_protocol", function(req, res, next) {
  sql_operation.query(`select * from networkdata_store limit ${req.query.start},${req.query.start+100}`,data=>{
    res.send(d3.nest().key(d=>d.protocol).entries(data).map(d=>{
      return {
        name:d.key,
        value:d.values.length
      }
    }));
  });
});

router.get("/data_lim100_length", function(req, res, next) {
  let format = d3.timeFormat('%Y-%m-%d %H:%M:%S');
  sql_operation.query(`select * from networkdata_store limit ${req.query.start},${req.query.start+100}`,data=>{
    res.send(d3.nest().key(d=>format(new Date(d.record_time))).entries(data).map(d=>{
      return {
        date:d.key,
        value:d3.sum(d.values,s=>parseFloat(s.uplink_length))+d3.sum(d.values,s=>parseFloat(s.downlink_length))
      }
    }).sort((a,b)=>new Date(a.date)-new Date(b.date)));
  });
});

module.exports = router;
