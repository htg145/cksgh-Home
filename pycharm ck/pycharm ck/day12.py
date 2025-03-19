# 모듈
import math

# math - 수학 무듈

# ceil - 올림
# print(math.ceil(3.14))
#
# # copysign - 두 번째 인자의 부호만 취해 첫 번째 인자에 적용
# print(math.copysign(3.14, -2))
#
# # fabs - 절댓값 을 반환 하는 메소드
# print(math.fabs(-3.14))
#
# # factorial - 펙토리얼 구하는 메소드
# print(math.factorial(7))
#
# # floor - 내림
# print(math.floor(3.14))
#
# # gcd - 두 수의 최대공약수
# print(math.gcd(6, 8))
#
# # modf - 정수 부분과 소수 부분을 분리 해서 리턴
# print(math.modf(3.14))
#
# # trunc - 내림
# print(math.floor(-3.14)) # 무조건 아래로 내림
# print(math.trunc(-3.14)) # 0으로 향해서 내림
#
# # log(a, b) - b를 밑으로 하는 log a에 대한 로그 값
# print(math.log(10, 10))
#
# # 원주율
# print(math.pi)

# import random
#
# # 난수
# print(random.random())
#
# print(random.randint(1, 10))
# print(random.randrange(1, 10, 2))
#
# # shuffle
# abc = ["a", "b", "c", "d", "e"]
# random.shuffle(abc)
# print(abc)
#
# # choice
# abc = ["a", "b", "c", "d", "e"]
# print(random.choice(abc))
#
# menu = "삼겹살", "된장 찌개", "맥주", "소주"
# print(random.choice(menu))


# from datetime import datetime, timedelta
#
# 현재 날짜
# now = datetime.now()
# print(now)
#
# # 7일뒤 날짜
# one_week_later = now + timedelta(days=7)
# print(one_week_later)
#
# formatted_date = now.strftime("%Y-%M-%D-%H-%M:%S") # 순서(형식)을 바꿀수 있다
# print(formatted_date)

# import os
#
# print(os.getcwd()) # 현재 디렉 토리
# print(os.listdir()) # 현재 폴더의 파일 목록
#
# if not os.path.exists("new_folder"):
#     os.mkdir("new_folder")

# import re
#
# pattern = r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"
# email = "htg145@naver.com"
#
# if re.match(pattern, email):
#     print("올바른 이메일")
# else:
#     print("틀린 이메일")

# 주사위 놀이 만들기
import random

def dice_list():
    dice_number = random.randint(1, 6)
    return dice_number
dice_number = dice_list()
print(f"숫자 : {dice_number} ")








