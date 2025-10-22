# student_manager.py

import json

def load_students(filepath):
    """从 JSON 文件加载学生数据。"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(filepath, students_data):
    """将学生数据保存到 JSON 文件中。"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(students_data, f, indent=4, ensure_ascii=False)

def add_student(students, student_id, name, grade):
    """
    向学生列表中添加一个新学生。
    返回 (bool, str): 表示操作是否成功以及相应的消息。
    """
    # 检查ID是否已存在
    if any(s['id'] == student_id for s in students):
        return False, f"错误：学生ID '{student_id}' 已存在。"
    
    students.append({"id": student_id, "name": name, "grade": grade})
    return True, f"学生 '{name}' 添加成功。"

def find_student_by_id(students, student_id):
    """
    根据ID查找学生。
    返回: 找到的学生字典，否则返回 None。
    """
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def calculate_average_grade(students):
    """
    计算平均成绩。
    返回: 平均分（float），如果没有学生则返回 0.0。
    """
    if not students:
        return 0.0
    
    total = sum(s['grade'] for s in students)
    return total / len(students)