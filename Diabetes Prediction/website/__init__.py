# app.py

from flask import Flask, session
from .views import views
from .auth import auth
import joblib

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'NDHFIWBFEWAHF khdHDKABNFKB'
    app.config['USER_AUTHENTICATED'] = False

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Load the saved scaler and classifier during initialization
    scaler = joblib.load('scaler.joblib')
    classifier = joblib.load('classifier.joblib')

    # Save the scaler and classifier in the app context
    app.config['SCALER'] = scaler
    app.config['CLASSIFIER'] = classifier

    @app.before_request
    def before_request():
        # Pass the user_authenticated value to all templates
        session['user_authenticated'] = app.config['USER_AUTHENTICATED']

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
