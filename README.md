# Тестовое задание #
Задача:

Сделать web-сервис позволяющий узнать текущую загрузку ЦПУ, ОЗУ, ГПУ(при наличии), а также сохраняющий время запроса(MM:DD:hh:mm:ss), метод запроса и отправляемые данные в Redis.


Взаимодействие с сервисом происходит посредством GET и POST запросов:


1) GET запрос получения всех видов загрузки (ЦПУ, ОЗУ, ГПУ)


2) POST запрос получения определенных видов загрузки. Тип запрашиваемой загрузки передается в JSON формате.


3) GET запрос получения всех записей из Redis в формате JSON, где ключ - это время запроса, а значение – метод и отправленные данные.


4) POST запрос очистки записей в Redis. Вместе с запросом может посылаться JSON с промежутком по времени (MM:DD:hh:mm:ss), в таком случае удаление производится в заданном диапазоне, иначе удаляются все записи.


Технологии выбираются самостоятельно (Обязательно должен быть только Redis). Если есть непонятные места, или предложения по улучшению - то приветствуется импровизация

