from datasets import Dataset, load_dataset, load_from_disk

dataset = load_dataset("ceval/ceval-exam", "logic")
dataset.save_to_disk("D:\萧珉南京大学的平静生活\科研笔记\Llama-3\ceval")  # 保存到该目录下

