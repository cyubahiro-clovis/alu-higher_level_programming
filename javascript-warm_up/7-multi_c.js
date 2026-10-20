#!/usr/bin/node
const count = parseInt(process.argv[2], 10);
if (Number.isNaN(count)) {
  console.log('Missing number of occurrences');
}
let output = '';
for (let i = 0; i < count; i++) {
  output += i === count - 1 ? 'C is fun' : 'C is fun\n';
}
if (!Number.isNaN(count) && count > 0) {
  console.log(output);
}
