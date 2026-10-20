#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';
for (let i = 0; i < languages.length; i++) {
  output += i === languages.length - 1 ? languages[i] : `${languages[i]}\n`;
}
console.log(output);
