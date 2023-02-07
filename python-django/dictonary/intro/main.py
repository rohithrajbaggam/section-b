dict1 = {
        "name" : "max",
        "age" : 21,
        "university" : "ABC University",
        "grade" : {
            "10th" : 90,
            "12th" : 80,
            "be" : 85 
        }
    }
dict2 = {
        "name" : "lucy",
        "age" : 20,
        "university" : "ABC University",
        "grade" : {
            "10th" : 92,
            "12th" : 83,
            "be" : 84 
        }
    }
student = [dict1, dict2] 

for i in student:
    # print(i)
    for j in i.keys():
        print(j, i[j])

# for i in range(len(student)):
#     for j in student[i].keys():
#         print(j,student[i][j])
#     print()
# student = {
#     1 : {
#         "name" : "max",
#         "age" : 21,
#         "university" : "ABC University",
#         "grade" : {
#             "10th" : 90,
#             "12th" : 80,
#             "be" : 85 
#         }
#     }, 
#     2 : {
#         "name" : "lucy",
#         "age" : 20,
#         "university" : "ABC University",
#         "grade" : {
#             "10th" : 92,
#             "12th" : 83,
#             "be" : 84 
#         }
#     }
# }

# for i in student.keys():
#     # print(i, student[i].keys())
#     for j in student[i].keys():
#         print(i, j, student[i][j])
#     print()
    # for j in student[i].
#print(student[2]["name"])
#for i,j in student.items():
   # print(i,j)

# for i in student.keys():
#     for j in student[i].keys():
#         print(j,student[i][j])
#     print()
# from pprint import pprint

# student = {
#     "name" : "max",
#     "age" : 21,
#     "university" : "ABC University",
#     "grade" : {
#         "10th" : 90,
#         "12th" : 80,
#         "be" : 85 
#     }
# }
# for i in student.keys():
#     print(i, student[i])
# pprint(student)
# student["branch"] = "CSE"
# print()
# print()
# pprint(student)
# grade = student["grade"]
# print(grade["12th"])
# print(student["grade"]["12th"])




# grade = student["grade"]
# print(grade["be"])
# print(student["grade"]["be"])
# print(student["university"])

# for i in student.keys():
#     print(i, student[i])




