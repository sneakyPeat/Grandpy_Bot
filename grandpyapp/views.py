from flask import render_template, jsonify, request
from grandpyapp.query import Query
from grandpyapp.start import app


@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/ajax', methods=['POST'])
def submit():
    query = request.form['query']
    response = Query(query)
    response = response.collect_data()
    return jsonify({"json": response})
