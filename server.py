from flask import Flask, render_template, url_for, redirect, request, jsonify
import util

app = Flask('__name__')

@app.route('/')
def main_app():
    return render_template('main.html')


@app.route('/get_species', methods = ['POST'])
def login():
    if request.method == 'POST':
        data = request.form
        species = util.predict(data)
        response = jsonify({'species': species})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

if __name__ == "__main__":
    app.run(debug = True)
