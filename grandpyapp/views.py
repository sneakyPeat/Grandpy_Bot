from flask import Flask, render_template, jsonify, request
from grandpyapp.query import Query

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/', methods=['POST'])
def submit():
    query = request.form['query']
    response = Query(query)
    response = response.collect_data()
    return jsonify({"json": response})
