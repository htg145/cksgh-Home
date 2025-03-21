import json
import random

def review():
    with open("../review_note.json", "r", encoding="utf-8") as review_file:
        word_list = list(json.load(review_file))
        incorrect_cound = 0
        for word_index in range(0, len(word_list)):
            print("=============================")
            input_eng = ("단어 :")
            if input_eng == word_list[word_index]["word"]:
                print("정답 입니다.")
            elif input_eng != word_list[word_index]["word"]:
                print("오답입니다.")
                print(f"정답 : {word_list[word_index]}")

