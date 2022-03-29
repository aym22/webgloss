from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_pages', __name__,
                        template_folder='templates')

@simple_pages.route('/index')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/welcome')
def welcome():
    try:
        return render_template('welcome.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/AAA_Testing')
def AAA_Testing():
    try:
        return render_template('AAA_Testing.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/OOPs')
def OOPs():
    try:
        return render_template('OOPs.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/SOLID')
def SOLID():
    try:
        return render_template('SOLID.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)
