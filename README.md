# Cafe Ordering System (OOP Python)

ระบบจัดการสั่งอาหารและเครื่องดื่ม พัฒนาด้วยหลักการ Object-Oriented Programming (OOP) ภาษา Python และ Flask Framework

## 📌 สถาปัตยกรรมคลาส (3 Classes)
1. `MenuItem`: จัดการโครงสร้างข้อมูลของแต่ละเมนู
2. `Order`: รวบรวมรายการสินค้าที่สั่ง และคำนวณราคารวมของบิล
3. `CafeSystem`: ศูนย์กลางควบคุมระบบ จัดการรายการเมนู คลังออเดอร์ และสรุปยอดขาย

## 🚀 วิธีการติดตั้งและรัน Local

```bash
# 1. ติดตั้ง Dependencies
pip install -r requirements.txt

# 2. รัน Unit Test
pytest

# 3. เริ่มต้นรันเซิร์ฟเวอร์
python app.py