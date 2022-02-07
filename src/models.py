from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=False)

    @classmethod
    def register(cls, new_user):
        new_user = cls(**new_user)
        
        db.session.add(new_user)
        try:
            db.session.commit()
            return new_user
        except Exception as error:
            db.session.rollback()
            return None

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "gender": self.gender
            # do not serialize the password, its a security breach
        }