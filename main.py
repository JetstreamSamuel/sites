from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.<br>
              Человечеству мала одна планета.<br>
              Мы сделаем обитаемыми безжизненные пока планеты.<br>
              И начнем с Марса!<br>
              Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return f"""
    <!doctype HTML>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Привет, Марс!</title>
      </head>
      <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/mars.png')}">
      </body>
    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""
    <!doctype HTML>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.2.1/dist/css/bootstrap.min.css" 
        integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" 
        crossorigin="anonymous">
        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        <title>Привет, Марс!</title>
      </head>
      <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/mars.png')}">
        <div class="alert alert-dark">Человечество вырастает из детства.</div>
        <div class="alert alert-success">Человечеству мала одна планета.</div>
        <div class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
        <div class="alert alert-warning">И начнем с Марса!</div>
        <div class="alert alert-danger">Присоединяйся!</div>
      </body>
    </html>"""


@app.route('/astronauts', methods=['GET', 'POST'])
def astronauts():
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" 
                            />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input class="form-control" id="surname" placeholder="Введите фамилию" 
                                    name="surname">
                                    <input class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br></br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                                    placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Общее образование</option>
                                          <option>Высшее образование</option>
                                        </select>
                                     </div>
                                     <br>Какие у вас есть профессии?</br>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" 
                                        name="explorer">
                                        <label for="classSelect">Инженер-исследователь</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" 
                                        name="builder">
                                        <label for="classSelect">Инженер-строитель</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" 
                                        name="pilot">
                                        <label for="classSelect">Пилот</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" 
                                        name="meteorolog">
                                        <label for="classSelect">Метеоролог</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" 
                                        name="medic">
                                        <label for="classSelect">Инженер по жизнеобеспечению</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" 
                                        name="radioshield">
                                        <label for="classSelect">Инженер по радиационной защите</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" 
                                        name="biolog">
                                        <label for="classSelect">Экзобиолог</label>
                                    </div>

                                    <div class="form-group" style="padding-top:20px;">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" 
                                          checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check" >
                                          <input class="form-check-input" type="radio" name="sex" id="female" 
                                          value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group" style="padding-top:20px;">
                                        <label for="about">Почему вы хотите принять участие в миссии</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group" style="padding-top:20px;">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check" style="padding:20px;">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?
                                        </label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('education'))
        print(request.form.get('explorer'))
        print(request.form.get('builder'))
        print(request.form.get('pilot'))
        print(request.form.get('meteorolog'))
        print(request.form.get('medic'))
        print(request.form.get('radioshield'))
        print(request.form.get('biolog'))
        f = request.files.get('file')
        if f:
            print(f.read())
        print(request.form.get('about'))
        print(request.form.get('accept'))
        print(request.form.get('sex'))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    planets = {
        "Меркурий": ["Эта планета относительно близка к Земле;", "Эта планета первая в Солнечной системе",
                     "Она крутая;", "Есть ТЦ такой", "Давай дальше."],
        "Венера": ["Эта планета близка к Земле;", "На ней много необходимых ресурсов;",
                   "Вторая по удалённости от Солнца и шестая по размеру планета Солнечной системы;",
                   "Радиус Венеры 6052 км, а масса составляет 81% от массы нашей планеты;", "Она просто красивая!"],
        "Земля": ["Это наша любимая Земля;", "На ней много солёной воды;", "На ней есть магнитное поле;",
                  "На ней есть много ресурсов;", "НАША ЛЮБИМАЯ ПЛАНЕТА!"],
        "Марс": ["Эта планета близка к Земле;", "На ней много необходимых ресурсов;", "На ней есть вода и атмосфера;",
                 "На ней есть небольшое магнитное поле;", "Она просто красивая!"],
        "Юпитер": ["Это крупнейшая планета Солнечной системы;", "ТЦ такой есть", "Идём дальше",
                   "Ты Венера, я Юпитер...", "Ну вы поняли."],
        "Сатурн": ["Шестая планета по удалённости от Солнца и вторая по размерам планета",
                   "Так называли американские ракеты", "У этой планеты есть кольца", "Крутая планета", "Дальше."],
        "Уран": ["Была открыта в 1781 году", "Уран – это седьмая по удаленности от Солнца планета",
                 "Такой химический элемент есть", "Его открыл Уильям Гершель", "Это крутая планета."],
        "Нептун": ["Тик токер такой есть", "Планета с кайфом", "Надо её захватить",
                   "НА ШТУРМ!", "Уже не знаю что писать("],
        "Плутон": ["Это не планета", "Это не планета", "Это не планета",
                   "Это не планета", "Это не планета"]
    }
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous">
            </script>
            <title>Вариант выбора</title>
        </head>
        <body>
            <h1>Мое предложение: {planet_name}</h1>
            <h2>{planets[planet_name][0]}</h2>
            <h2 class="text-success bg-success bg-opacity-25">{planets[planet_name][1]}</h2>
            <h2 class="bg-secondary bg-opacity-25">{planets[planet_name][2]}</h2>
            <h2 class="text-warning bg-warning-subtle bg-opacity-25">{planets[planet_name][-2]}</h2>
            <h2 class="text-danger bg-danger-subtle bg-opacity-25">{planets[planet_name][-1]}</h2>
        </body>
    </html>
"""


@app.route('/carousel')
def carousel():
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" 
            integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous">
            </script>
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Вариант выбора</title>
        </head>
        <body>
            <h1>Пейзажи Марса</h1>
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6">
                    <div id="carouselExampleIndicators" class="carousel slide">
                  <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" 
                    class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" 
                    aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" 
                    aria-label="Slide 3"></button>
                  </div>
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img src="{url_for('static', filename='img/first.png')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                      <img src="{url_for('static', filename='img/second.png')}" class="d-block w-100" alt="...">
                    </div>
                    <div class="carousel-item">
                      <img src="{url_for('static', filename='img/free.png')}" class="d-block w-100" alt="...">
                    </div>
                  </div>
                  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" 
                  data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                  </button>
                  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" 
                  data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                  </button>
                </div>
                </div>
                <div class="col-3"></div>
            </div>
        </body>
    </html>
"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
