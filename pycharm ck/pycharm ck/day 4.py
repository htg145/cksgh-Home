# 딕셔너리 (Dictionary)
# 세트 (Set)
# 키-값 쌍으로 데이터를 저장하는 자료형
# 키는 고유해야 하며, 키를 사용해서 빠르게 접근가능
# 중괄호{}를 둘러싸여 있음. 각 키와 값은 콜론 : 으로 구분, 쌍은 쉼표, 로 구분
from operator import index

# 딕셔너리


person = {"철수"
          "나이": 25,
          "취미":["독서", "영화 감상"]
          }
profile = {
    "name" : "박찬호",
    "age" : 26,
    "hobby" : ["여행하기", "영화보기"],
}
# print(profile)
# print(person)
#
# print(profile["name"])
# print(profile["hobby"][1])
# profile["age"] = 28 # 키가 존재 하는 것은 수정
# print(profile)
#
# profile["job"] = "강사" # 키가 존재 하지 않는 것은 추가 된다
# print(profile)
#
# del profile["job"] # 삭제
# print(profile)
#
# profile.keys() # 키만 뽑아 내기
# key_list = list (profile.keys())
# key_list.append("job")
# print(key_list)
#
# profile.values() # 값만 뽑아 내기
# value_list =list (profile.values())
# print(value_list)
#
# profile.items() # 키 - 값 형태로 다 뽑아내기
# items_list = list(profile.items())
# items_list.append(("jod", "강사"))
# print(items_list)
#
# python_grade = {
#     "동윤" : "B",
#     "길동" : "C",
#     "준식" : "A",
#     "상혁" : "D"
# }
# print(python_grade)
# print(sorted(python_grade.items())) # 키 기준 오름 차순
# print(sorted(python_grade.items(), reverse=True)) # 키 기준 내림 차순
#
# print(sorted(python_grade. items(), key=lambda x: x[1]))
# print(sorted(python_grade. items(), key=lambda x: x[1], reverse=True))
#
student = {}
# 이름 입역 받고 점수도 입력 받고 딕셔너리에 저장
# student = {"name", "찬호", "score": 80}
#  첫번째 방법
student = {
    "name": input("이름 : "),
    "score": int(input("점수 : "))
}
# print(student)
#
# # 두 번째 방법
# student["name"] = input("이름 : ")
# student["score"] = int(input("점수 : "))
# print(student)

# 세트
# 중복을 허용 하지 않고, 순서가 없는 데이터 모음, 정렬x
# 수학 에서 말하는 집합 개념과 유사함

# fruits = {"사과", "바나나", "오렌지"} # -> 세트
# print(fruits)
# apple_str = set("apple")
# print(apple_str)

# num = {1, 2, 5, 5, 6}
# num.add(8) # 추가
# index() # 없는 것을 찾으면 오류 발생
# find() #없는 것을 찾으면 -1 반환
# num.remove(19) # 삭제 없는 것을 삭제 할려면 오류 발생 o
# num.discard(1) # 삭제 없는 것을 삭제 할려면 오류 발생 x
# num.update([10, 11, 12])
# print(num)

# empty_set = set() # 빈 세트를 선엉
#
# num.clear() # 요소 전체 제거
# print(num)

# 세트 핵심 기능
# 합집합, 교집합, 차집합

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# 합집합
# print(a.union(b))
# print(a|b)

# 교집합
# print(a.intersection(b))
# print(a & b)

# 차집합
# print(a.difference(b)) # a에서 b를 뺀다
# print(a-b)

# color = {"b", "l", "u", "e"}
# print(color.pop())
# print(color) # 세트 특징 정렬이 없다

# a = [21, 22, 23, 25, 26]
# b = [22, 24, 27]
# common = set(a) & set(b)
# print(common)

python_class = ["수현", "현호", "지니", "가인"]
java_class = ["현호", "지니", "홍수", "찬호"]

# 공통 으로 출석한 학생:
# 파이썬 만 출석한 학생:
# 자바만 출석한 학생:


# 공통 으로 출석한 학생:
common_class = set(python_class) & set(java_class)
print(common_class)

# 파이썬 만 출석한 학생:
python = set(python_class) - set(java_class)
print(python)

# 자바만 출석한 학생:
java = set(java_class) - set(python_class)
print(java)












