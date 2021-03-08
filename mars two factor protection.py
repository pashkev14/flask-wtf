from flask import Flask, render_template, url_for
from werkzeug.utils import redirect
from accsessform import AccessForm


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
    return render_template('auto_answer.html', form=pre_form, css=css)


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


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
