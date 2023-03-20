import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта Python

tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

print(title)  # выводим полученный заголовок страницы

#//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]/a

import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('body/div//div[3]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл? в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    #print(a.text)  # из этого тега забираем текст — это и будет нашим названием

#Задание 18.4.5
#Используя полученные знания, допишите сделанный в начале юнита скрипт
# (где мы доставали заголовки новостей о Python с Python.org) так,
# чтобы он показывал ещё и дату добавления новости.

#Примечание: Для получения атрибутов тега (т. е. его дополнительных параметров)
# используется метод .get(<имя атрибута>).

#Решение

    time = li.find('time')
    print(time.get('datetime'), a.text) # из этого тега забираем текст -
    # это и будет нашим названием