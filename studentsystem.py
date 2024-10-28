import re
import json
import os


def menu():
    print("""
    ----------------------------------学生信息管理系统----------------------------------
          

          ==============================功能菜单==============================

          1. 录入学生信息
          2. 查找学生信息
          3. 删除学生信息
          4. 修改学生信息
          5. 排序
          6. 统计学生总数
          7. 显示所有学生信息
          0. 退出系统

          ====================================================================
          说明：通过数字或↑↓方向键选择菜单
    """)


filename = "students.txt"
def save(student):
    try:
        students_txt = open(filename, "a") # 最加模式
    except Exception as e:
        students_txt = open(filename, "w")
    for info in student:
        students_txt.write(str(info) + "\n")
    students_txt.close()


def insert():
    studentlist = []
    mark = True
    while mark:
        id = input("请输入ID 如(1001) :")
        if not id:
            break
        name = input("请输入名字: ")
        if not name:
            break
        try:
            english = int(input(f"请输入英语成绩: "))
            python = int(input(f"请输入python成绩: "))
            c = int(input(f"请输入c语言成绩: "))
        except:
            print(f"输入无效,不是整型数值...重新录入信息")
            continue
        # 将输入的学生信息保存到字典
        student = {"id": id, "name": name, "english": english, "python": python, "c": c}
        studentlist.append(student)
        inputMark = input(f"是否继续添加？ (y/n): ")
        if inputMark == "y":
            mark = True
        else:
            mark = False
    save(studentlist)
    print("学生信息录入完毕!!!")


def search():
    pass


def delete():
    mark = True
    while mark:
        studentId = input(f"请输入要删除的学生ID: ")
        if studentId is not "":
            if os.path.exists(filename):
                with open(filename, "r") as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list)) # 字符串转换成字典
                        if d["id"] != studentId:
                            wfile.write(str(d) + "\n") # 将学生信息写入文件
                        else:
                            ifdel = True
                    if ifdel:
                        print(f"ID为{studentId} 的学生信息已经被删除...")
                    else:
                        print(f"没有找到ID为{studentId}的学生信息...")
            else:
                print(f"无学生信息...")          
                break
            show()
            inputMark = input(f"是否继续删除?  (y/n) :")
            if inputMark == "y":
                mark = True
            else:
                mark = False

def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


def main():
    ctrl = True
    while (ctrl):
        menu()
        option = input("请选择...")
        option_str = re.sub(r"\D",'', option)
        if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_int = int(option_str)
            if option_int == 0:
                print('您已退出学生管理系统！')
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()


if __name__ == "__main__":
    main()