from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    # role = Column(String(10))


class Group(db.Model):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    # status = Column(String(10))



if __name__ == '__main__':
    app.run(debug=True)
