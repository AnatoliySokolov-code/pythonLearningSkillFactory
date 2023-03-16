# API(Application programming interface) — это набор публичных свойств и методов для взаимодействия с другими
# программами, которые могут быть написаны даже на другом языке
# программирования.  API через наш Python-скрипт с помощью библиотеки Requests.
# Для этого отправим гет-запрос:

import requests

r = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print(r.content)
import requests

#чтобы получить содержание ответа, надо обратится к полю content объекта
# response, который возвращается, когда приходит ответ от сервера через
# библиотеку Requests. У этого объекта на самом деле есть много полей,
# например, status_code, который говорит нам о том, какой вообще ответ пришёл.
# Давайте поменяем наш код и посмотрим, что программа выведет теперь.

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(r.status_code)  # узнаем статус полученного ответа

#Есть несколько категорий ответов, например:

#200, 201, 202 и т. д. — ответы, которые говорят, что с запросом всё хорошо,
# и ответ приходит правильный, т. е. его можно обрабатывать и как-либо
# взаимодействовать с ним. На самом деле почти все сервера всегда в ответ
# шлют именно ответ 200, а не какой-либо другой из этой же категории.
#300, 301 и т. д. — ответы, которые говорят, что вы будете перенаправлены
# на другой ресурс (не обязательно на этом же сервере).
#400, 401 и т. д. — ответы, которые говорят, что что-то неправильно с запросом.
# Запрашивается либо несуществующая страница (всем известная 404 ошибка),
# либо же недостаточно прав для просмотра страницы (403) т. д.
#501, 502 и т. д. — ответы, которые говорят, что с запросом всё хорошо,
# но вот на сервере что-то сломалось, и поэтому нормальный ответ прийти не
# может.

import requests
import json  # импортируем необходимую библиотеку

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
    print(text[:50], '\n')

#Давайте посмотрим теперь на ещё один тип возвращаемых значений.
# Он тоже будет JSON, но в данном случае он, скорее,  будет похож на словарь.

import requests
import json

r = requests.get('https://api.github.com')

print(r.content)

#теперь сделаем его настоящим словарём.

import requests
import json

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

#Давайте попробуем отправить post-запрос:

import requests

r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
print(r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет

#Обратите внимание, что здесь тип отправляемых нами данных указан как FORM,
# но многие API, однако, требуют тип JSON в качестве отправляемых данных.

#Давайте посмотрим, как с помощью уже знакомой нам библиотеки отправить данные
# в нужном нам формате JSON:
import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
print(r.content)