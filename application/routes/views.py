from flask import Blueprint, request

views = Blueprint('views', __name__)

@views.route("/")
def index():
  return "Hello, World!"