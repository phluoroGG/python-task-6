from flask import Flask
from flask import request, render_template

from logic import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/crossword', methods=['GET', 'POST'])
def crossword():
    image_path = request.form.get('f')
    cell_count = request.form.get('num')
    print(image_path)
    if image_path is not None:
        to_crossword(image_path, int(cell_count))

    image_path = request.form.get('solve')
    label = request.form.get('lab')
    if label is not None:
        if label == 'Решённый кроссворд':
            image_path = 1
        elif label == 'Нерешённый кроссворд':
            image_path = None
    if image_path is None:
        label = 'Решённый кроссворд'
        image_path = 'static/crossword.png'
    else:
        label = 'Нерешённый кроссворд'
        image_path = 'static/solved_crossword.png'

    return render_template('crossword.html', label=label, image_path=image_path)


if __name__ == '__main__':
    app.run(debug=True)
