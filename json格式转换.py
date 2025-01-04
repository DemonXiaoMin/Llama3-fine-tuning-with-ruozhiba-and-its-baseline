import json

# 打开JSON文件并加载数据，保留原始中文
with open('D:/萧珉南京大学的平静生活/科研笔记/Llama-3/ruozhiba.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 从1开始计数的值
count = 1

# 替换JSON中的值
def replace_one(obj):
    global count
    if isinstance(obj, dict):
        for key, value in obj.items():
            if value == 1:
                obj[key] = count
                count += 1
            else:
                replace_one(value)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            if obj[i] == 1:
                obj[i] = count
                count += 1
            else:
                replace_one(obj[i])

# 调用函数替换值
replace_one(data)

# 将修改后的数据写回文件，并保留原始中文
with open('D:/萧珉南京大学的平静生活/科研笔记/Llama-3/ruozhiba.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

