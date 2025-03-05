# print("Hello World")
#
# # 사용자로부터 두 개의 숫자를 입력받아 더한 값을 출력하는 프로그램을 작성하세요
# a = int(input("첫 번째 숫자를 입력하시오 :"))
# b = int(input("두 번째 숫자를 입력하시오 :"))
# print("두 수의 합:", a+b)
# 숫자를 입력받아 짝수면 "짝수", 홀수면 "홀수"를 출력하세요.
# num = int(input("숫자를 입력하시오: "))
#
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# name = "찬호"
# age = 26
# "제 이름은 ___입니다."
# print("제 이름은" + name + "입니다.") # 띄어쓰기 X
# print("제 이름은" , name, "입니다.") # 띄어쓰기 O
#
# # print("제 나이는" , age, "입니다.")
# # print("제 나이는 {} 이고 이름은 {} 입니다.".format(age, name))
# # print("제 나이는 {a} 이고 이름은 {b} 입니다.".format(a=25, b="박찬호"))
# print(f"제 나이는 %d 이고 이름은 %s 입니다." % (age, name)) #f-string 방식
# # print("제 나이는 %s 입니다." % age) # 문자열 로 들어 간다
# # print("제 나이는 %d 입니다." % age) # 모든 숫자가 정수로 들어 간다
# # print("제 주식은 %d%% 입니다." % 2)
#입력
# input()
# email = input("이메일 : ")
# hobby = input("취미 : ")
# age = int (float(input("나이 : ")))
# print(type(age))
# print(f"제 이메일 은 {email}, 제 취미는 {hobby}, 나이는 {age}")

# # 리스트에서 index() 사용
# my_list = [10, 20, 30, 40, 20]
# print(my_list.index(20)) # 결과: 1 (20이 처음 나타나는 위치)
# print(my_list.index(20, 2)) # 결과: 4 (인덱스 2부터 검색 시작)
#
# # 문자열에서 index() 사용
# my_string = "Hello, Python!"
# print(my_string.index("Python")) # 결과: 7
#
# # 튜플에서 index() 사용
# my_tuple = (1, 2, 3, 4, 3)
# print(my_tuple.index(3)) # 결과: 2
