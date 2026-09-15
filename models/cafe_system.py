from models.menu_item import MenuItem
from models.order import Order

class CafeSystem:
    def __init__(self):
        self.menu = {}              # Dict[str, MenuItem]
        self.completed_orders = []  # List[Order]
        self._next_order_id = 1

    # --------------------------------------------------
    # [คน A]: ส่วนจัดการเมนูและสต็อกสินค้า
    # --------------------------------------------------
    def add_menu_item(self, item_id: str, name: str, price: float, category: str) -> MenuItem:
        item = MenuItem(item_id, name, price, category)
        self.menu[item_id] = item
        return item

    def get_menu_list(self):
        return list(self.menu.values())

    def find_item(self, item_id: str):
        return self.menu.get(item_id)

    # --------------------------------------------------
    # [คน B]: ส่วนจัดการคำสั่งซื้อและยอดขาย
    # --------------------------------------------------
    def create_order(self, selected_item_ids: list) -> Order:
        order = Order(self._next_order_id)
        self._next_order_id += 1
        
        for item_id in selected_item_ids:
            item = self.find_item(item_id)
            if item:
                order.add_item(item)
                
        return order

    def checkout(self, order: Order) -> bool:
        if order.items:
            order.is_paid = True
            self.completed_orders.append(order)
            return True
        return False

    def get_total_revenue(self) -> float:
        return sum(order.calculate_total() for order in self.completed_orders)