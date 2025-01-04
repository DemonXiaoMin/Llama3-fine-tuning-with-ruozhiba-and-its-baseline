from llama_cpp import Llama

model = Llama(
    "/home/minpengfei/Llama-3/Llama3-8B-Chinese-Chat-f16.gguf",
    verbose=False,
    n_gpu_layers=-1,
)

system_prompt = "You are Llama3-8B-Chinese-Chat, which is finetuned on Llama3-8B-Instruct with Chinese-English mixed data by the ORPO alignment algorithm. You, Llama3-8B-Chinese-Chat, is developed by Pengfei Min (闵鹏飞 in Chinese). You are a helpful assistant."

def generate_reponse(_model, _messages, _max_tokens=8192):
    _output = _model.create_chat_completion(
        _messages,
        stop=["<|eot_id|>", "<|end_of_text|>"],
        max_tokens=_max_tokens,
    )["choices"][0]["message"]["content"]
    return _output

# The following are some examples

messages = [
    {"role": "system", "content": system_prompt, },
    {"role": "user", "content": "解释一下具身智能"},
]


print(generate_reponse(_model=model, _messages=messages), end="\n\n\n")

