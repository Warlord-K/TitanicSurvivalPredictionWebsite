from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "Data"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=True)
    Gender = db.Column(db.String(10))
    Age = db.Column(db.Integer)
    Class = db.Column(db.String(10))
    Married = db.Column(db.String(5))

    def __init__(self,Name,sex,age,income,married):
        self.Name = Name
        self.sex = sex
        self.age = age
        self.income = income
        self.married = married
