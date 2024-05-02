from func import show_type
from func import show_menu_coffee
from func import show_menu_Tea
print("--------** ยินดีต้อนรับ** --------")
print("-----เครื่องดื่มอัตโนมัติ 24 ชั่วโมง-----")

type_menu = show_type()
# เลือกประเภทสินค้าและเลือกสินค้าเมนู 1 หรือ 2(menu_coffee/menu_Tea)
if type_menu == 1 or type_menu == 2:
    if type_menu == 1:
        menu_coffee = show_menu_coffee()
        if menu_coffee == 1:
            print("คุณได้เลือก: 'Cappuccino' ยอดรวม: 35 บาท.")
        elif menu_coffee == 2:
            print("คุณได้เลือก: 'Latte' ยอดรวม: 45 บาท.")
            
    if type_menu == 2:
        menu_Tea = show_menu_Tea()
        if menu_Tea == 1:
            print("คุณได้เลือก: 'Iced milk tea' ยอดรวม 55 บาท.")
        elif menu_Tea == 2:
            print("คุณได้เลือก: 'Greentea' ยอดรวม 65 บาท.")       

# จ่ายเเละทอนเงิน
payment = int(input("กรุณาใส่จำนวนเงิน: "))
if menu_coffee == 1:
    while True:
        if payment >=35:
            sum = (payment-35)
            change = sum
            print("เงินทอน: " + str(change))
            break
        else:
            print("เงินไม่พอ กรุณาใส่จำนวนเงินใหม่")
            payment = int(input("กรุณาใส่จำนวนเงิน: "))
else:
    if menu_coffee == 2:
        while True:
            if payment >=45:
                sum = (payment -45)
                change = sum
                print("เงินทอน: " + str(change))
                break
            else:
                print("เงินไม่พอ กรุณาใส่จำนวนเงินใหม่")
                payment = int(input("กรุณาใส่จำนวนเงิน: "))
if menu_Tea == 1:
    while True:
        if payment >=55:
            sum = (payment-55)
            change = sum
            print("เงินทอน: " + str(change))
            break
        else:
            print("เงินไม่พอ กรุณาใส่จำนวนเงินใหม่")
            payment = int(input("กรุณาใส่จำนวนเงิน: "))
else:
    if menu_Tea == 2:
        while True:
            if payment >=65:
                sum = (payment-65)
                change = sum
                print("เงินทอน: " + str(change))
                break
            else:
                print("เงินไม่พอ กรุณาใส่จำนวนเงินใหม่")
                payment = int(input("กรุณาใส่จำนวนเงิน: "))