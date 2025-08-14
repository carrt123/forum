from flask import Flask
import config
from exts import db, migrate
from buleprints.cms import bp as cms_bp
from buleprints.front import bp as front_bp
from buleprints.user import bp as user_bp
from models import user

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db.init_app(app)
migrate.init_app(app, db)


app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(user_bp)