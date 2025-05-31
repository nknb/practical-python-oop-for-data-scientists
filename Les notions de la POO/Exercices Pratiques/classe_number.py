class Numbers:
    MULTIPLIER = 10
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multiply(self, a):
        return a * Numbers.MULTIPLIER
    @staticmethod
    def substract(b, c):
      return b - c
    @property
    def values(self):
        return self.x , self.y
    @values.setter
    def values(self, new_values):
        self.x ,self.y = new_values
        

num = Numbers(1,2)
#exemple de addition
addition =num.add()
print(addition)
#exemple de mutiplication
multiplication = num.multiply(2)
print(multiplication)
#exemple de soustraction
soustraction = num.substract(7,2)
print(soustraction)
#exemple de valeur
valeur = num.values
print(valeur)
# modification de valeur avec setter

num.values = (3,4)
valeur_modifier = num.values
print(valeur_modifier)