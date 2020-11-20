n = int(input())
student_score = {}

for j in range(n):
    name, *line = input().split()
    marks = list(map(float, line))
    student_score[name] = marks

query_name = input()
avg_score = sum(student_score[query_name])
result = avg_score/3

print("%.2f"%(result))