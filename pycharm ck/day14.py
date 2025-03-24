# 클래스 - 설계도, 설명서 (class) 구성: 속성(모델명, 가격, 종류)-생성자, 기능(앞으로, 뒤로) - 메소드
# 객체 - 오브 젝트(object) 설계도 로 만들어 졌다. instance(인스 턴스) 라고 말할수 있다.
# 클래스 정의와 생성자, 메소드



# class 클래스 이름: 케이스 - 스네 이크 케이스
#     def __init__(self, 매개 변수): self 꼭 있어야 함 # 생성자, __init__(속성 정의)
#         self.(변수)

# 소멸자 - 당장 소멸 시켜야 할 때, 소멸 되기 전 무언가 처리 해야할 때
# class 클래스 이름:
#     def __del__(self):
#       소멸자 코드

# 소멸자
# class Example:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} 객체가 생성됨.")
#
#     def __del__(self):
#         print(f"{self.name} 객체가 소멸됨.")

# 객체 생성
# object = Example("테스트") # 객체 생성

# 객체 삭제 (명시적 으로 삭제 하지 않아도 자동 으로 삭제 합니다.)
# del odj # 객체 삭제 - 소명자 삭제

# class Car:
#     pass # 일단 패스 그냥 지나감 오류 안뜨고
#
# while True:
#     pass

# class Car: # 클래스 정의
#     def __init__(self, model, price): # 생성자
#         self.model = model
#         self.price = price
#         print(f"모델 이름:{self.model}, 가격:{self.price} 객체 생성 !!")
#
#     def __del__(self): # 소멸자
#         print(f"{self.model}의 객체가 소멸 됨!!")
#
#     def drive(self, speed, distance):
#         print(f"{self.model}가 {speed}의 속도가 {distance}km 만큼 전진")
#
# car1 = Car("avente", 2400) # 객체 생성 (car 클래스 의 인스 턴스)
# car1.is_n = False, "아님" # 맴버 변수
# print(car1.is_n)
#
# print(isinstance(car1, Car)) # Car 로 만들 어진 인스 턴스 맞다
# car2 = Car("santafe", 4000 ) # car2 객체 생성 (Car 클래스 인스 턴스)
# car2.drive(50, 10)

# class Player:
#     def __init__(self, nickname, hp, gold = 0, level = 0):
#         self.nickname = nickname
#         self.hp = hp
#         self.gold = gold
#         self.level = level
#         print(nickname, hp, gold, level)
#
#     def __del__(self):
#         print("저장 중")
#         print("저장 되었 습니다.")
#
#     def del_player(self):
#         print("케삭 되었 습니다.")
#
#     def change_nickname(self, new_nickname):
#         self.nickname = new_nickname
#
# player1 = Player("yoon", 5000, 1000, 100)
# player1.change_nickname("doog")
# print(player1.nickname)
#
# def func(age, name = "홍길동"):
#     print(age, name)
#
# func(27)

# class Person:
#     def __init__(self, age, email, name="홍길동"):
#         self.name = name
#         self.age = age
#         self.email = email
#     def introduce(self):
#         print(f"이름은 {self.name}이고 나이는 {self.age} 이메일은 {self.email}")
# person1 = Person(27, "htg145@naver.com")
#
# print(person1)


# 영화

# class Movie:
#     def __init__(self, 제목, 배우, 개봉일, 평점):
#         self.제목 = 제목
#         self.배우 = 배우
#         self.개봉일 = 개봉일
#         self.평점 = 평점
#
#     def 영화정보(self):
#         print(f"제목: {self.제목}, 배우:{self.배우}, 개봉일:{self.개봉일}, 평점:{self.평점}")
#
# movie1 = Movie("진격의 거인 완결판", "거인", "2025 - 03 - 13", "9.5" )
# movie2 = Movie("에브리씽 에브리웨어 올 앳 원스", "양자경", "2022","8.81")
#
# movie1.영화정보()
# movie2.영화정보()











