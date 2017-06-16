let express = require('express');
let mongoose = require('mongoose');

let router = express.Router();
let interest = mongoose.model('Interest');

router.get('/', function (req, res, next) {
    interest.find({}, function (err, interest) {
        if(err){
            next(err);
        }
        res.json(interest);
    })
});

module.exports = router;
