from flask import Flask

# импорт функций страниц
from utils import candidates_page
from utils import main_page
from utils import skills_page

app = Flask(__name__)


# главня страница
@app.route('/')
def main():
    return main_page()


# страница с канлидатами
@app.route('/candidates/<num>')
def candidates(num):
    return candidates_page(num)


# страница с умениями
@app.route('/skills/<skill>')
def skills(skill):
    return skills_page(skill)


app.run('0.0.0.0', 8000)
