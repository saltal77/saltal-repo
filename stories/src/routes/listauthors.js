let express = require('express');
let mongoose = require('mongoose');

let router = express.Router();
let authors = mongoose.model('Authors');

router.get('/', function (req, res, next) {
    authors.find({}, function (err, authors) {
        if(err){
            next(err);
        }
        res.json(authors);
    })
});

module.exports = router;