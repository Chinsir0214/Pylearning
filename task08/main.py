# main_8.py

import os
import log_analyzer # 导入我们自己创建的模块

# --- 1. 配置 ---
LOG_FILE = "app.log"
OUTPUT_FILE = "errors.log"
KEYWORD_TO_FIND = "[ERROR]"

# 示例日志内容
SAMPLE_LOG_CONTENT = """2025-10-21 10:00:01 [INFO] User 'admin' logged in successfully.
2025-10-21 10:03:45 [ERROR] Failed to connect to database 'prod_db'.
2025-10-21 10:05:00 [ERROR] Connection timed out after retry.
2025-10-21 10:07:00 [ERROR] NullPointerException at module 'data_processor'.
"""

def run_analysis():
    """
    执行日志分析的完整流程。
    """
    # --- 2. 准备工作 ---
    log_analyzer.create_sample_log(LOG_FILE, SAMPLE_LOG_CONTENT)
    print(f"示例日志文件 '{LOG_FILE}' 已创建。")
    print("\n开始分析日志...")

    # --- 3. 调用核心逻辑 ---
    try:
        error_lines = log_analyzer.analyze_log(LOG_FILE, KEYWORD_TO_FIND)

        # --- 4. 处理结果 ---
        if error_lines is None:
            print(f"错误：无法找到日志文件 '{LOG_FILE}'。")
        elif not error_lines:
            print("分析完成，未发现错误日志。")
        else:
            print(f"分析完成，发现 {len(error_lines)} 条错误日志。")
            log_analyzer.write_log(OUTPUT_FILE, error_lines)
            print(f"所有错误日志已写入到 '{OUTPUT_FILE}' 文件中。")
            
    except Exception as e:
        print(f"发生错误：{str(e)}")
        
    finally:
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
            print(f"\n清理完成，已删除示例文件 '{LOG_FILE}'。")


# 程序主入口
if __name__ == "__main__":
    run_analysis()