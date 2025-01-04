--nproc_per_node specifies the number of GPUs to use, different models require different values
--ckpt_dir specifies the path to the checkpoint file and tokenizer
--param_size specifies the parameter size of the model
--ntrain specifies the number of few-shot demos
--few_shot whether to use few-shot learning
--cot specifies whether to use chain-of-thought
--subject specifies the subject to be tested
torchrun --nproc_per_node 2 /home/minpengfei/Llama-3/ceval/code/evaluator_series/eval_llama.py --ckpt_dir [/home/minpengfei/Llama-3/myllama] --param_size 8 --few_shot --ntrain 5 --subject [logic]



lm_eval --model_args pretrained=/home/minpengfei/Llama-3/myllama/ --tasks ceval-valid_logic  --device cuda:1




