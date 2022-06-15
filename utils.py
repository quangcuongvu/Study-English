import json
import os
import subprocess
import time

from translate import Translator

start = time.time()
# //3 days,7 days ..
array_time_repeat = ["1", "2", "3", "5", "7", "10", "13"]
language = "en"


def get_next_time_practice(current_nb_repeat):
    current_time_stamp = int(time.time())  # (s)

    if current_nb_repeat > len(array_time_repeat) - 1:
        return current_time_stamp + int(array_time_repeat[-1]) * 24 * 3600
    else:
        return (
            current_time_stamp + int(array_time_repeat[current_nb_repeat]) * 24 * 3600
        )


def ham_write_json(dict_data, path_json_file):
    with open(path_json_file, "w") as json_file:
        json.dump(dict_data, json_file)


def ham_read_json(path_json_file):
    data = ""
    with open(path_json_file) as json_file:
        data = json.load(json_file)
    return data


def ham_on_bai(word):
    current_word = word["word"]
    current_word = current_word.replace("  ", " ")
    current_tran = word["tran"]
    print(current_word)
    print(current_tran)

    while True:
        current_sentence_user = input()

        if current_sentence_user.lower().strip() == current_word.lower().strip():
            print("\n")
            break
        else:
            print("Repeat...")
    elapsed = (time.time() - start) / 60
    a = round(elapsed, 2)
    print("Time: ", +a, " minute")
