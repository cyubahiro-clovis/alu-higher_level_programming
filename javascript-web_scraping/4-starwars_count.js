#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const withWedge = films.filter((film) =>
      film.characters.some((character) => character.endsWith('/18/'))
    );
    console.log(withWedge.length);
  }
});
