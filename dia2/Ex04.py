class Animal:
    def animais(self):
        return "Som de animal aleatorio"
class Cachorro(Animal):
    def animais(self):
        return "Au Au"
class Gato(Animal):
    def animais(self):
        return "miau"

garfield = Gato()
print(garfield.animais())