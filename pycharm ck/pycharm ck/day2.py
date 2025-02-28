#
# a = "Life is too short, You need Python"
# print(len(a)) # 문자열 길이
# print(a.count("t", 5, 10)) # 문자가 몇개 있는지
# print(a.index("t")) # 앞에서 부터 찾는데 해당 문자의 인덱스 번호
# print(a.find("x")) # 문자열 에 만 사용
# print(a.lower()) #upper 소문자/대문자
# print(a[0]. isupper())
# print(a.replace("too ","top "))
# print(a)
# b = "a:b:c:d"
# print(b.split(":"))

email = input("email : ") # htg145@naver.com
# id는 htg145
email_id = email.split("@")[0]
print("id는:", email_id)

email.find("@") # index 번호
print(email[:email.find("@")])




















