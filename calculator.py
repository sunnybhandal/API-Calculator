# import Flask and jsonify
from flask import Flask, jsonify, request, abort, render_template
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import math

app = Flask(__name__)

@app.route('/add')
def add_args():
    # create request parser
    parser = reqparse.RequestParser()

    # Create arguments
    parser.add_argument('arg1', type=int)
    parser.add_argument('arg2', type=int)

    arg1 = parser.parse_args().get('arg1')
    arg2 = parser.parse_args().get('arg2')

    answer = arg1 + arg2

    return (jsonify({'answer':answer}))

@app.route('/subtract')
def subtract_args():
    # create request parser
    parser = reqparse.RequestParser()

    # Create arguments
    parser.add_argument('arg1', type=int)
    parser.add_argument('arg2', type=int)

    arg1 = parser.parse_args().get('arg1')
    arg2 = parser.parse_args().get('arg2')

    answer = arg1 - arg2

    return (jsonify({'answer':answer}))

@app.route('/multiply')
def multiply_args():
    # create request parser
    parser = reqparse.RequestParser()

    # Create arguments
    parser.add_argument('arg1', type=int)
    parser.add_argument('arg2', type=int)

    arg1 = parser.parse_args().get('arg1')
    arg2 = parser.parse_args().get('arg2')

    answer = arg1 * arg2

    return (jsonify({'answer':answer}))

@app.route('/divide')
def divide_args():
    # create request parser
    parser = reqparse.RequestParser()

    # Create arguments
    parser.add_argument('arg1', type=int)
    parser.add_argument('arg2', type=int)

    arg1 = parser.parse_args().get('arg1')
    arg2 = parser.parse_args().get('arg2')

    answer = arg1 / arg2

    return (jsonify({'answer':answer}))


if __name__ == '__main__':
    app.run(debug=True)