from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['sgda']


@app.route("/")
@app.route("/home")
def hello():
    classrooms = db.aulas.find()
    return render_template('index.html', classrooms=classrooms)

if __name__ == '__main__':
    app.run(debug=True)