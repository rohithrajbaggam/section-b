
student = {
    "name" : "max",
    "age" : 21,
    "university" : "ABC University",
    "grade" : {
        "10th" : 90,
        "12th" : 80,
        "be" : 85 
    }
}
grade = student["grade"]
print(grade["be"])
print(student["grade"]["be"])
# print(student["university"])

# for i in student.keys():
#     print(i, student[i])




