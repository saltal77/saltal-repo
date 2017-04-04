/*author - saltal*/


//Подключение плагинов GULP
var gulp = require('gulp');
var sass = require('gulp-sass');//Ковертация SCSS SASS в CSS
var brSync = require('browser-sync');//Перегрузка браузера
var useref = require('gulp-useref');//Сбор JS CSS файлов проекта в одну папку
var uglify = require('gulp-uglifyjs');//Сжатие файлов JS
var csso = require('gulp-csso');//Сжатие файлов CSS
var gulpIf = require('gulp-if');//Модуль условий Если... то...
//Пути для Gulp
var config = {
    from: './in',
    to: './out',
    index: './'
};
//Конвертация файла стилей SCSS в CSS
gulp.task('scss-transfer', function(){
    //gulp.src('./in/scss/style.scss')//Путь поиска без переменной config
    //gulp.src(config.from +'/sass/**/*.sass')//Переработка SASS
      gulp.src(config.from + '/scss/**/*.scss')//Переработка SCSS
        .pipe(sass())
        //.pipe(gulp.dest('./out/css'))//Путь для готовых файлов без переменной config
        .pipe(gulp.dest(config.to + '/css'))
          .pipe(brSync.reload({stream: true}))
});
//Автоматическое отслеживание изменений файлов SCSS и конвертация , а так же перезапуск браузера
gulp.task('watch',['sync', 'scss-transfer'], function () {
    gulp.watch(config.from + '/scss/**/*.scss', ['scss-transfer']);
});
//Перезагрузка браузера
gulp.task('sync', function () {
    brSync({
        server: {
            baseDir: config.index //Путь к файлу HTML
        }
    });
});
//Сбор всех файлов JS и CSS из разных папок проекта (по очереди следования) в один файл (кладем в папку OUT)
gulp.task('js-css-compile', function(){
       return  gulp.src('*.html') //!Возвращает поток для передачи данных другому заданию по цепочке
             .pipe(useref())
             .pipe(gulp.dest('out'))
});
//Сжатие файлов JS и CSS (Зависимость от завершения задачи js-css-compile)
gulp.task('compress',['js-css-compile'],  function() {
    gulp.src('out/**/*.*')
        //.pipe(uglify())
        //.pipe(csso())
        .pipe(gulpIf('*.css', csso()))//Сжатие CSS
        .pipe(gulpIf('*.js', uglify()))//Сжатие JS
        .pipe(gulp.dest('out'))
});
//Задача сборки всех файлов CSS & JS проекта в нужные  папки (CSS & JS) со сжатием (зависимость от завершения задачи 1-js-css-compile 2-compress)
gulp.task('assemble', ['compress', 'js-css-compile'], function () {
console.log('Project complete!');
});
//Тестовый запуск задания GULP
gulp.task('greet', function() {
    console.log('gulp running!');
});
