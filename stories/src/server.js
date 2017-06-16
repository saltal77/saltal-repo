let express = require('express');
let logger = require('morgan');
let bodyParser = require('body-parser');
let mongoose = require('mongoose');

// Модели
require('./models/modelAuthor');
require('./models/modelInterest');
require('./models/modelComments');
require('./models/modelStories');

// Маршруты запроса к БД
let routeAuthor = require('./routes/listauthors');
let routeInterest = require('./routes/listinterest');
let routeComments = require('./routes/listcomments');
let routeStories = require('./routes/liststories');


mongoose.connect('mongodb://localhost:27017/stories');

let app = express();
app.set('view engine', 'html');

// Роутинг
app.use(function (req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'X-Requested-With');
    next();
});

app.use(express.static(__dirname + '/dist'));

app.use(logger('combined'));

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({extended: false}));

// запросы к БД
app.use('/store/listauthors', routeAuthor);
app.use('/store/listinterest', routeInterest);
app.use('/store/listcomments', routeComments);
app.use('/store/liststories', routeStories);

// Обработка запросов и ошибок
app.use(function (req, res, next) {
    let err = new Error('Not Found');
    err.status = 404;
    next(err);
});

app.use(function (err, req, next) {
    res.status(err.status || 500);
    req.json({
        message: err.message,
        error: err
    });
});

let PORT = 8888;
app.listen(PORT, function () {
    console.log('NodeServer запущен на порту: ', PORT);
});
