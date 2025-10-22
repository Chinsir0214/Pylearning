# 外层循环控制行数 (从 1 到 9)
for i in range(1, 10):
    # 内层循环控制列数 (从 1 到当前行数 i)
    for j in range(1, i + 1):
        # 计算乘积
        product = i * j
        # 打印表达式
        # print() 函数的 end 参数可以控制打印结束后的字符，默认为换行符 '\n'
        # 我们把它设置为空格或者制表符，让后续内容在同一行输出
        print(f"{j}x{i}={product}\t", end="")
    
    # 在每一行的所有表达式都打印完毕后，执行一个空的 print() 来换行
    print()