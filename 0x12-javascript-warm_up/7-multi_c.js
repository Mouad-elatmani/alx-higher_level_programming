#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
const num = process.argv[2] | 0;
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
