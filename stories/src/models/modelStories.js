let mongoose = require('mongoose');

let storySheme = new mongoose.Schema({
    id: String,
    title: String,
    text: String,
    text_next: String,
    author: String
});

mongoose.model('Stories', storySheme, 'story');

