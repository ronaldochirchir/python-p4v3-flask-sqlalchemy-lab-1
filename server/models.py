from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, CheckConstraint
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("magnitude >= 0", name="check_magnitude_non_negative"),
        CheckConstraint("year >= 0", name="check_valid_year"),
    )

    def __repr__(self):
        return f"<Earthquake {self.id}: {self.magnitude}M at {self.location}, {self.year}>"
