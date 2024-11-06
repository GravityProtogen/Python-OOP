from item import Item

class Phone(Item):
    def __init__(self,name: str,price: float,quantity = 0,brokenPhones = 0):
        # superFunção pra pegar atributos do Item
        super().__init__(
            name, price, quantity
        )
        
        assert brokenPhones >= 0, f"The amount of broken phones {brokenPhones} isnt equal or bigger than 0"
        

        self.brokenPhones = brokenPhones

