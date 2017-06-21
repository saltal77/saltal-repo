let express = require('express');
let mongoose = require('mongoose');

let router = express.Router();
let users = mongoose.model('Users');

router.get('/', function (req, res, next) {
    users.find({}, function (err, users) {
        if(err){
            next(err);
        }
        res.json(users);
    })
});

module.exports = router;