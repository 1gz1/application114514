import json
import os

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 构造 JSON 文件的完整路径
json_path = os.path.join(current_dir, 'const.json')

# 打开并读取 JSON 文件
try:
    with open(json_path, 'r', encoding='utf-8') as file:
        const = json.load(file)

except FileNotFoundError:
    print(f"文件 {json_path} 未找到。请检查文件路径是否正确，并确保文件存在。")
except json.JSONDecodeError:
    print(f"文件 {json_path} 解析错误。请检查文件内容是否为有效的 JSON 格式。")
