from flask import Flask

def create_app():

    app = Flask(__name__)

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()
    
    return app