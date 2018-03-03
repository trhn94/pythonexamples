def create_student():
    ogrenci1= input("adınızı giriniz:")
    homeworks = []
    quiz = []

    for i in range(3):
        odevnot = int(input("notlarınızı giriniz:"))
        homeworks.append(odevnot)
        quiznot = int(input("quiz notu giriniz:"))
        quiz.append(quiznot)

    st1= {"name": ogrenci1, "homeworks": homeworks, "quiz": quiz}
    print(st1)
    return st1


def calculate_average(students):
    tstudent = {}
    for key, value in students.items():
        haverage = sum(value["homeworks"]) / len(value["homeworks"])
        qaverage = sum(value["quiz"]) / len(value["quiz"])
        average = (haverage + qaverage) / 2
        tstudent.update({key: {"name": value["name"], "haverage": haverage, "qaverage": qaverage, "average": average}})

    return tstudent

# students= []
# for i in range(2):
#     x= create_student()
#     students.append(x)
# print(students)

students= {}
for i in range(2):
    a = create_student()
    key = "student" + str(i+1)
    students.update({key: a})
print(students)

print(calculate_average(students))





