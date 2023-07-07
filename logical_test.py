"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def number_to_thai_text():
    thai_numbers = {0: 'ศูนย์', 1: 'หนึ่ง', 2: 'สอง', 3: 'สาม', 4: 'สี่', 5: 'ห้า',
                    6: 'หก', 7: 'เจ็ด', 8: 'แปด', 9: 'เก้า'}
    # units = ['สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

    while True:
        try:

            number = int(input('กรอกตัวเลข (0-9999999): '))
            if 0 <= number <= 9999999:
                break
            else:
                print('กรุณากรอกตัวเลขระหว่าง 0-9999999')
        except ValueError:
            print('กรุณากรอกตัวเลขที่ถูกต้อง')

    if number == 0 or number == 1:
        return print(thai_numbers[number])
    else:
        thai_text = ''
        millions = number // 1000000
        hundred_thousands = (number % 1000000) // 100000
        ten_thousands = (number % 100000) // 10000
        thousands = (number % 10000) // 1000
        units = number % 1000

        if millions > 0:
            thai_text += thai_numbers[millions] + 'ล้าน'

        if hundred_thousands > 0:
            thai_text += thai_numbers[hundred_thousands] + 'แสน'

        if ten_thousands > 0:
            thai_text += thai_numbers[ten_thousands] + 'หมื่น'
        if thousands > 0:
            thai_text += thai_numbers[thousands] + 'พัน'

        if units > 0:
            if units >= 100:
                thai_text += thai_numbers[units // 100] + 'ร้อย'
                units %= 100
            if units >= 10:
                if units // 10 == 1:
                    thai_text += 'สิบ'
                elif units // 10 == 2:
                    thai_text += 'ยี่สิบ'
                else:
                    thai_text += thai_numbers[units // 10] + 'สิบ'
                units %= 10
            if units > 0:
                if units == 1:
                    thai_text += 'เอ็ด'
                else:
                    thai_text += thai_numbers[units]

        print(thai_text)



number_to_thai_text()

