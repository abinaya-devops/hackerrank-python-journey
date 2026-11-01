
n = int(input())

student_marks = {}

for i in range(n):
    name, *line = input().split()
    marks = list(map(float, line))
    student_marks[name] = marks

query_name = input()

average = sum(student_marks[query_name]) / len(student_marks[query_name])

print(f"{average:.2f}")
