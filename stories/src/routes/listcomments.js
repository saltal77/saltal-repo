let express = require('express');
let mongoose = require('mongoose');

let router = express.Router();
let comments = mongoose.model('Comments');

router.get('/', function (req, res, next) {
    comments.find({}, function (err, comments) {
        if(err){
            next(err);
        }
        res.json(comments);
    })
});

module.exports = router;