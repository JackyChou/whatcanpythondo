# coding: utf-8

from flask import Blueprint

image_processing_bp = Blueprint(
    'image_processing_bp', __name__,
    template_folder='templates'
)

from . import views
