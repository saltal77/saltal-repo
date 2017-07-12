
// подключаем нужные модули 
var fs = require('fs');
var clc = require('cli-color');
var warn = clc.yellow;
var error = clc.red.bold;
var winner = clc.bgMagentaBright;
var Table = require('cli-table');
var table = new Table();
var prompt = require('prompt');
var logdata = {"rounds": 0, "wins": 0, "loss": 0};
var moneta = Math.random();
var name_c, name_h, res;

// приводим случайное число к 0 или 1 (орлу или решке)
if (moneta > 0.5) {
	moneta = 1;
}
else {
	moneta = 0;
}

// если файл статистики есть покажем ее с помощью cli-table
if(fs.existsSync('logg.json')){

	fs.readFile('logg.json', function (err, data) {
	     if (err) throw err;
	     logdata = JSON.parse(data);
	     console.log();
	     console.log(' Статистика Игры')
	     table.push({'Раундов': logdata.rounds },
	     	        {'Побед': logdata.wins },
	     	        {'Поражений': logdata.loss }, 
	     	        {'Отношение П/П': (parseInt(logdata.wins)/ parseInt(logdata.loss)).toFixed(2)});
         console.log(table.toString());
	     });
       }

console.log('-=-Консольная Игра на NodeJS-=-');
console.log('-=-*** Орел и Решка ***-=-');
console.log('Нужно ввести число - 1 (Орел) или - 0 (Решка)');


// ввод данных пользователя
prompt.start();

prompt.get('Vashe_chislo', function (err, result) {
    
    res = result.Vashe_chislo;
// красивый вывод загаданной стороны монеты компьютером и пользователя вместо 0 или 1
    if(res == '1'){
    	name_c = 'Орел'
    }
    else{
    	name_c = 'Решка'
    }
    if(moneta == '1'){
        name_h = 'Орел'
    }
    else{
    	name_h = 'Решка'
    }

// функция сравнения, подсчета и записи результатов в json
	function match() {
	   
	    if (res == moneta){
	    	console.log(winner('Вы угадали!'));
	    	console.log(warn('Вы ввели: ' + name_c + ', выпало: '  + name_h));
	        logdata.rounds +=1;
	        logdata.wins +=1;
	        logdata = JSON.stringify(logdata);
	        fs.writeFileSync('logg.json', logdata)
	    }
	    else{
	    	console.log(error('Вы не угадали!'));
	    	console.log(error('Вы ввели: '  + name_c + ', выпало: '  + name_h)); 
	        logdata.rounds +=1;
	        logdata.loss +=1;
	        logdata = JSON.stringify(logdata);
	        fs.writeFileSync('logg.json', logdata)
	        }  
	    }
// блок проверки введенных данных пользователем
		switch(res) {

			case '1':
			match();
			break;

			case '0':
			match();
			break;

			default:
			console.log('Не верно введено число! Нужно ввести 0 или 1...');
			break;
		} 
});

