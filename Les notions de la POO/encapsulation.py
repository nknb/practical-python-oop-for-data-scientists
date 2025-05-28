# L'encapsulation est un principe important de la POO ,car l'idée est que les données à l'interieur d'un objet ne doivent être accessible que via les methodes de l'objet
# Exemple de création de classe

class Student:
    def __init__(self , name , surname):
        self.name = name
        # j'ai defini surname comme propriété privée
        self._surname = surname