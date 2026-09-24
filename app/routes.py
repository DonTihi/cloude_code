from flask import Blueprint, render_template, request

from .calculator import add, parse_number

INVALID_INPUT_MESSAGE = "Please enter two valid numbers."

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    return render_template("index.html")


@bp.post("/calculate")
def calculate():
    try:
        a = parse_number(request.form["a"])
        b = parse_number(request.form["b"])
    except (KeyError, ValueError):
        return render_template("index.html", error=INVALID_INPUT_MESSAGE), 400

    return render_template("index.html", result=add(a, b))
