# 제어문
# 프로 그램의 실행 흐름을 제어 하는 구문
# 조건에 따라 코드 블록을 실행
# 반복적 으로 코드 블록을 실행

# 조건문
# 어떤 조건에 따라 실행이 분기 되도록 하는 기준이 되는 식
"1"
# if 조건문:
#     수행할_문장1
#     수행할_문장2
#     수행할_문장3
"2"
# if 조건문:
#     수행할_문장1
#     수행할_문장2
# else:
#     수행할_문장3
"3"
# if 조건문:
#     수행할_문장1
#     수행할_문장2
# elif:
#     수행할_문장3
# else:
#     수행할_문장4

# num =int(input("숫자를 입력해 주세요."))
# if num > 0:
#     print("양수 입니다.")
# else:
#     print("음수 입니다.")

# score = int(input("점수를 입력해 주세요."))
#
# if score >= 90:
#     print("A 입니다.")
# elif score >= 80:
#     print("B 입니다.")
# elif score >= 70:
#     print("C 입니다.")
# else:
#     print("D 입니다.")

# input_str = input("점수를 입력해 주세요.")
# if not input_str.isdigit():
#     print("숫자가 아닙 니다.")
# else:
#     if int(input_str) >= 90:
#         print("A 입니다.")
#     elif int(input_str) >= 80:
#         print("B 입니다.")
#     elif int(input_str) >= 70:
#         print("C 입니다.")
#     else:
#         print("D 입니다.")

# 숫자를 입력 받고 짝수 인지 홀수 인지
# num = int(input("숫자를 입력해 주세요."))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 나이랑 학생 인지 아닌지 두가지 질문
# 성인 이면서 학생 이면 성인 학생 입니다.
# 성인 학생이 아닙 니다
# age =int(input("나이를 입력 하세요."))
# student = input("학생 입니까?(y/n)")
# if age >= 18 and student == "y":
#     print("성인 학생 입니다.")
# else:
#     print("성인 학생이 아닙 니다.")


# 반복문 while
# 조건이 참(True)인 동안 계속 반복
# 특정 조건을 만족 할때 까지 계속 실행 해야 하는 경우
# while 조건 : break(멈춤다), continue(처음 부터 돌아 가서 또 돈다)

# num = 0
# while num < 10:
#     num += 1
#     if num % 3 == 0:
#         continue
#     print(num)

# num = 0
# while num < 5:
#     print(num)
#     num += 1

# 구구단
# dan = 1
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print(f"{dan}x{n}={dan*n}")
#         n += 1
#     dan += 1

# 5부터 5의 배수를 50이하 까지 조건
# 근대 30일때 멈출 게요
# num = 5
# while num <= 50:
#     print(num)
#     if num == 30:
#         break
#     num += 5

# 반복문 for
# 특정 조건을 만족할 때까지 계속 실행 해야 하는 경우
# 반복 해야 할 횟수가 정해져 있거나, 반복 해야 할 대상이 명확 하게 정의 되어 있는 경우
# for 변수 in 리스트 (또는 튜플, 문자열):
# 수행할_문장1
# 수행할_문장2

# for i in range(2, 10, 2):
#     print(i)

# for 문
fruits = ["사과", "바나나", "체리", "딸기"] # 리스트 fruits 이거 안에 fruit 로 하나씩 뽑아줘
for fruit in fruits:
    print(fruit)
# 딕셔 너리
# score = {
#     "동윤": 80,
#     "종원": 70,
#     "지니": 100
# }
# for key in score:
#     print(f"{key}의 점수는 {score[key]}")
# 튜플
# a_tuple = ("안녕", "하세요", "반갑 습니다")
# for a in a_tuple:
#     print(a)
# 세트
# a_set = {3, 1, 1, 2, 4, 6, 2}
# print(sorted(a_set))
# for a in a_set:
#     print(a)

# word = "python"
# for i in word:
#     print(i)

# for i in range(1, 10):
#     if  i == 5:
#         continue
#     print(i)

# for i in range(1, 101, 2):
#     print(i)

# 리스트 합 구하기
# 전역 변수
# total = 0
# num_list = [10, 20 ,40, 60, 80]
# for num in num_list:
#     print("num", num)
#     total += num
#     print("total", total)

# for 문 으로 구구단
# for dan in range(1 ,10):
#     for n in range(1, 10):
#         print(f"{dan}x{n}={dan*n}")



# 지역 변수는 전역 변수에 사용 할수 없다
# 전역 변수는 지역 변수에 사용 할수 있다





