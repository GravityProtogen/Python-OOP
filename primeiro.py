import csv
import os
print(os.getcwd())
class Item:
    
    all = []
    #__init__ é sempre chamado toda vez que um novo  objeto é instanciando, por exemplo: item1 = Item()]
    # Funções dentro de classes são chamados de MÉTODOS
    # Self pega o objeto em si, por exemplo no primeiro o self é a mesma coisa que item1, logo é item1.price
    # e item1.quantity sendo calculados

    def __init__(self,name: str,price: float,quantity = 0):
        pay_rate = 0.8
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
    

    @classmethod
    def instantiate_from_csv(cls):
        
        # SEARCHING FOR FILE SINCE PYTHON DOESNT WANT TO
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'items.csv')
        print(f"Looking for items.csv in: {file_path}")
        
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
            

    @staticmethod
    def check_if_integer(num):
            # We will count out the floats that are point zero
            # For i.e: 5.0, 10.0
            if isinstance(num, float):
                # Count out the floats that are point zero
                return num.check_if_integer()
            elif isinstance(num, int):
                return True
            else:
                return False


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity} )\n"





class Phone(Item):
    def __init__(self,name: str,price: float,quantity = 0,brokenPhones = 0):
        # superFunção pra pegar atributos do Item
        super().__init__(
            name, price, quantity
        )
        
        assert brokenPhones >= 0, f"The amount of broken phones {brokenPhones} isnt equal or bigger than 0"
        

        self.brokenPhones = brokenPhones
    


phone1 = Phone("jscPhonev10", 500, 5,2)
phone1.calc_total_price()
phone2 = Phone("jscPhonev10", 700, 5)
print(phone2.brokenPhones)
