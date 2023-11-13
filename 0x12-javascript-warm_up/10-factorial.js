#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(recFactorial(parseInt(argv[2])));
}

function recFactorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } return (n * recFactorial(n - 1));
}
