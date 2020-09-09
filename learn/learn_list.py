
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = []
for student in students:
    scores.append(student[1])

low_score = min(scores)
max_score = max(scores)

for score in scores:
    if low_score < score < max_score:
        low_score = score

for student in students:
    if student[1] == low_score:
        print(student[0])






