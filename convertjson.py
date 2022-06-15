import csv
import json

data = {}
data["unit4"] = []
with open("unit4.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        # print(row)
        id = row[0]
        word = row[1]
        mean = row[2]
        if word != "word":
            data["unit4"].append(
                {"id": id, "word": word, "tran": mean, "nb_repeat": 0, "next_time": 0}
            )
# print(data)
with open("tuvung.json", "a+") as outfile:
    json.dump(data, outfile)
