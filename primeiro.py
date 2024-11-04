class Item:
    pay_rate = 0.8
    all = []
    #__init__ é sempre chamado toda vez que um novo  objeto é instanciando, por exemplo: item1 = Item()]
    # Funções dentro de classes são chamados de MÉTODOS
    # Self pega o objeto em si, por exemplo no primeiro o self é a mesma coisa que item1, logo é item1.price
    # e item1.quantity sendo calculados

    def __init__(self,name: str,price: float,quantity = 0):
        # Validações
        assert price >= 0, f"The price {price} its not bigger than 0"
        assert quantity >= 0, f"A quantidade {quantity} não é maior do que 0"
        
        print(f"Instance created:", {name})
        self.name = name
        self.price = price
        self.quantity = quantity
    
        # Ações para executar
        Item.all.append(self)
    def calc_total_price(self):
        total = self.price * self.quantity,
        return print(total)
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return print(self.price)
    pass

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity} )\n"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
