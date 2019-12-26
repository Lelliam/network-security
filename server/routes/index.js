let express = require('express');
let router = express.Router();

let faker = require('faker');
for(let i =0;i<10;i++){
  console.log(
      faker.internet.ip(),
      faker.internet.protocol(),
      faker.internet.mac(),
      faker.internet.domainName(),
  );
}
/*let Cap = require('cap').Cap;
let decoders = require('cap').decoders;
let PROTOCOL = decoders.PROTOCOL;
let c = new Cap();

let device = Cap.findDevice('10.10.4.133');
let filter = 'tcp and dst port 80';
let bufSize = 10 * 1024 * 1024;
let buffer = Buffer.alloc(65535);

let linkType = c.open(device, filter, bufSize, buffer);

c.setMinBytes && c.setMinBytes(0);

c.on('packet', function(nbytes, trunc) {
  console.log('packet: length ' + nbytes + ' bytes, truncated? '
      + (trunc ? 'yes' : 'no'));

  // raw packet data === buffer.slice(0, nbytes)

  if (linkType === 'ETHERNET') {
    let ret = decoders.Ethernet(buffer);

    if (ret.info.type === PROTOCOL.ETHERNET.IPV4) {
      console.log('Decoding IPv4 ...');

      ret = decoders.IPV4(buffer, ret.offset);
      console.log('from: ' + ret.info.srcaddr + ' to ' + ret.info.dstaddr);

      if (ret.info.protocol === PROTOCOL.IP.TCP) {
        let datalen = ret.info.totallen - ret.hdrlen;

        console.log('Decoding TCP ...');

        ret = decoders.TCP(buffer, ret.offset);
        console.log(' from port: ' + ret.info.srcport + ' to port: ' + ret.info.dstport);
        datalen -= ret.hdrlen;
        console.log(buffer.toString('binary', ret.offset, ret.offset + datalen));
      } else if (ret.info.protocol === PROTOCOL.IP.UDP) {
        console.log('Decoding UDP ...');

        ret = decoders.UDP(buffer, ret.offset);
        console.log(' from port: ' + ret.info.srcport + ' to port: ' + ret.info.dstport);
        console.log(buffer.toString('binary', ret.offset, ret.offset + ret.info.length));
      } else
        console.log('Unsupported IPv4 protocol: ' + PROTOCOL.IP[ret.info.protocol]);
    } else
      console.log('Unsupported Ethertype: ' + PROTOCOL.ETHERNET[ret.info.type]);
  }
});*/
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
