from flask import Flask, url_for, request

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
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/mars_form.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Выше среднего</option>
                                          <option>Супер</option>
                                        </select>
                                     </div>
                                     <form>
                                        <label for="city-select">Ваш город</label>
                                        <select name="city" id="city-select">
                                            <option value="">-- Выберите город --</option>
                                            <option value="petersburg">Санкт-Петербург</option>
                                            <option value="samara">Самара</option>
                                            <option value="perm">Пермь</option>
                                            <option value="novosibirsk">Новосибирск</option>
                                        </select>
                                     </form>
                                     
                                     
                                     
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')