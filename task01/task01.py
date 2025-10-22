# 提示用户输入信息
name = input("请输入您的姓名: ")
age_str = input("请输入您的年龄: ")
favorite_color = input("请输入您最喜欢的颜色: ")

# 将年龄从字符串转换为整数（可选，但推荐）
age = int(age_str)

# 使用 f-string 格式化输出
# f-string 是 Python 中非常常用和方便的字符串格式化方法
print(f"你的名字是 {name}，今年 {age} 岁，最喜欢的颜色是 {favorite_color}。")