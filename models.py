from db import db

class CityModel(db.Model):
    __tablename__ = "cities"

    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(25), unique=True, nullable=False)