students_marks = dict()
school = list()
for _ in range(0, int(input())):
    data = input().split()
    students_marks['student'] = str(data[0])
    students_marks['math'] = float(data[1])
    students_marks['physics'] = float(data[2])
    students_marks['chemistry'] = float(data[3])
    school.append(students_marks.copy())

student = str(input())

if students_marks['student'] == student:
    mean = round(Decimal((students_marks['chemistry'] + students_marks['physics'] + students_marks['math'])/3),2)
    print('{0: .2f}'.format(mean))
