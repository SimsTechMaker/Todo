from cmath import inf
from statistics import mode
from . import model

def commit():
    model.db.session.commit()

def add_theme(nom_theme):
    model.db.session.add(model.Theme_tache(nom_theme))
    commit()

def add_tache(description, id_theme):
    tmp = model.Tache(description)
    tmp.theme_key = id_theme
    model.db.session.add(tmp)
    commit()
    
    
def drop_theme(id_thme):
    model.db.session.query(model.Theme_tache).filter_by(id= id_thme).delete()
    commit()

def drop_tache(id_tache):
    model.db.session.query(model.Tache).filter_by(id = id_tache).delete()
    commit()

def update_tache(id_tache, valeur):
    model.db.session.query(model.Tache).filter_by(id=int(id_tache)).update({"description": valeur})
    commit()

def update_theme(id_theme, valeur):
    model.db.session.query(model.Tache).filter_by(id=int(id_theme)).update({"nom_theme": valeur})
    commit()
    
def get_tache(id_tache=None):
    data = []
    for info in model.db.session.query(model.Tache).order_by(model.Tache.id):
        if info.id == id_tache:
            data.append(info.description)
    commit()
    return data

def get_theme(id_theme=None):
    data =[]
    for info in model.db.session.query(model.Theme_tache).order_by(model.Theme_tache.id):
        data.append(info.id)
        if info.id == id_theme:
            commit()
            return info
    commit()
    return max(data)
    
    


a = get_theme(1)
print(type(a))
print(a.nom_theme)
add_theme("OssTutto")

a = get_theme()
print(a)

add_tache("bonjour le monde",a)
add_tache("bonjour le monde2",1)
add_tache("bonjour le monde3",1)
add_tache("bonjour le monde3",1)

drop_tache(6)
drop_theme(1)






