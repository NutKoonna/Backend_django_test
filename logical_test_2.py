"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def arabic_number_to_roman_number(num):
    arabic_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_numeral = ''
    i = 0
    while num > 0:
        if num >= arabic_values[i]:
            roman_numeral += roman_symbols[i]
            num -= arabic_values[i]
        else:
            i += 1

    return roman_numeral


# Example usage
while True:
    try:
        number = int(input('Enter an Arabic number (1-1000): '))
        if 1 <= number <= 1000:
            break
        else:
            print('Please Enter an Arabic number between 1-1000')
    except ValueError:
        print('Please Check Your Input')
roman_number = arabic_number_to_roman_number(number)
print(f"Convert Arabic number to Roman Number:{number} => {roman_number} ")
