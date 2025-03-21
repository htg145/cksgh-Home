# 영어 단어장 만들기
# 기능 : 난이도 선택, 랜덤 으로 단어뜻 출력
# 해당 영어 단어를 입력 => 정답: 다음 으로
# 틀리면 오답 노트 리스트 만들 어서 데이터 셋
# 메뉴 에서 복습 하기 => 오답 노트에 있는 거 가져 온다
# 흐름
# 메뉴 선택 - 공부 하기 - 난이도 선택
# 정답 맞추기 - 틀리면 오답 리스트
# 메뉴 선택 - 복습 하기 - 틀렷던 오답 리스트 불러 오기 - 공부 하기
from mypackage.study.study import study
from mypackage.review.review import review

while True:
    print("=======메뉴========")
    print("""
        1. 초등
        2. 중고
        3. 전문
        4. 오답 노트
        5. 종료
    """)

    choice = input("메뉴를 선택 하세요. : ")
    if choice == "1":
        study("초등")
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    elif choice == "5":
        break
    else:
        print("다시 선택해 주세요.")
        continue