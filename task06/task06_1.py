def show_menu():
    """打印主菜单"""
    print("\n请选择一个操作:")
    print("1. 添加事项")
    print("2. 查看所有事项")
    print("3. 删除事项")
    print("4. 退出程序")

def add_item(todo_list):
    """向待办列表中添加一个新事项"""
    item = input("请输入要添加的待办事项: ")
    todo_list.append(item)
    print(f"'{item}' 已成功添加!")

def view_items(todo_list):
    """显示所有待办事项"""
    print("\n--- 您的待办事项 ---")
    if not todo_list:
        print("目前没有待办事项。")
    else:
        for index, item in enumerate(todo_list):
            print(f"{index + 1}. {item}")
    print("--------------------")

def remove_item(todo_list):
    """从待办列表中删除一个指定的事项"""
    if not todo_list:
        print("列表已空，无法删除。")
        return

    view_items(todo_list) # 先显示列表方便用户选择
    try:
        item_num = int(input("请输入要删除的事项编号: "))
        if 1 <= item_num <= len(todo_list):
            removed_item = todo_list.pop(item_num - 1)
            print(f"事项 '{removed_item}' 已被删除。")
        else:
            print("无效的编号。")
    except ValueError:
        print("请输入一个有效的数字。")

def main_todo_app():
    """待办事项应用的主函数"""
    todos = []
    print("--- 欢迎使用待办事项列表 (函数版) ---")
    while True:
        show_menu()
        choice = input("请输入您的选择 (1-4): ")
        if choice == '1':
            add_item(todos)
        elif choice == '2':
            view_items(todos)
        elif choice == '3':
            remove_item(todos)
        elif choice == '4':
            print("感谢使用，再见！")
            break
        else:
            print("无效的选择，请输入 1 到 4 之间的数字。")

# 运行主程序
if __name__ == "__main__":
    main_todo_app()