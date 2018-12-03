const readline = require('readline');
const fs = require('fs');

let totalFrequency = 0;
const rl = readline.createInterface({
  input: fs.createReadStream('./dataset.txt'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  if (line[0] == '+') {
    totalFrequency += parseInt(line.slice(1, line.length))
  } else if (line[0] == '-') {
    totalFrequency -= parseInt(line.slice(1, line.length))
  }
});

rl.on('close', () => {
  console.log('we done', totalFrequency)
});