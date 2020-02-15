from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    add_result = add(a, b)
    
    return f"The result is: {add_result}"
    

@app.route('/sub')
def subtration():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    sub_result = sub(a, b)

    return f"The result is: {sub_result}"

@app.route('/mult')
def multiplication():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    mult_result = mult(a, b)

    return f"The result is: {mult_result}"

@app.route('/div')
def division():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    div_result = div(a, b)

    return f"The result is: {div_result}"

    
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<operator>')
def calc_math(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    foo = operators[operator](a, b)

    return f"The result is: {foo}"
