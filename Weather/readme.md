OpenWeatherMap is an online service that provides a free API for accessing current weather data, forecasts, for web services and mobile applications. Archived data is available only on a commercial basis. The official meteorological services, data from airport weather stations, and data from private weather stations are used as a data source.

    The OpenWeatherMap.py script retrieves a list of cities using APPID on the OpenWeatherMap website - http://bulk.openweathermap.org/sample/city.list.json.gz

    Unpacks and asks about the city in which we want to know the weather (offering to enter the three initial letters, then displays a list of available cities based on the downloaded data)

    Displays current weather data for the selected city.

    Creates a SQL database and enters data on this city and weather, when it is called again, it updates the data in the database

    The export_openweather.py script exports weather data for the desired city from the SQL database created by OpenWeatherMap.py in json or csv forms

The format is export_openweather.py --csv filename city or export_openweather.py --json filename city

    city ​​and file name can be omitted, then the entire database with the name filename will be exported



OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API для доступа к данным о текущей погоде, прогнозам,
для web-сервисов и мобильных приложений. Архивные данные доступны только на коммерческой основе.
В качестве источника данных используются официальные метеорологические службы, данные из метеостанций аэропортов, 
и данные с частных метеостанций.


1) Скрипт OpenWeatherMap.py получает с помощью APPID на сайте OpenWeatherMap список городов - 
http://bulk.openweathermap.org/sample/city.list.json.gz

2) Распаковвывает и спрашивает о городе в которм хотим узнать погоду (предлагая ввести три начальные буквы, далее 
выводит список доступных 
городов основываясь на загруженных данных)

3)  Выводит данные о текущей погоде ввыбранном  городе

4) Создает БД SQL и  заносит данные об этом городе и погоде, при повторном вызове обновляет данные в базе

5) Скрипт export_openweather.py экспортирует данные о погоде нужного города из БД SQL созданной OpenWeatherMap.py
в формах json или csv 
 
Формат - export_openweather.py --csv filename город  или  export_openweather.py --json filename город
* город и имя файла можно не задавать, тогда будет сделан экспорт всей базы с именем filename
