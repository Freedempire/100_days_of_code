import csv

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from cafe_form import CafeForm


def get_cafes():
    with open(cafes_filename, encoding='utf-8') as f:
        return list(csv.DictReader(f))

def get_titles(table):
    return [(key, key) for key in table[0].keys()]

def anchorize(cafes):
    for cafe in cafes:
        cafe['Location'] = f'<a href={cafe["Location"]}>Maps Link</a>'

def process_adding_form(form):
    cafe = [
        form.name.data,
        form.location.data,
        form.opening_time.data.strftime('%H:%M'),
        form.closing_time.data.strftime('%H:%M'),
        int(form.coffee_rating.data) * '☕',
        int(form.wifi_strength_rating.data) * '💪' or '❌',
        int(form.power_socket_availability.data) * '🔌' or '❌'
    ]
    try:
        with open(cafes_filename, 'a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(cafe)
    except Exception as e:
        print(e)

cafes_filename = 'cafe_data.csv'
app = Flask(__name__)
app.secret_key = ('some secret key')
bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cafes')
def cafes():
    cafes = get_cafes()
    anchorize(cafes)
    return render_template('cafes.html', table=cafes, titles=get_titles(cafes))

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        process_adding_form(form)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
