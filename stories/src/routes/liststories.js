let express = require('express');
let mongoose = require('mongoose');

let router = express.Router();
let stories = mongoose.model('Stories');

router.get('/', function (req, res, next) {
    stories.find({}, function (err, story) {
        if(err){
            next(err);
        }
        res.json(story);
    })
});

module.exports = router;
