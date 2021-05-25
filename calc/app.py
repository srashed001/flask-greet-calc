# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div 

app = Flask(__name__)

@app.route("/add")
def add_args():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{add(a,b)}"

@app.route("/sub")
def sub_args():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{sub(a,b)}"

@app.route("/mult")
def mult_args():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{mult(a,b)}"

@app.route("/div")
def div_args():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f"{div(a,b)}"
