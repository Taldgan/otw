import sys
s = ""
for i in range(len(sys.argv[1])-1, -1, -1):
    s += sys.argv[1][i]
print(s)

