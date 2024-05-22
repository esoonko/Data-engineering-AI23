
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)

@app.route('/')
def index():
    # Retrieve data from the database
    users = Users.query.all()
    user_list = [user.username for user in users]
    return f'Users: {", ".join(user_list)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
