class Item:
    
    def __init__(self,name,weight, price,) -> None:
        self.itemName = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return  f"<Item name:{self.itemName} weight:{self.weight} price:{self.price}>"
