# age = int(input("ป้อนอายุของคุณ: "))

# if age>=1:
#     print("คำนำหน้าเป็น เด็กชาย/เด็กหญิง")
# elif age>=0:
#     print("ไม่สามารถระบุได้")
#     if age>=15:
#         print("คำนำหน้าเป็น นาย/นางสาว")


# num = int(input("ป้อนตัวเลขที่ต้องการเเสดงตารางสูตรคูณ: "))
# print("ตารางสูตรคูณของเลข {} ได้เเก่".format(num))
# for i in range(1,13):
#     print("{}x{}={}".format(num,i,num*i))

def calculate_length(text):
    return len(text)
input_number = input("Insert your text: ")
length = calculate_length(input_number)
print("The number of your text is total.",length)

