# 기본 입출력
# 문자열 인덱싱
# 문자열 슬라이싱
# 다양한 문자열 함수
# print("Hello World")
#
# name = "박찬호"
# age = 25
# "제 이름은 ___입니다."
# print("제 이름은" + name + "입니다.") # 띄어쓰기 X
# print("제 이름은" , name, "입니다.") # 띄어쓰기 O
# # "제 나이는 __ 입니다."
# print("제 나이는" , age, "입니다.")
# print("제 나이는 {} 이고 이름은 {} 입니다.".format(age, name))
# print("제 나이는 {a} 이고 이름은 {b} 입니다.".format(a=25, b="박찬호"))
# print(f"제 나이는 %d 이고 이름은 %s 입니다." % (age, name)) #f-string 방식
# print("제 나이는 %s 입니다." % age) # 문자열 로 들어 간다
# print("제 나이는 %d 입니다." % age) # 모든 숫자가 정수로 들어 간다
# print("제 주식은 %d%% 입니다." % 2)
# #
# hobby = "산책"
# money = 10000
# print("제 돈은 %d 이고 취미는 %s 입니다." % (money, hobby))
# print(f"제 돈은 {money} 이고 취미는 {hobby} 입니다.")
#
# print("%10.6f" % 3.141565186) # %"자릿수"."몇번째소수점"f
#입력
# input()
# email = input("이메일 : ")
# hobby = input("취미 : ")
# age = int (float(input("나이 : ")))
# print(type(age))
# print(f"제 이메일 은 {email}, 제 취미는 {hobby}, 나이는 {age}")
# from curses.ascii import isupper


# a = "Life is too short, You need Python"
# print(a[2:10:1])

date = "20250218sunny"
date2 = "20260505cloudy"

#연도, 월, 일, 날씨
# 연도는 2025, 월은 02 일은 18 날씨는 sunny

print(date[0:4])
print(date[4:6])
print(date[6:8])
print(date[8:])
print(f"연도는{date[0:4]}, 월은{date[4:6]}, 일은{date[6:8]}, 날씨는{date[8:]} ")