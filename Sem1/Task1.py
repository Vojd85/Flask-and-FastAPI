# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), 
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template
from collections import namedtuple

app = Flask(__name__)

Product = namedtuple('Product', 'name image price')

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/clothes/')
def clothes():
    products = [Product('Штаны', '/static/img/im3.jpg', 300 ), Product('Свитер', '/static/img/im1.jpg', 1200),
                Product('Майка', '/static/img/im4.jpg', 150)]
    return render_template('clothes.html', products = products)

@app.route('/shoes/')
def shoes():
    products = [Product('Берцы', 'Изображение', 4500 ), Product('Кроссовки', 'Изображение', 3000),
                Product('Шлёпки', '/static/img/im2.jpg', 270)]
    return render_template('shoes.html', products = products)

@app.route('/jacket/')
def jacket():
    products = [Product('Дождевик', 'Изображение', 2300 ), Product('Пальто', 'Изображение', 5200),
                Product('Пуховик', 'Изображение', 6350)]
    return render_template('jacket.html', products = products)


if __name__ == '__main__':
    app.run(debug=True)