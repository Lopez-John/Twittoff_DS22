"""Main app/routing file for Twitoff."""

from flask import Flask, render_template
from .models import DB, User, insert_example_users

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite:///db.sqlite3'
    app.congfig['SQLALCHEMY_TRACKING_MODIFICATIONS'] = False

    DB.init_app(app)


    @app.route('/')
    def root:
        DB.drop_all()
        DB.create_all()
        insert_example_users()
        return render_template('base.html', title='Home',
                                users=User.query.all())

    @app.route('/goodbye')
    def goodby():
        return 'Goodbye Twitoff!'

    return app
