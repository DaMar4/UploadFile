from flask import redirect, render_template
from flask.blueprints import Blueprint
from WepApp.model.frmUp import UpFile
from WepApp import images
index = Blueprint("index",__name__)
@index.route("/",methods=['GET','POST'])
def main():
    form = UpFile()
    if form.validate_on_submit():
        filename= images.save(form.image.data)
        return filename
    return render_template("index.html", form= form)