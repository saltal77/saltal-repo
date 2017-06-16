let mongoose = require('mongoose');

let interestSheme = new mongoose.Schema({
    title: String,
    text: String,
});

mongoose.model('Interest', interestSheme, 'interest');


