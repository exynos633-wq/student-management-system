FILE_NAME = "students.txt"
#添加学生
def add_student():
    name = input("请输入学生姓名：")

    try:
        score = int(input("输入学生成绩："))
    except:
        print("成绩必须是数字")
        return 

    if score < 0 or score >100:
        print("成绩必须在0~100之间")
        return 

    with open(FILE_NAME,'a',encoding='utf-8') as f:
        f.write(f"{name},{score}\n")

#读取所有学生

def load_students():
    students = []

    try:
        with open(FILE_NAME,'r',encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                data = line.split(",")

                student = {'name': data[0],'score':int(data[1])}
                students.append(student)

    except FileNotFoundError:
        pass
    return students

#查看所有学生

def show_students():
    students = load_students()

    if not students:
        print("暂无学生数据")
        return

    print('\n=====学生列表=====')

    for i ,s in enumerate(students,start=1):
        print(f"{i}. {s['name']} - {s['score']}")

#计算平均分

def show_average():
    students = load_students()

    if not students:
        print('暂无学生数据')
        return
    total = sum(s['score'] for s in students)
    average = total/len(students)

    print(f"平均分:{average:.2f}")

#查询最高分

def show_top_student():
    students = load_students()

    if not students:
        print('暂无学生数据')
        return
    top = max(students,key=lambda x:x['score'])

    print('最高分学生：')
    print(f"姓名：{top['name']}")
    print(f"成绩：{top['score']}")

#按姓名搜索

def find_student():
    students = load_students()

    if not students:
        print('暂无学生数据')
        return

    keyword = input('输入想要搜索的姓名：')

    found = False

    for s in students:
        if keyword.lower() in s['name'].lower():
            print(f"找到学生：{s['name']} - {s['score']}")
            found = True

    if not found:
        print('未找到该学生')

#主菜单

def menu():
    while True:
        print('\n=====成绩管理系统=====')
        print('1.添加学生')
        print('2.查看所有学生')
        print('3.查看平均分')
        print('4.查看最高分')
        print('5.搜索学生')
        print('6.退出系统')

        choice = input('请选择功能')

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()
        elif choice == "3":
            show_average()
        elif choice == "4":
            show_top_student()
        elif choice == "5":
            find_student()
        elif choice == "6":
            print("系统已退出")
            break
        else:
            print("无效选项，请重新选择")

#程序入口

menu()
