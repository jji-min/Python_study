# def hello():
#     print("Hello!")
#     print("Welcome~")
# hello()

# def hello(name):
#     print("Hello!")
#     print(name)
#     print("Welcome~")
# hello("Lucy")

# def print_sum(a, b, c):
#     print(a + b + c)
# print_sum(1, 2, 3)

# def get_square(x):
#     return x * x
# print(get_square(3))

# print(round(3.1415926535))
# print(round(3.1415926535, 2))
# print(round(3.1415926535, 4))

# print("I'm excited to learn Python!")
# print("I\'m \"excited\" to learn Python!")

# 형 변환
# print(int("2") + int("5"))
# print(str(2) + str(5))
# age = 11
# print("나이 : " + str(age) + "살")

# format
# year = 2025
# month = 1
# day = 1
# print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

# date_string = "오늘은 {}년 {}월 {}일입니다."
# print(date_string.format(year, month, day))

# 문자열 포맷팅
# # %
# name = "홍길동"
# age = 11
# print("제 이름은 %s이고 %d살입니다." % (name, age))

# # f-string
# print(f"제 이름은 {name}이고 {age}살입니다.")

# --------------------------------------------------------

# if문
# a = 1
# b = 3
# if a > b:
#     print("a가 더 큼")
# else:
#     print("b가 더 큼")

# while문
# previous = 0
# current = 1
# i = 1
# while i <= 10:
#     print(current)
#     temp = previous
#     previous = current
#     current = current + temp
#     i += 1

# print("\n")

# previous = 0
# current = 1
# i = 1
# while i <= 10:
#     print(current)
#     previous, current = current, current + previous
#     i += 1

# for문
# a, b = 1, 1
# for i in range(10):
#     print(a)
#     a, b = b, a + b

# break문
# i = 1
# while i <= 20:
#     print(i)
#     if i % 7 == 0:
#         break
#     i += 1

# continue문
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 1:
#         continue
#     print(i)

# 리스트
# numbers = [2, 4, 7, 9, 15]
# print(numbers[0:4])

# numbers = []
# numbers.append(5)
# numbers.append(10)
# print(len(numbers))

# numbers = [1, 3, 6, 8, 23, 49]
# del numbers[3]
# print(numbers)
# numbers.insert(4, 33)
# print(numbers)

# print(1 in numbers)
# print(8 in numbers)

# dictionary
cafe_menu = {
    '커피' : '아메리카노',
    '에이드' : '레몬에이드'
}
print(cafe_menu.values())

for value in cafe_menu.values():
    print(value)

cafe_menu['디저트'] = '와플'
print(cafe_menu)

for key in cafe_menu:
    print(key , '->', cafe_menu[key])