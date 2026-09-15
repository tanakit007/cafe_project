class MenuItem:
    def __init__(self, item_id: str, name: str, price: float, category: str):
        self.item_id = item_id
        self.name = name
        self.price = float(price)
        self.category = category

    def to_dict(self):
        return {
            "id": self.item_id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }