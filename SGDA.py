from flask import Flask, render_template
app = Flask(__name__)

classrooms = [
    {
        'name': '30 PAIII/Edif. Aulas',
        'value': 1
    },
    {
        'name': '34 Edif. Aulas',
        'value': 2
    },
    {
        'name': '29 PAIII/Edif. Aulas',
        'value': 3
    },
    {
        'name': '5 CCCT',
        'value': 4
    },
    {
        'name': '9 PBIII',
        'value': 5
    },
    {
        'name': '5 ICARO',
        'value': 6
    },
    {
        'name': '9 ICARO',
        'value': 7
    }
]




@app.route("/")
@app.route("/home")
def hello():
    return render_template('index.html', classrooms=classrooms)

if __name__ == '__main__':
    app.run(debug=True)