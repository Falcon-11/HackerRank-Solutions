l = []
s = []
n = int(input())

for _ in range(n):
    name = input()
    score = float(input())
    l.append([name, score])
    s.append(score)

s = sorted(list(set(s)))
second_lowest = s[1]

for a, b in sorted(l):
    if b == second_lowest:
        print(a)