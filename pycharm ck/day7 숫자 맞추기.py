import random

# 난이도 선택 유효성 감사를 위한 난이도 리스트
difficulty_list = ["쉬움", "보통", "어려움"]
try_count = 0 # 시도 횟수 변수
guess = 0 # 내가 추측한 숫자 변수
difficulty = "" # 난이도 를 입력 하는 변수
max_try_count = 0 # 최대 시도 횟수 변수
max_range = 0 # 최대 범위 변수

# 난이도 선택 유효성 검사
while True:
    # 난이도 입역 받음
    difficulty = input("난이도를 선택해 주세요(쉬움, 보통, 어려움)")
    # 만약에 입력 받은 난이도 가 난이도 리스트 안에 있는 요소 중 하나 이면
    if difficulty in difficulty_list:
        break
    else:
        # 난이도 리스트 에 없는 입력 값 -- 재입력
        print("다시 난이도를 입력해 주세요")
        continue

# 난이도 선택때 설정 되는 최대 시도 횟수, 최대 범위
if difficulty == "쉬움":
    max_try_count = 10
    max_range = 50
elif difficulty =="보통":
    max_try_count = 7
    max_range = 70
else:
    max_try_count = 5
    max_range = 100
# 선택된 난이도에 따라 랜덤 숫자 최대 범위는 달라진다
correct_answer = random.randint(1, max_range)
print(f"선택된 난이도 -- {difficulty} 랜덤 범위 -1~{max_range} 최대 시도 횟수-{max_try_count}")
#==============================================

# 여기가 본체
while True:
    # 시도 횟수와 최대 시도 횟수가 같아 지면 게임 종료
    if try_count == max_try_count:
        print(f"최대 시도 횟수에 도달 했습 니다. 게임 종료. 정답은{correct_answer} ")
        break

    input_str = input("숫자를 입력해 주세요 : ") # 문자열
    if input_str.isdigit():
        guess = int(input_str)
    else:
        print("숫자를 입력해 주세요!!!")
        continue

# 게임 진행
    try_count += 1  # 시도 횟수 증가

    print(f"시도 횟수 : {try_count}")

    if correct_answer > guess:
        print("UP")

    elif correct_answer < guess:
        print("DOWN")

    else:
        print("정답 입니다!!")
        break