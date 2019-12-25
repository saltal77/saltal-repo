ReactJS blog (ES6), Bootstrap styles are used in the design. Application routing is based on "React-router", the blog has two stores based on the Flux architecture (sections "Interesting" and "Comments"), asynchronous data loading from MongoDB in conjunction with the backend Express server is performed.
(to demonstrate the project, the server part is simulated and stubs written with data in JSON format - data folder are written) (After entering the site using the registered username and password on the pages, the functions - Add, Delete and Edit
in the "Comments" section, in the "Interesting" and "Blogs" section - only the Addendum. (List of users and passwords from users_data.json: admin - 12345, author - 67891, etc.))

To start a project:

    copy - paste stories)
    install Node.js
    install the necessary modules - "npm i"
    building and starting the local server - "webpack -w" (building from the src folder to the dist folder)

To run the full version of the project with MongoDB:

    copy - paste stories)
    install Node.js
    install the necessary modules - "npm i"
    install MongoDB
    comment out && uncomment line data in files: Directory ... / src / app / components / blogsContent.js drown line - 20, open line - 21 AuthorInfo.js drown - 16, open - 17 authorsList.js drown - 16, open - 17 modal.js silence - 23, open - 24 Catalog ... / src / app / stores / commentsStore.js silence - 32, open - 33 interestStore.js silence - 29, open - 30
    launch MongoDB in the project folder ... / db mongod --dbpath ... / ... / current project path / db
    running backend Express server in the project folder ... / src / node server
    building and starting the local server - "webpack -w" (building from the src folder to the dist folder)


Блог на ReactJS (ES6), в оформлении используются Bootstrap стили. 
Роутинг приложения выполнен на основе "React-router",
в блоге имеется два хранилища на основе архитектуры Flux (разделы "Интересное" и "Комментарии"), 
выполнена асинхронная загрузка данных из MongoDB в связке с backend сервером Express.  
(***для демонстрации проекта имитирутся работа серверной части  и написаны заглушки c  данными в формате  JSON - папка data***)
(После входа на сайт под зарегистрированным  логином и паролем на страницах становятся доступны фунциии - Добавления, Удаления и Редактирования  
 в разделе "Комментарии", в разделе "Интересное" и "Блоги" -  только Добавление.  (Список пользователей и паролей из users_data.json: admin - 12345, author - 67891 и т.д.))


Для запуска проекта:
1) copy - paste stories)  
2) установить Node.js 
3) установить нужные модули - "npm  i"
4) сборка и запуск локального сервера - "webpack  -w" (сборка из  папки src в папку dist)

***Для запуска полной версии проекта с MongoDB***:
1) copy - paste stories)  
2) установить Node.js 
3) установить нужные модули - "npm  i"
4) установить MongoDB
5) закомментировать && раскомментировать данные строки в файлах:
Каталог
.../src/app/components/
blogsContent.js
заглушить строку - 20 , открыть строку - 21
AuthorInfo.js
заглушить - 16 , открыть - 17
authorsList.js
заглушить - 16 , открыть - 17
modal.js
заглушить - 23 , открыть - 24
Каталог
.../src/app/stores/
commentsStore.js
заглушить - 32 , открыть - 33
interestStore.js
заглушить - 29 , открыть - 30
6) запуск MongoDB в папке проекта
.../db
 mongod  --dbpath .../.../текущий путь проекта/db
7) запуск backend сервера Express в папке проекта
... /src/node server
8) сборка и запуск локального сервера - "webpack  -w" (сборка из  папки src в папку dist)
