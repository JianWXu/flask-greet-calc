from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route('/math/<method>')
def math_method(method):
    arg1 = int(request.args.get('a'))
    arg2 = int(request.args.get('b'))
    answer = operators[method](arg1, arg2)
    return f"<h1>The answer is {answer}"


@app.route("/add")
def math_add():
    arg1 = int(request.args.get('a'))
    arg2 = int(request.args.get('b'))
    answer = add(arg1, arg2)
    return f"<h1>The answer is {answer}"


@app.route("/sub")
def math_sub():
    arg1 = int(request.args.get('a'))
    arg2 = int(request.args.get('b'))
    answer = sub(arg1, arg2)
    return f"<h1>The answer is {answer}"


@app.route("/mult")
def math_mult():
    arg1 = int(request.args.get('a'))
    arg2 = int(request.args.get('b'))
    answer = mult(arg1, arg2)
    return f"<h1>The answer is {answer}"


@app.route("/div")
def math_div():
    arg1 = int(request.args.get('a'))
    arg2 = int(request.args.get('b'))
    answer = div(arg1, arg2)
    return f"<h1>The answer is {answer}"
