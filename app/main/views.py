# coding: utf-8

from flask import render_template
from . import main_bp


@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
