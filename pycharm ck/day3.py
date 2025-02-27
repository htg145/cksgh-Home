# # 컬렉션
# # 리스트 (List)
# # 튜플 (Tuple)
# # 컬렉션 (List"리스트", Tuple"튜플", Dictionary"딕셔너리", Set"세트")
# # 여러 개의 데이터를 저장하고 관리하는 구조 "컬렉션"
#
#
# #숙제
# # email = input("email : ") # htg145@naver.com
# # id는 htg145
# # email.find("@") # 4 -> index번호
# # print(email.split("@")[0])
# # print(email[:email.find("@")]) # 슬라이싱 이게 더 좋다
#
# # 리스트(List) : 순서가 있고, 중복가능, 요소 추가/삭제 가능, 변경 가능
# fruits = ["appie", "banana", "cherry"] # 문자열 리스트
# # to_do_list = ["쉼쉬기", "자기", "밥먹기"]
# numbers = [6, 3, 1, 5] # 숫자 리스트
# # bools = [True, False, True] # 불리언 리스트
# mixed_list = ["안녕하세요", 3, True]
# # print(fruits)
# # print(mixed_list)
# # print(fruits[2][1])
# # print(fruits[-2])
# #
# # fruits[0] = "orange" # 요소 수정
# # print(fruits)
# #
# # numbers.append("hi") # 마지막 자리에 요소 추가
# # print(numbers)
# # numbers.insert(1, 2) # 특정 자리에 요소 추가
# # # print(numbers.pop()) # 리스트 의 마지막 요소가 리턴 된다
# # print(numbers.remove("hi"))
#
# # del numbers[2] # 삭제
# # print(numbers)
# #
# # print(len(mixed_list)) # 리스트 의 길이
#
# # numbers.sort()
# # print(numbers)
# # fruits.sort()
# # print(fruits)
# # bools.sort()
# # print(bools)
# #
# # numbers.sort(reverse=True) #sort()작은순 옵션 reverse=True 큰순
# # print(numbers)
#
# # numbers.reverse() # 그냥 순서를 거꾸로
# # print(numbers)
#
# # fruits = "-".join(fruits) # 이어 붙이기
# # print(fruits)
# #
# # cart = []
# #
# # # 추가할 상품 : 입력
# # # 추가할 상품 : 입력
# # # 추가할 상품 : 입력
# # # 장바 구니 목록
# #
# # cart.append(input("추가할 상품 : "))
# # cart.append(input("추가할 상품 : "))
# # cart.append(input("추가할 상품 : "))
#
# # print(cart)
#
# # 튜플(Tuple)
#
# # 순서가 있지만, 요소 변경 불가능 -> 변경불가능
# # contract = ("계약기간:100년", "시급:100", "보증금:500만원")
# # birth_into = ("김철수", 1995, "서울")
# # print(contract)
#
# colors = ("red", "green", "black") # 변경 불가능
# numbers = (1, 5, 3, 9, 1, 2)
# bools = (True, False, True)
# mixed_tuple = ("red", 1, True)
#
# a = ("float",) # 요소가 하나일때는 마지막 쉼표!!
#
# print(colors[1])
# # colors[1] = "yellow" # 튜플은 변경 불가능
# print(numbers[0:2]) # 슬라이싱 가능
# print(numbers.count(1))
# print(numbers.index(3))
#
# a, b, c = colors
# print(c)

# 숙제 풀이: 이메일 ID 추출

email = input("이메일: ")  # htg145@naver.com
id = email[:email.find("@")]  # @ 앞까지 슬라이싱
print(id)