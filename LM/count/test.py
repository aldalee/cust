import re

with open(r"./data/sum.txt", encoding='utf-8') as f:
    data = f.read()
    data = re.findall(r'[a-zA-Z]+',data)
    # data = re.sub("\（.*?\）", " ", data)
    data = ' '.join(data)
    print(data)
with open("./data/sum.txt","w") as f:
    f.write(data)
