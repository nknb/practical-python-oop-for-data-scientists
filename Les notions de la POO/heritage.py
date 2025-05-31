# L'heritage est une manière d'organiser les objets dans une hiérachie du plus général au plus spécifique.
# Un objet qui herite d'un autre objet est considéré comme un sous-type de cet object.

#classe Parent
class Agents:
    def __init__(self, nom):
        self.nom = nom
    
    
#classe enfant
class Informaticien(Agents):
    def __init__(self , nom_inf):
        self.nom_inf= nom_inf
        print(f" nom : {self.nom_inf}")



travailleur = Informaticien("blanchard")