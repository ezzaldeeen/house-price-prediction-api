import os
from flask import Flask, jsonify
# import the controller blueprint
from src.controller.routes import controller_blueprint

app = Flask(__name__)

# setting-up the app configration
app_config = os.getenv(
    'APP_CONFIGURATION',
    default='src.config.DevelopmentConfig'
)
app.config.from_object(app_config)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404


# register the controller blueprint
app.register_blueprint(controller_blueprint)
