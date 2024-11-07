import csv
import os
print(os.getcwd())



class Item:
    all = []
    pay_rate = 0.8
    #__init__ é sempre chamado toda vez que um novo  objeto é instanciando, por exemplo: item1 = Item()]
    # Funções dentro de classes são chamados de MÉTODOS
    # Self pega o objeto em si, por exemplo no primeiro o self é a mesma coisa que item1, logo é item1.price
    # e item1.quantity sendo calculados

    def __init__(self,name: str,price: float,quantity = 0):
        
        # Validações
        assert price >= 0, f"The price {price} its not bigger than 0"
        assert quantity >= 0, f"A quantidade {quantity} não é maior do que 0"
        
        print(f"Instance created:", {name})
        self.__name = name
        self.__price = price
        self.quantity = quantity
    
        # Ações para executar
        Item.all.append(self)
        
    @property
    def name(self):
        # Makes it Read-Only
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,incrementValue):
        self.__price = self.__price + self.__price * incrementValue
        
    def calc_total_price(self):
        total = self.__price * self.quantity,
        
    def __connect(self,smptServer):
        pass
    
    def __prepareBody(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards
        """
    
    def __send(self):
        print("Enviado")
        pass
    
    def sendEmail(self):
        self.__connect('')
        self.__prepareBody()
        self.__send()
        pass
    

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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    