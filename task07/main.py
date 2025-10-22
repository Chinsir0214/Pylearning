# 这个文件是主程序，它会导入并使用我们创建的 calculator 模块。

# 从 calculator.py 文件中导入我们定义的所有函数
import calculator

# 使用模块中的函数
num1 = 10
num2 = 5

sum_result = calculator.add(num1, num2)
print(f"{num1} + {num2} = {sum_result}")

diff_result = calculator.subtract(num1, num2)
print(f"{num1} - {num2} = {diff_result}")

prod_result = calculator.multiply(num1, num2)
print(f"{num1} * {num2} = {prod_result}")

quot_result = calculator.divide(num1, num2)
print(f"{num1} / {num2} = {quot_result}")

# 测试除以零的情况
zero_div_result = calculator.divide(num1, 0)
print(f"{num1} / 0 = {zero_div_result}")