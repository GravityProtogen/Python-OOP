class Item:
    #__init__ é sempre chamado toda vez que um novo  objeto é instanciando, por exemplo: item1 = Item()
    def __init__(self,name: str,price: float,quantity = 0):
        # Validações
        assert price >= 0, f"O Preço {price} não é maior do que 0"
        assert quantity >= 0, f"A quantidade {quantity} não é maior do que 0"
        
        print(f"Instancia criada:", {name})
        self.name = name
        self.price = price
        self.quantity = quantity
    # Funções dentro de classes são chamados de MÉTODOS
    # Self pega o objeto em si, por exemplo no primeiro o self é a mesma coisa que item1, logo é item1.price
    # e item1.quantity sendo calculados
    def calcular_preco_total(self):
        total = self.price * self.quantity,
        return print(total)
    pass


item1 = Item("Phone", 100, 5)
item1.calcular_preco_total()

item2 = Item("Laptop", 200, 2)
item2.calcular_preco_total()

