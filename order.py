# models/order.py
from models.menu_item import MenuItem

class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = []          # เก็บ list ของ instance MenuItem
        self.is_paid = False

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)

    def get_summary(self):
        return {
            "order_id": self.order_id,
            "items": [item.name for item in self.items],
            "total": self.calculate_total(),
            "is_paid": self.is_paid
        }