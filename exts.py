from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache()