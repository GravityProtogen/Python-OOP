class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material 
        
    def trocaCor(self,corNova):
        self.cor = corNova
    def mostraCor(self):
        return print(self.cor)
    
item1 = Bola("azul",85,"borracha")
item1.mostraCor()
item1.trocaCor("roxo")
item1.mostraCor() 