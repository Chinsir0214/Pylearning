# main_9.py

import student_manager # 导入核心逻辑模块

DATA_FILE = "students.json"

def display_menu():
    """显示主菜单。"""
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加新学生")
    print("2. 查找学生")
    print("3. 显示所有学生")
    print("4. 计算平均成绩")
    print("5. 退出系统")
    print("==========================")

def handle_add_student(students):
    """处理添加学生的交互逻辑。"""
    print("\n--- 添加新学生 ---")
    student_id = input("请输入学生ID: ")
    name = input("请输入学生姓名: ")
    try:
        grade = float(input("请输入学生成绩: "))
    except ValueError:
        print("无效的成绩，请输入一个数字。")
        return
    
    success, message = student_manager.add_student(students, student_id, name, grade)
    print(message)
    if success:
        student_manager.save_students(DATA_FILE, students)

def handle_find_student(students):
    """处理查找学生的交互逻辑。"""
    student_id = input("请输入要查找的学生ID: ")
    student = student_manager.find_student_by_id(students, student_id)
    if student:
        print("\n--- 找到学生信息 ---")
        print(f"ID: {student['id']}, 姓名: {student['name']}, 成绩: {student['grade']}")
        print("--------------------")
    else:
        print(f"未找到ID为 '{student_id}' 的学生。")

def handle_show_all(students):
    """处理显示所有学生的逻辑。"""
    print("\n--- 所有学生信息 ---")
    if not students:
        print("系统中没有任何学生信息。")
    else:
        for student in students:
             print(f"ID: {student['id']}, 姓名: {student['name']}, 成绩: {student['grade']}")
    print("--------------------")

def handle_calculate_average(students):
    """处理计算平均成绩的逻辑。"""
    average = student_manager.calculate_average_grade(students)
    if average > 0:
        print(f"\n当前共有 {len(students)} 名学生，平均成绩为: {average:.2f}")
    else:
        print("系统中没有任何学生信息。")

def main():
    """程序主循环。"""
    students_data = student_manager.load_students(DATA_FILE)
    
    while True:
        display_menu()
        choice = input("请输入您的选择 (1-5): ")
        
        if choice == '1':
            handle_add_student(students_data)
        elif choice == '2':
            handle_find_student(students_data)
        elif choice == '3':
            handle_show_all(students_data)
        elif choice == '4':
            handle_calculate_average(students_data)
        elif choice == '5':
            # 数据在每次成功添加后已经保存，退出时无需额外操作
            print("感谢使用，系统已退出。")
            break
        else:
            print("无效的输入，请输入 1 到 5 之间的数字。")

if __name__ == "__main__":
    main()