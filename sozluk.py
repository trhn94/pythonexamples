student= {"name": "turhan", "courses": ["math", "physics", "biology"], "instructors": ["fatos", "kader"]}
s1= {"grades": [90, 85, 70]}
student.update(s1)
student["courses"].sort()
x= sum(student["grades"])/ len(student["grades"])
print(student)
print(x)
student["instructors"].remove("kader")
print(student)