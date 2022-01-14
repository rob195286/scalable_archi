const express = require('express');
const cluster = require('cluster');
const numCPUs = require('os').cpus().length; // Check the number of available CPU.
 
const app = express();
var bodyParser = require('body-parser');
var jsonParser = bodyParser.json();
const PORT = 5000;


if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);
  // Fork workers.
  for (let i = 0; i < numCPUs-1; i++) {
    cluster.fork();
  }

  cluster.on('exit', function (worker) {
    // Replace the dead worker, we're not sentimental
    console.log('Worker %d died ', worker.id);
    cluster.fork();
  });
}

else {  
  // Workers can share any TCP connection
  app.listen(PORT, err => {
    err ? console.log("Error in server setup") :
     console.log(`Worker ${process.pid} started`);
  });

  app.post('/', jsonParser, (req, res) => {
      var compNbr = req.body;
      var mandelbrot = mandelbrotComputation([compNbr.real, compNbr.img]);
      //console.log(req.body, ' ', mandelbrot, ' ', );
      //console.log('-----------------');
      //console.log(`cluster ${cluster.worker.id} `);
      res.send(JSON.stringify(
      {
          'mandelbrot' : mandelbrot,
          'real' : compNbr.real,
          'img' : compNbr.img
      }))        
  })
}

function mandelbrotComputation(c, max_iter = 30){
  var z = [0,0];
  for(var i = 0; i < max_iter; i++){
    z = addComplexNumber(multComplexNumber(z, z), c);
    if(getModuleComplexNumber(z) > 2){
      return false;
    }
  }
  return true;
}



function addComplexNumber(nbr1, nbr2) {
  return [
      nbr1[0] + nbr2[0],
      nbr1[1] + nbr2[1]
  ]
}

function multComplexNumber(nbr1, nbr2) {
  return [
      nbr1[0] * nbr2[0] - nbr1[1] * nbr2[1],
      nbr1[0] * nbr2[1] + nbr1[1] *nbr2[0]
  ]
}

function getModuleComplexNumber(nbr){
  return Math.sqrt(Math.pow(nbr[0], 2) + Math.pow(nbr[1], 2));
}

