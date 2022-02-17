from WepApp.module.index import index
from flask import Flask
from flask_uploads import configure_uploads, UploadSet, IMAGES
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import secrets
app = Flask(__name__)
secretkey = secrets.token_urlsafe(64)
app.config['SECRET_KEY'] = secretkey
app.config['UPLOADED_IMAGES_DEST'] = 'upload/images'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)
app.register_blueprint(index)
