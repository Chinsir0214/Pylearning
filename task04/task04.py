# 初始化一个空的列表来存储待办事项
todo_list = []

print("--- 欢迎使用待办事项列表 ---")

# 使用一个无限循环让程序持续运行，直到用户选择退出
while True:
    # 打印菜单选项
    print("\n请选择一个操作:")
    print("1. 添加事项")
    print("2. 查看所有事项")
    print("3. 删除事项")
    print("4. 退出程序")

    choice = input("请输入您的选择 (1-4): ")

    if choice == '1':
        # 添加事项
        item = input("请输入要添加的待办事项: ")
        todo_list.append(item)
        print(f"'{item}' 已成功添加!")
    
    elif choice == '2':
        # 查看所有事项
        print("\n--- 您的待办事项 ---")
        if not todo_list: # 检查列表是否为空
            print("目前没有待办事项。")
        else:
            # enumerate 函数可以同时获取索引和值，非常方便
            for index, item in enumerate(todo_list):
                print(f"{index + 1}. {item}")
        print("--------------------")

    elif choice == '3':
        # 删除事项
        if not todo_list:
            print("列表已空，无法删除。")
            continue # continue 会跳过本次循环的剩余部分，直接开始下一次循环

        # 先显示列表，方便用户选择要删除的项
        for index, item in enumerate(todo_list):
            print(f"{index + 1}. {item}")
        
        try:
            item_num_str = input("请输入要删除的事项编号: ")
            item_num = int(item_num_str)
            
            # 检查编号是否有效
            if 1 <= item_num <= len(todo_list):
                # pop 方法会移除指定索引的元素并返回它
                removed_item = todo_list.pop(item_num - 1) # 列表索引从0开始，所以用户输入的编号需要减1
                print(f"事项 '{removed_item}' 已被删除。")
            else:
                print("无效的编号。")
        except ValueError:
            print("请输入一个有效的数字。")

    elif choice == '4':
        # 退出程序
        print("感谢使用，再见！")
        break # break 会跳出整个 while 循环

    else:
        # 处理无效输入
        print("无效的选择，请输入 1 到 4 之间的数字。")