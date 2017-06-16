let mongoose = require('mongoose');

let commentsSheme = new mongoose.Schema({
    postId: String,
    id: String,
    name: String,
    comm: String
});

mongoose.model('Comments', commentsSheme, 'comments');


