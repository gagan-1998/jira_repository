from pymongo import MongoClient
from flask import *

app = Flask(__name__)

#client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
client = MongoClient("mongodb+srv://test:test@cluster0.sfliq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('form_data')

@app.route('/')
def jf_data():
    return render_template('details.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    data = {};
    if request.method == 'POST':
        data['Title'] = request.form['Title']
        data['Description'] = request.form['Description']
        data['Jira_Project_ID'] = request.form['Jira_Project_ID']
        db.formData.insert_one(data)
        return render_template("result.html")


if __name__ == '__main__':
    app.run(debug=False)