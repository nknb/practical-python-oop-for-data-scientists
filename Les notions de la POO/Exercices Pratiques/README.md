# 🧮 Classe `Numbers` – Exercice Python

## Objectif

Cet exercice a pour but d’implémenter une classe Python nommée `Numbers` qui effectue des opérations numériques simples en utilisant les principes de la programmation orientée objet.

## Spécifications

Créez une classe nommée `Numbers` avec les caractéristiques suivantes :

### Attribut de classe
- `MULTIPLIER = 10`  
  Un attribut de classe utilisé pour les opérations de multiplication.

### Constructeur
- `__init__(self, x, y)`  
  Initialise une instance avec deux attributs numériques `x` et `y`. Ces deux valeurs doivent obligatoirement être des nombres (`int` ou `float`).

### Méthodes d’instance
- `add(self)`  
  Retourne la **somme** des attributs `x` et `y`.

- `multiply(self, a)`  
  Prend en paramètre un nombre `a` et retourne le **produit** de `a` par `MULTIPLIER`.

### Méthode statique
- `substract(b, c)`  
  Méthode statique qui prend deux paramètres numériques `b` et `c`, et retourne le résultat de `b - c`.

### Propriété : `values`
- Un **setter** qui permet de mettre à jour `x` et `y` à l’aide d’un tuple ou d’une liste contenant deux valeurs numériques.
