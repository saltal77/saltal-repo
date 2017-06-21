let mongoose = require('mongoose');

let userSheme = new mongoose.Schema({
    user: String,
    pass: String
});

mongoose.model('Users', userSheme, 'users');


