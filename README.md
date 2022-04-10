# Поиск пути между ссылками на Википедии

## Описание 
Программа на вход получает две ссылки.

Программа выводит за какое количество переходов можно дойти от первой ссылки до второй, переходя только по ссылкам на открывающихся страницах, а также путь - последовательность ссылок, по которым нужно идти, чтобы попасть из первой ссылки во вторую.

Программа реализованна в соответствии с паттерном «Очередь задач». Работает только для англоязычной версии википедии. 

## Запуск

1. `docker-compose up rabbit-mq`
2. `docker-compose up message_queue`
3. `python client.py`

Все команды необходимо осуществлять в разных окнах терминала и строго в таком порядке. 