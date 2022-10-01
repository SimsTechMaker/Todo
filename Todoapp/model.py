from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .route import app

db = SQLAlchemy(app)

class Theme_tache(db.Model):
    __tablename__ = "Theme_tache"
    id = db.Column(db.Integer, primary_key=True)
    nom_theme = db.Column(db.String(50), nullable=False)
    #liesion avec les taches 
    tache = db.relationship("Tache",
                            backref = db.backref("Theme_tache", cascade='all,delete')
                            )

    def __init__(self,nom_theme) -> None:
        self.nom_theme = nom_theme

        
class Tache(db.Model):
    __tablename__ = "Tache"
    id = db.Column(db.Integer, primary_key=True)
    theme_key = db.Column(db.Integer, db.ForeignKey("Theme_tache.id"))
    description = db.Column(db.String(500), nullable = False)
    
    def __init__(self, description) -> None:
        self.description = description
        
def init_db():
    db.drop_all()
    db.create_all()
    theme_init = Theme_tache("Defaut")
    db.session.add(theme_init)
    db.session.commit()
    
    tache_init = Tache("Bonjour nous sommes a l'initialisation de la tache")
    
    tache_init2 = Tache("Bonjour nous sommes a l'initialisation de la tache deux")
    db.session.add(tache_init)
    db.session.add(tache_init2)
    db.session.commit()
    return "Initialisation Done"

init_db()
    
