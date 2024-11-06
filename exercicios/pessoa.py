class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self,valor):
        for _ in range(valor):
            if self.idade < 21:
                self.crescer(0.5)
            self.idade += 1 
    def engordar(self,valor):
        self.peso = self.peso + valor
    def emagrescer(self,valor):
        self.peso = self.peso - valor
    def crescer(self,valor):
        self.altura = self.altura + valor
    