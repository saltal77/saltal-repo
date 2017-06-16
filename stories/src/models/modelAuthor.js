let mongoose = require('mongoose');

let authorSheme = new mongoose.Schema({
    id: String,
    name: String,
    username: String,
    address: String,
    phone: String,
    prof: String,
    desc: String
});


// 'authors' - название схемы в БД MongoDB
// 'Authors' - экспортируемое название модели
mongoose.model('Authors', authorSheme, 'authors');

