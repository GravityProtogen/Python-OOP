class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def mudarLado(self,ladoNovo):
        self.lado = ladoNovo
    def mostrarLado(self):
        print(self.lado)
    def calcularArea(self):
        area = self.lado * self.lado
        print(area)
        
        
item1 = Quadrado(50)
item1.mostrarLado()
item1.mudarLado(100)
item1.mostrarLado()
item1.calcularArea()
