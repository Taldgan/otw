from collections import Counter
import collections
with open("found1") as f:
    letters = ""
    while True:
        data = f.read(1)
        letters += data + "\n"
    #print(data)
        if not data:
            break
    c = Counter(letters).most_common()
    print(c)
        
