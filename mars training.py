from flask import Flask, render_template, url_for


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
