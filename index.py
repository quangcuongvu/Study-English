import json
import time
import utils
path_json_file='tuvung.json'
data=utils.ham_read_json(path_json_file)
# print(data)
current_time_stamp=int(time.time()) #(s)

print(data.keys())
print('Enter a deck name which you want to learn:')
current_deck=input() #'6000 basic word'
start = time.time()
list_words=data[current_deck]
print("=== Better than yesterday ===")
for i in range(len(list_words)):
    word=list_words[i]
    print('\nMời bạn nhập từ mới 😍: ')
    if int(word['next_time'])<current_time_stamp:
        # print(word)
        utils.ham_on_bai(word)
        #update file json
        current_nb_repeat=int(word['nb_repeat'])
        list_words[i]['nb_repeat']=current_nb_repeat+1
        list_words[i]['next_time']=utils.get_next_time_practice(current_nb_repeat)
        data[current_deck]=list_words
        utils.ham_write_json(data,path_json_file)

elapsed = time.time() - start
