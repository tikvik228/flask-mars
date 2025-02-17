from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


slogan = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
          "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]

res = '<br>'.join(slogan)


@app.route('/promotion')
def promotion():
    return res


@app.route('/image_mars')
def image_mars():
    res = f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <mets charset="UTF-8">
                <title>Привет, Марс!</title>
            </head>
            <body>
                <h1>Жди нас, марс!</h1>
                <img src="{url_for('static', filename='image/mars.jpg')}"
                alt="здесь должна была быть картинка марса">
                <p>Вот она какая, красная планета.</p>
            </body>
            </html>"""
    return res


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')