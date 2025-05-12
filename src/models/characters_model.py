from src.models import db, ma

class Character(db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    
    def __repr__(self):
        return f"<Character {self.name}>"
    
class CharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    type = ma.String()
    gender = ma.String()
    image = ma.String()
    

class CharactersOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    image = ma.String()

character_output = CharacterOutput()
characters_output = CharactersOutput(many=True)