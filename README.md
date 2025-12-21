
## Запуск проекта

### С помощью Docker Compose
1. `docker-compose up --build`

### Альтернативный способ
1. `docker build -t steinadler-demo .`
2. `docker run -p 7860:7860 steinadler-demo`

## Демонстрация

Вы можете зайти на данное демо по [ссылке](https://diploma.vadimslab.ru)

## Описание

Данный проект работает по схеме `internet <-> VPS <-> PC`. 

* VPS - виртуальный приватный сервер с белым IP и настроенным VPN, выполняет роль прокси сервера на базе apache.
* PC - компьютер на котором запущено данное демо, находится в одном VPN вместе с VPS.

## Настройка Apache на VPS

### Установка и настройка
1. `sudo apt update && sudo apt install apache2`
2. `sudo a2enmod proxy proxy_http proxy_wstunnel ssl headers rewrite`
3. Скопируйте конфигурацию из `assets/apache/steinadler-demo.conf` в `/etc/apache2/sites-available/`
4. `sudo a2ensite steinadler-demo`
5. `sudo a2dissite 000-default`
6. `sudo systemctl reload apache2`

### SSL сертификат
1. `sudo apt install certbot python3-certbot-apache`
2. `sudo certbot --apache -d diploma.vadimslab.ru`

### Проверка конфигурации
- `sudo apachectl -t` - проверка синтаксиса
- `sudo apachectl -S` - просмотр виртуальных хостов
   