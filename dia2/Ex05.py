class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    def sons_animais(self):
        return "Som de animal aleatorio"


class Cachorro(Animal):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
    def apresentacao(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
    def sons_animais(self):
        return "Au Au"


class Gato(Animal):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
    def apresentacao(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
    def sons_animais(self):
        return "miau"


garfield = Gato("Garfield", 12)
garfield.apresentacao()
