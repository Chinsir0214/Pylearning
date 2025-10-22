# 这个文件是我们的模块，它包含可重用的函数。

def add(a, b):
    """返回两个数的和"""
    return a + b

def subtract(a, b):
    """返回两个数的差"""
    return a - b

def multiply(a, b):
    """返回两个数的积"""
    return a * b

def divide(a, b):
    """
    返回两个数的商。
    包含一个检查以防止除以零的错误。
    """
    if b == 0:
        return "错误：不能除以零"
    return a / b