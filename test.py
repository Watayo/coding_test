"""
このファイルに解答コードを書いてください
"""
test = open('input.txt')
lines = test.readlines()

lists = []

for line in lines[:-1]:
    cha = line.strip()
    lists.append(list(cha.split(":")))

final = int(lines[-1])
lists = sorted(lists, key=lambda a: int(a[0]))

i = 0
bool_ans = False
ans = ""
for i in range(len(lists)):
    if (final % int(lists[i][0]) == 0):
        bool_ans = True
        ans += lists[i][1]

if (bool_ans == False):
    ans += str(final)

print(ans)

test.close()
