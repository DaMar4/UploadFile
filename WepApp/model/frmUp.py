from email.mime import image
from msilib.schema import File
import re
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import FileField
class UpFile(FlaskForm):
    image = FileField('Image File')