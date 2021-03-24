from app import db


class PlaceHolder(db.Model):
    __tablename__ = 'place_holder'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name
        }

