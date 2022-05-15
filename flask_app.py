from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# create connection to a database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost:5432/family"
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = "persons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route("/")
def index():
    return "hello world! again makes sense too much. i prefer this one"


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug="true")