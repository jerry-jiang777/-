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


def show_student(studentList):
    if not studentList:
        print(f"(o@.@o) 无数据信息 (o@.@o) \n")
        return
    else:
        for info in studentList:
            print(f"学生ID: {info['id']}, 姓名: {info['name']}, english: {info['english']}, python: {info['python']}, c: {info['c']}")


def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename): # 判断文件是否存在
            mode = input(f"按ID查输入1, 按姓名查输入2: ")
            if mode == "1":
                id = input(f"请输入学生ID: ")
            elif mode == "2":
                name = input(f"请输入学生姓名：")
            else:
                print(f"您输入的有误，请重新输入！")
                search()
            with open(filename, "r") as file:
                student = file.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id is not "":
                        if d["id"] == id:
                            student_query.append(d)                                
                    elif name is not "":
                        if d["name"] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input(f"是否继续查询？ (y/n): ")  
                if inputMark == 'y':
                    mark = True
                else:
                    mark = False
        else:
            print(f"暂未保存数据信息...")
            return


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
    show()
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
    else:
        return
    studentid = input(f"请输入要修改的学生ID: ")
    with open(filename, "w") as wfile: # 以只写的模式打开文件
        for student in student_old:
            d = dict(eval(student)) # 字符串转换成字典
            if d['id'] == studentid: # 是否是要修改的学生
                print(f"找到了这名同学，可以修改他的信息！")
                while True:
                    try:
                        d["name"] = input(f"请输入姓名: ")
                        d["english"] = int(input(f"请输入英语成绩: "))
                        d["python"] = int(input(f"请输入python成绩: "))
                        d["c"] = int(input(f"请输入c语言成绩: "))
                    except:
                        print(f"您输入的有误，请重新输入: ")
                    else:
                        break
                student = str(d) # 将字典转换成字符串
                wfile.write(student + "\n")
            else:
                wfile.write(student)
    mark = input(f"是否继续修改其他学生信息？ (y/n): ")
    if mark == "y":
        modify()
def sort():
    pass


def total():
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
            if student_old:
                print(f"共有{len(student_old)} 名学生! ")
    else:
        print(f"暂未保存数据信息...")


def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
            if student_old:
                for list in student_old:
                    d = dict(eval(list))
                    student_new.append(d)
                if student_new:
                    show_student(student_new)
    else:
        print(f"暂未保存数据信息...")


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