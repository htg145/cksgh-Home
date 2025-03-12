# 사용자 정의 함수
# 기본 적인 사용자 정의 함수
# def 함수이름():
#     수행할 코드
# def func1():
#     print("Hello World")
#
# func1()
# func1()
# func1()


# def plus():
#     a = 2
#     b = 3
#     print(a + b)
# plus()



# 매개 변수와 return
# def 함수이름(매개 변수1, 매개 변수2, ...)
#     수행할 코드
#     ...
#     [return]
# 매개 변수가 있는 사용자 정의 함수

# def hello(name="찬호"):
#     print(f"안녕 하세요 저는 {name} 입니다.")
#
# hello()
# hello(123)

# def plus(x, y):
#     print(x + y)
# plus(5, 6)

# def introduce(name, age):
#     print(f"제 이름은 {name}이고 나이는 {age}입니다.")
#
# introduce(age=26, name="찬호")

# 리턴 값이 있는 사용자 정의 함수

# def plus(x, y):
#     return  x + y
#
# result = plus(1, 2)
# print(result)
# print(plus(1, 2))

# def multiple_seven(num):
#     return num * 7
# print(multiple_seven(3))
# print(multiple_seven(100))

# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
# print(check_divide_seven(14))
# print(check_divide_seven(15))


# 7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040 # !가 factorial 팩토 리얼
# factorial 7까지 쭉 곱 하는거

# def factorial(num):
#     sum = 1
#
#     for n in range(num):
#         print(f"n = {n}")
#         sum = sum * (n + 1)
#         print(f"sum = {sum}")
#     return sum
#
# print(factorial(7))



# def cal_average(scores):
#     sum = 0
#
#     for score in scores:
#         sum += score
#
#     return sum / len(scores)
#
# score_list1 = [55, 70, 100]
# score_list2 = [100, 99, 88]
# score_list3 = [80, 70, 60]
#
# print(cal_average(score_list1))
# print(cal_average(score_list2))
# print(cal_average(score_list3))

# 콜백 함수
# 함수를 매개 변수로 전달 하여 필요 할때 호출 하도록 하는 개념
# 어떤 함수가 실행 되는 동안 미리 정의된 다른 함수를 호출 하여 실행 되는 역할

# def calculator(x, y, operation):
#     return operation(x , y)
#
# def plus(x, y):
#     return x + y
#
# def minus(x, y):
#     return x - y
#
# def multiple(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# print(calculator(4 ,8, plus))
# print(calculator(8 ,4, minus))
# print(calculator(4 ,8, multiple))
# print(calculator(4 ,8, divide))

# import time
#
# def timer(pause_second, callback):
#     print(f"{pause_second}초 타이머 가 시작 되었 습니다.")
#     print(f"{pause_second}초 뒤에 함수가 실행 됩니다.")
#
#     time.sleep(pause_second)
#
#     callback()
#     print("타이머가 종료 되었습니다.")
#
# def hello():
#     print("안녕")
#
# timer(5, hello)

# lambda 함수 (익명 함수, 미시 함수)
# 특정 범위 내에서 만 사용 되거나 호출 되는 횟수가 한번인 경우에 매우 유용
# lambda  매 개변수1, 매개 변수2, ...: 함수 내부 코드

# def plus(x, y):
#     return x + y
#
# print(plus(4, 5))
#
# add_lambda = lambda x, y: x + y # 꼬리 + 털 = 고양이
# print(add_lambda(4, 5))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# double = list(map(lambda x: x * 2, numbers))
# print(double)

# parity = lambda x: "짝수" if x % 2 == 0 else "홀수"
#
# print(parity(5))

# 1. 두 수를 입력 받고 두수의 합을 출력 하는 함수

# a = int(input("첫번째 숫자 : "))
# b = int(input("두번째 숫자 : "))
#
# def num (a, b):
#     print(a + b)
#
# num(a, b)

#2. 숫자 하나를 입력 받고 해당 숫자가 짝수 이면
# 짝수를 출력 받고 홀수 이면 홀수를 출력 하는 함수

# a = int(input("숫자 : "))
#
# def num1(x):
#     if x % 2 == 0 :
#         print("짝수")
#     else:
#         print("홀수")
# num1(a)


# # 평균 계산 함수
# def num1 (numbers):
#     """숫자 리스트의 평균을 계산하는 함수"""
#     return sum(numbers) / len(numbers)
#
# scores = [80, 90, 95, 85]
# print(num1(scores))  # 출력: 87.5


# # 람다 함수 기본 예시
# add_lambda = lambda x, y: x + y
# print(add_lambda(3, 7))  # 출력: 10
#
# # map() 함수와 함께 사용
# numbers = [1, 2, 3, 4, 5]
# num_numbers = list(map(lambda x: x * 2, numbers))
# print(num_numbers)  # 출력: [2, 4, 6, 8, 10]
#
# # filter() 함수와 함께 사용
# abc = list(filter(lambda x: x % 2 == 0, numbers))
# print(abc)  # 출력: [2, 4]



# lambda 함수 (익명 함수, 미시 함수)
# 특정 범위 내에서 만 사용 되거나 호출 되는 횟수가 한번인 경우에 매우 유용
# lambda  매 개변수1, 매개 변수2, ...: 함수 내부 코드

# def plus(x, y):
#     return x + y
#
# print(plus(4, 5))
#
# add_lambda = lambda x, y: x + y # 꼬리 + 털 = 고양이
# print(add_lambda(4, 5))

# def plus(x, y):
#     if x == "꼬리" and y == "털":
#         return "고양이"
#     else:
#         return x + y
# print(plus("꼬리", "털"))