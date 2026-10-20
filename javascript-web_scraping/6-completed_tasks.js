#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const completed = {};
    for (const task of JSON.parse(body)) {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    }
    console.log(completed);
  }
});
