import transformers
import torch
torch.cuda.set_device(1)

model_id = "/home/minpengfei/Llama-3/myllama"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",
)

messages = [
    {"role": "system", "content": "在接下来的回答中，你的角色是被闵天帝刚刚调试好的中文大语言模型Llama-3，请尽量用中文回答"},
    {"role": "user", "content": "我同时吸入氧气和氢气是不是就等于我在喝水了"},
]

prompt = pipeline.tokenizer.apply_chat_template(
		messages,
		tokenize=False,
		add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs[0]["generated_text"][len(prompt):])