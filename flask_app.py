from email.policy import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# create connection to a database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost:5432/todoapp"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr(self):
        return f'<Todo id={self.id} description={self.description}>'


# db.create_all()

@app.route("/")
def index():
    person = Person.query.first()
    return "hello world! my name is {}".format(person.name)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug="true")