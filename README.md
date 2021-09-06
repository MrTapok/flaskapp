# flaskapp
Пояснения:

Для создания приложения использовался flask. Так как было требование использовать JSON как входные данные, методы работают с помощью POST (чтобы заработали сценарии curl).
Поиск по ID и поиск с фильтрацией могут работать и через GET. JSON-ы по которым происходит поиск с фильтрацией выглядят как '{"name":"что-то","properties":["что-то":"что-то"]}',
так как в ТЗ было указание на использование массива пар ключ-значение. Можно делать поиск только по имени или только по значению одного из properties. Проверки на полное
совпадение формата данных нет, есть обработка плохо созданных JSON-ов, которые не парсятся.

Настройки:
  
docker run -d -p 27017:27017 -v ~/mongodb:/data/db --name itemsdata mongo
pip install -r requirements.txt
app.py (Windows) / python3 app.py (Остальное)

Curl-сценарии:
  
curl -X POST http://192.168.1.101:5000/create_item
   -H 'Content-Type: application/json'
   -d '{"name":"Iphone 11 white","description":"It is Iphone 11 white", "properties":[{"creator":"Apple"},{"cost":20000},{"color":"white"}]}'
curl -X POST http://192.168.1.101:5000/create_item
   -H 'Content-Type: application/json'
   -d '{"name":"Iphone 12 black","description":"It is Iphone 12 black", "properties":[{"creator":"Apple"},{"cost":30000},{"color":"black"}]}'
curl -X POST http://192.168.1.101:5000/create_item
   -H 'Content-Type: application/json'
   -d '{"name":"Iphone 11 black","description":"It is Iphone 11 black", "properties":[{"creator":"Apple"},{"cost":20000},{"color":"black"}]}'
curl -X POST http://192.168.1.101:5000/create_item
   -H 'Content-Type: application/json'
   -d '{"name":"Xiaomi black","description":"It is Xiaomi black", "properties":[{"creator":"Mi"},{"cost":30000},{"color":"black"}]}'
curl -X POST http://192.168.1.101:5000/create_item
   -H 'Content-Type: application/json'
   -d '{"name":"Xiaomi white","description":"It is Xiaomi white", "properties":[{"creator":"Mi"},{"cost":20000},{"color":"white"}]}'


curl -X POST http://192.168.1.101:5000/id_search
   -H 'Content-Type: application/json'
   -d '{"_id":"вставьте сюда любой id который вернул create_item"}'

curl -X POST http://192.168.1.101:5000/get_item
   -H 'Content-Type: application/json'
   -d '{"name":"Iphone"}'
curl -X POST http://192.168.1.101:5000/get_item
   -H 'Content-Type: application/json'
   -d '{"properties":["color":"black"]}'
curl -X POST http://192.168.1.101:5000/get_item
   -H 'Content-Type: application/json'
   -d '{"name":"Iphone","properties":["color":"black"]}'
