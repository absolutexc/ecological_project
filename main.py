#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

# def result_calculate(first, second, third):
#     dep_coef = 100
#     trubs_coef = 0.04
#     class_coef = 5   
#     first = 1
#     return first * dep_coef + second * trubs_coef + third * class_coef

def result_calculate(first, second, third):
    dep_coef = 100
    trubs_coef = 5
    class_coef = 5
    # first = 1
    return first * dep_coef + second * trubs_coef + third * class_coef

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html')
#Вторая страница

@app.route('/<first>')
def trubs(first):
    return render_template(
                            'truba.html', 
                            first=first
                           )

#Третья страница
@app.route('/<first>/<second>')
def electronics(first, second):
    return render_template(
                            'type.html',                           
                            first=first, 
                            second=second                           
                           )

#Расчет
@app.route('/<first>/<second>/<third>')
def end(first, second, third):
    return render_template('result.html', 
                            result=result_calculate(int(first),
                                                    int(second), 
                                                    int(third)
                                                    )
                        )
#Форма
@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    name = request.form['name']
    address = request.form['address']
    date = request.form['date']
    email = request.form['email']
    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(f"Имя: {name}\n")
        f.write(f"Адрес: {address}\n")
        f.write(f"Дата: {date}\n")
        f.write(f"Эл. почта: {email}\n")
        f.write(f"-------\n")

    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,
                           address=address,
                           date=date,
                           email=email
                           )

app.run(debug=True)