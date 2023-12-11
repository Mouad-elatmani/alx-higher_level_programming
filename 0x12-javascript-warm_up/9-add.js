#!/usr/bin/node
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
if (!isNaN(process.argv[2]) && !isNaN(process.argv[3])) {
  add(process.argv[2], process.argv[3]);
} else {
  console.log('NaN');
}
