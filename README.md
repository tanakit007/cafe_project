# ☕ Cafe Ordering System (OOP Python)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-pytest-brightgreen?logo=pytest&logoColor=white)

ระบบจัดการคำสั่งซื้ออาหารและเครื่องดื่ม พัฒนาตามหลักการ **Object-Oriented Programming (OOP)** ด้วยภาษา Python ร่วมกับ **Flask Web Framework** รองรับการแสดงผลทุกอุปกรณ์แบบ Responsive ด้วย Bootstrap 5

---

## ✨ ฟังก์ชันเด่น (Key Features)

* **Real-time Revenue Summary:** สรุปยอดขายรวมสะสมทันทีเมื่อการชำระเงินสำเร็จ
* **Menu Management:** แสดงรายการสินค้าแยกตามหมวดหมู่ พร้อมระบบเพิ่มเมนูใหม่เข้าสู่ร้าน
* **Multi-select Ordering:** รองรับการเลือกสั่งซื้อหลายรายการพร้อมกันในบิลเดียว
* **Automated Billing & History:** คำนวณราคาและภาษีอัตโนมัติ พร้อมบันทึกประวัติคำสั่งซื้อ (`Completed Orders`)
* **Automated Unit Testing:** ครอบคลุมชุดทดสอบด้วย `pytest` รับประกันความถูกต้องของ Logic

---

## 🏛️ สถาปัตยกรรมคลาส (Class Architecture)

ออกแบบตามหลัก **Separation of Concerns (SoC)** แบ่งความรับผิดชอบออกเป็น 3 คลาสหลัก:

```
[MenuItem] ──(1..*)──> [Order] ──(1..*)──> [CafeSystem]
 (Blueprint)             (Billing)           (Central Controller)
```

1. **`MenuItem` (`models/menu_item.py`)**
   * โมเดลข้อมูลสินค้า: รหัส (`item_id`), ชื่อ (`name`), ราคา (`price`), และหมวดหมู่ (`category`)
   * มีเมธอดแปลงข้อมูลเป็น Dictionary (`to_dict()`) สำหรับการเชื่อมต่อ API / Templates

2. **`Order` (`models/order.py`)**
   * จัดการบิลและการคำนวณเงิน รวบรวมรายการสินค้าในรูปแบบ `List[MenuItem]`
   * ควบคุม Business Logic การคิดราคารวม (`calculate_total()`) และสถานะการชำระเงิน

3. **`CafeSystem` (`models/cafe_system.py`)**
   * Controller ศูนย์กลางสำหรับบริหารคลังเมนู (เพิ่ม/ค้นหารายการ)
   * ดำเนินการสร้างออเดอร์, การ Checkout, และคำนวณรายได้สะสม (`total_revenue`)

---

## 👥 การแบ่งหน้าที่รับผิดชอบ (Team Collaboration)

| สมาชิก | หน้าที่รับผิดชอบ | โมดูลที่เกี่ยวข้อง |
| :--- | :--- | :--- |
| **คน A** | เมนูและสต็อกสินค้า *(Menu Domain)* | `MenuItem` และเมธอด `add_menu_item()`, `get_menu_list()` |
| **คน B** | ธุรกรรมและยอดขาย *(Order Domain)* | `Order` และเมธอด `create_order()`, `checkout()`, `get_total_revenue()` |
| **ร่วมกัน** | Web Integration & DevOps | Routing ใน `app.py`, ส่วนติดต่อผู้ใช้ `index.html`, Unit Testing, และ Deployment |

---

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

```text
cafe_project/
├── models/
│   ├── __init__.py          # Model package exports
│   ├── menu_item.py         # Blueprint สำหรับรายการสินค้า
│   ├── order.py             # Logic การคิดเงินและจัดการบิล
│   └── cafe_system.py       # คอนโทรลเลอร์หลักของระบบ
├── templates/
│   └── index.html           # UI Responsive (Bootstrap 5)
├── tests/
│   ├── __init__.py
│   └── test_cafe.py         # Unit tests (pytest)
├── app.py                   # Flask Application Controller & Routing
├── requirements.txt         # Project dependencies
├── Procfile                 # Process file สำหรับ PaaS deployment
├── Dockerfile               # Container build configuration
├── .gitignore
└── README.md
```

---

## 🚀 เริ่มต้นใช้งาน (Getting Started)

### ข้อกำหนดเบื้องต้น
* Python 3.9 ขึ้นไป
* Git

### ขั้นตอนการติดตั้ง

**1. Clone โปรเจกต์ และเตรียมสภาพแวดล้อมเสมือน (Virtual Environment)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**2. ติดตั้ง Dependencies**
```bash
pip install -r requirements.txt
```

**3. รันการทดสอบระบบ (Unit Test)**
```bash
pytest -v
```

**4. เริ่มต้นเซิร์ฟเวอร์**
```bash
python app.py
```
> เปิดเบราว์เซอร์แล้วไปที่ `http://127.0.0.1:5000/` เพื่อเริ่มใช้งาน