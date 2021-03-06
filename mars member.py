from flask import Flask, render_template, url_for
import os
from werkzeug.utils import redirect
from accsessform import AccessForm
from fileform import FileForm
import json
import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    sim_img = url_for('static', filename='images/sim.jpg')
    train_img = url_for('static', filename='images/train.jpg')
    css = url_for('static', filename='css/training.css')
    return render_template('training.html', prof=prof.lower(), image_sim=sim_img, image_train=train_img, css=css)


@app.route("/list_prof/<list>")
def show_list(list):
    prof_list = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                 'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                 'штурман', 'пилот дронов'
                 ]
    css = url_for('static', filename='css/base.css')
    return render_template('list.html', prof_list=prof_list, list=list, css=css)


@app.route('/answer')
@app.route('/auto_answer')
def show_form():
    pre_form = {  # НИКТО НЕ ЗАПРЕЩАЕТ ВСТАВИТЬ СВОИ ЗНАЧЕНИЯ, НА ТО ЭТО И АВТОМАТИЧЕСКАЯ ФОРМА
        "Фамилия": "Watny",
        "Имя": "Mark",
        "Образование": "Выше среднего",
        "Профессия": "Штурман марсохода",
        "Пол": "male",
        "Мотивация": "Всегда мечтал застрять на Марсе!",
        "Готовы остаться на Марсе?": "True"
    }
    css = url_for('static', filename='css/base.css')
    return render_template('auto_answer.html', form=pre_form, css=css, title="Анкета")


@app.route('/login', methods=['GET', 'POST'])
def login():
    image = url_for('static', filename='images/mars emblem.png')
    css = url_for('static', filename='css/base.css')
    form = AccessForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form, image=image, css=css)


@app.route('/success')
def success():
    return '<h2>Доступ разрешен</h2>'


@app.route('/distribution')
def distribute():
    css = url_for('static', filename='css/base.css')
    astro_list = [  # ОПЯТЬ ЖЕ, НИКТО НЕ МЕШАЕТ ПОСТАВИТЬ СВОИ ЗНАЧЕНИЯ
        'Ридли Скотт',
        'Энди Уир',
        'Марк Уотни',
        'Венката Капур',
        'Тедди Сандерс',
        'Шон Бин'
    ]
    return render_template('distribution.html', astros=astro_list, css=css)


@app.route('/table_param/<sex>/<int:age>')
def show_room(sex, age):
    css = url_for('static', filename='css/base.css')
    image_adult = url_for('static', filename='images/adult_martian.jpg')
    image_kid = url_for('static', filename='images/kid_martian.jpg')
    return render_template('room.html', img_kid=image_kid, img_adult=image_adult, css=css, sex=sex, age=age)


@app.route('/galery', methods=["GET", "POST"])
def show_carousel():
    css = url_for('static', filename='css/base.css')
    images = [url_for('static', filename=f'images/carousel/{j}') for currentdir, dirs, files in os.walk(os.path.join(app.root_path, 'static', 'images', 'carousel')) for j in files]
    form = FileForm()
    if form.validate_on_submit():
        file = form.field.data
        file.save(os.path.join(app.root_path, 'static', 'images', 'carousel', file.filename))
        return redirect('/galery')
    return render_template('carousel.html', images=images, css=css, form=form)


@app.route('/member')
def show_profile():
    with open('templates/members.json', mode='r', encoding='utf-8') as jsfile:
        data = json.load(jsfile)
        rand_name = random.choice(list(data.keys()))
        member = {f"{rand_name}": {"photo": url_for('static', filename=f'images/{data[rand_name]["photo"]}'),
                                   "specialities": sorted(data[rand_name]["specialities"])}}
        return render_template('profile.html', member=member)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
