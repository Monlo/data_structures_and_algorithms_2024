# flask_app.py
from flask import Flask, render_template, request
from helper import perform_calculation, convert_to_float

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', printed_result='')

@app.route('/calculate', methods=['POST'])
def calculate():
    value1 = request.form['value1']
    value2 = request.form['value2']
    operation = str(request.form['operation'])

    try:
        value1 = convert_to_float(value1)
        value2 = convert_to_float(value2)
    except ValueError as e:
        return render_template('index.html', printed_result=str(e))

    try:
        result = perform_calculation(value1, value2, operation)
        return render_template('index.html', printed_result=f'Result: {result}')
    except ValueError as e:
        return render_template('index.html', printed_result=str(e))

if __name__ == '__main__':
    app.run(debug=True)
