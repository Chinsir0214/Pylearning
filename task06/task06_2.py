def count_word_frequency(text_to_analyze):
    """
    接收一段文本，返回一个包含单词频率的字典。
    """
    # 预处理文本
    text_to_analyze = text_to_analyze.lower().replace('.', '').replace(',', '')
    
    # 分割单词
    words = text_to_analyze.split()
    
    # 计数
    word_counts = {}
    for word in words:
        # dict.get(key, default) 是一个更简洁的计数方法
        # 如果 word 存在，返回它的值；如果不存在，返回默认值 0
        word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

# --- 主程序部分 ---
if __name__ == "__main__":
    sample_text = """
    Python is an amazing language. Python is versatile and easy to learn.
    Learning Python opens up many opportunities in data science, web development, and automation.
    """

    # 调用函数并获取结果
    frequency_dict = count_word_frequency(sample_text)

    # 打印结果
    print("单词频率统计结果 (函数版):")
    for word, count in frequency_dict.items():
        print(f"'{word}': {count}")