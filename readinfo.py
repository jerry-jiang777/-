# infos = open("students.txt", "r")
# info_pbj = infos.readlines()
# for i in info_pbj:
#     print(i)
import json


# with open("students.txt", "r", encoding='utf-8') as reader:
#     studentinfos = reader.readlines()
#     for student in studentinfos:
#         print(student, type(student))
#         s = student.strip()
#         s_dict = json.loads(s)
#         print(s_dict)
#         print(type(s_dict))
with open("students.txt", "r") as file:
    content = file.readlines()
    for info in content:
        # print(info)
        info  = info.replace('"', "'")
        print(info)