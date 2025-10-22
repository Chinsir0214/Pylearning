# 一段用于分析的示例文本
text = """
Python is an amazing language. Python is versatile and easy to learn.
Learning Python opens up many opportunities in data science, web development, and automation.
"""

print("原始文本:")
print(text)

# 1. 预处理文本：转换为小写，移除标点符号
#    这可以确保 'Python' 和 'python' 被视为同一个单词
text = text.lower()
text = text.replace('.', '')
text = text.replace(',', '')

# 2. 将文本分割成单词列表
words = text.split()

# 3. 初始化一个空字典来存储单词频率
word_counts = {}

# 4. 遍历单词列表并计数
for word in words:
    if word in word_counts:
        # 如果单词已经存在于字典中，将其计数值加 1
        word_counts[word] += 1
    else:
        # 如果单词是第一次出现，将其添加到字典中，计数值设为 1
        word_counts[word] = 1

# 5. 打印结果
print("\n单词频率统计结果:")
# .items() 方法可以同时遍历字典的键和值
for word, count in word_counts.items():
    print(f"'{word}': {count}")