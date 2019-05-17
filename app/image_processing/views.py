# coding: utf-8

from flask import render_template
from . import image_processing_bp


@image_processing_bp.route('/', methods=['GET', 'POST'])
def reverse_gif():
    return render_template('reverse_gif.html')
