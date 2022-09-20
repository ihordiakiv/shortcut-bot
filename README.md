### Загрузка 

Выполнить в теримнале

`git clone https://github.com/ihordiakiv/shortcut_bot.git`

`cd shortcut-bot`

В корне проекта создать файл ```.env``` 
Пример файла ```default.env```

Создать ```SHORTCUT_API_TOKEN``` на странице https://app.shortcut.com/happify/settings/account/api-tokens
и записать в файл ```.env```.

### Install Docker 

https://docs.docker.com/get-docker/

### Запуск

Выполнить в теримнале:

сборка проекта

```docker build . --tag shortcut```

запуск

```docker run --mount src="$(pwd)",target=/usr/src,type=bind -p 8000:8000 shortcut```

В браузере зайти по адресу http://0.0.0.0:8000/docs

Загруженные файлы находяться в папке ```./downloads/``` в корне проекта.

