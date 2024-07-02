from .fibonaci import get_nth_member
from .input_validation import query_validation


from flask import Blueprint
route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route("/<n>")
def fibonacci(n):
    n = query_validation(n)
    nth = get_nth_member(n)
    return str(nth)
