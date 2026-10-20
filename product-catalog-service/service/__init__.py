"""Flask application for the Product Catalog Service"""
from flask import Flask
from service import config

app = Flask(__name__)
app.config.from_object(config)

# pylint: disable=wrong-import-position
with app.app_context():
    from service import routes, models  # noqa: F401, E402
    from service.common import error_handlers  # noqa: F401, E402

models.Product.init_db(app)
