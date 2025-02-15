from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_URI = "mysql+mysqlconnector://admin:progknowledge@database-1.czsimoaie7x7.ap-south-1.rds.amazonaws.com/test_msql"

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
    return "connected to the db"

if __name__ == "__main__":
    app.run(debug=True)