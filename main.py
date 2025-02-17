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
    res_image = f"""<!DOCTYPE html>
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
    return res_image


@app.route('/promotion_image')
def promotion_image():
    picture_url = url_for('static', filename='image/mars.jpg')
    style_url = url_for('static', filename='css/style.css')
    prom_res = f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <mets charset="UTF-8">
                 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{style_url}" />
                <title>Колонизация</title>
            </head>
            <body>
                <h1>Жди нас, марс!</h1>
                <img src="{picture_url}"
                alt="здесь должна была быть картинка марса">
                <div class="alert-dark" role="alert">
                    <br><h3>{slogan[0]}</h3>
                </div>
                <div class="alert-success" role="alert">
                    <br><h3>{slogan[1]}</h3>
                </div>
                <div class="alert-secondary" role="alert">
                    <br><h3>{slogan[2]}</h3>
                </div>
                <div class="alert-warning" role="alert">
                    <br><h3>{slogan[3]}</h3>
                </div>
                <div class="alert-danger" role="alert">
                    <br><h3>{slogan[4]}</h3>
                </div>
            </body>
            </html>"""
    return prom_res


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')