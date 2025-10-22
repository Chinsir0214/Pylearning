# log_analyzer.py

def analyze_log(filepath, keyword="[ERROR]"):
    """
    分析指定的日志文件，找出包含特定关键字的行。

    Args:
        filepath (str): 日志文件的路径。
        keyword (str): 要搜索的关键字，默认为 '[ERROR]'。

    Returns:
        list: 包含所有匹配关键字的行的列表。
              如果文件未找到，则返回 None。
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # 使用列表推导式高效地找出所有匹配的行
            found_lines = [line for line in f if keyword in line]
        return found_lines
    except FileNotFoundError:
        return None # 返回 None 表示文件不存在

def write_log(filepath, lines_to_write):
    """
    将一个行列表写入到指定的文件中。

    Args:
        filepath (str): 输出文件的路径。
        lines_to_write (list): 要写入的字符串列表。
    """
    with open(filepath, "w", encoding="utf-8") as f:
        # .writelines() 可以高效地写入一个列表的所有行
        f.writelines(lines_to_write)

def create_sample_log(filepath, content):
    """
    (辅助函数) 创建一个用于演示的日志文件。
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)