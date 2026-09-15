from flask import Flask, render_template, request, redirect, url_for
from models.cafe_system import CafeSystem

app = Flask(__name__)

# สร้าง instance ของระบบ
system = CafeSystem()

# ข้อมูลตั้งต้น
system.add_menu_item("M1", "Espresso", 55.0, "Coffee")
system.add_menu_item("M2", "Iced Latte", 65.0, "Coffee")
system.add_menu_item("M3", "Green Tea", 60.0, "Tea")
system.add_menu_item("M4", "Croissant", 45.0, "Bakery")

@app.route("/")
def index():
    menu_items = system.get_menu_list()
    orders = [o.get_summary() for o in system.completed_orders]
    total_sales = system.get_total_revenue()
    return render_template("index.html", menu=menu_items, orders=orders, total_sales=total_sales)

@app.route("/menu/add", methods=["POST"])
def add_menu():
    item_id = request.form.get("item_id")
    name = request.form.get("name")
    price = request.form.get("price")
    category = request.form.get("category")
    
    if item_id and name and price:
        system.add_menu_item(item_id, name, float(price), category)
    return redirect(url_for("index"))

@app.route("/order/create", methods=["POST"])
def place_order():
    selected_items = request.form.getlist("selected_items")
    if selected_items:
        order = system.create_order(selected_items)
        system.checkout(order)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)