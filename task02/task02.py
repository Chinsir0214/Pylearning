import random

# 生成一个 1 到 100 之间的随机整数
target_number = random.randint(1, 100)
guess = 0 # 初始化猜测的数字

print("猜数字游戏开始！我已经想好了一个 1 到 100 之间的整数。")

# 当猜测的数字不等于目标数字时，循环继续
while guess != target_number:
    try:
        # 提示用户输入并转换为整数
        guess_str = input("请输入你猜的数字: ")
        guess = int(guess_str)

        # 进行判断
        if guess > target_number:
            print("太大了，再猜小一点。")
        elif guess < target_number:
            print("太小了，再猜大一点。")
        else:
            print(f"恭喜你，猜对了！答案就是 {target_number}。")
            
    except ValueError:
        # 如果用户输入的不是有效的数字，则捕获异常并提示
        print("无效的输入，请输入一个整数。")