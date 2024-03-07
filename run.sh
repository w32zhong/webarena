python scripts/generate_test_data.py
python agent/prompts/to_json.py
python run.py $@

#python run.py --instruction_path agent/prompts/jsons/p_cot_id_actree_2s.json --test_start_idx 0 --test_end_idx 1 --result_dir output/ --model Qwen/Qwen1.5-1.8B-Chat --tokenizer Qwen/Qwen1.5-1.8B-Chat --provider huggingface_generator
#python run.py --instruction_path agent/prompts/jsons/p_cot_id_actree_2s.json --test_start_idx 0 --test_end_idx 1 --result_dir output/ --model Qwen/Qwen1.5-7B-Chat --tokenizer Qwen/Qwen1.5-7B-Chat --provider huggingface_generator

#python run.py --instruction_path agent/prompts/jsons/p_cot_id_actree_2s.json --test_start_idx 0 --test_end_idx 1 --result_dir output/ --model Zyphra/BlackMamba-2.8B --tokenizer EleutherAI/gpt-neox-20b

#python run.py --instruction_path agent/prompts/jsons/p_cot_id_actree_2s.json --test_start_idx 0 --test_end_idx 1 --result_dir output/ --model havenhq/mamba-chat --tokenizer havenhq/mamba-chat

#python run.py --instruction_path agent/prompts/jsons/p_cot_id_actree_2s.json --test_start_idx 0 --test_end_idx 1 --result_dir output/ --model xiuyul/mamba-2.8b-zephyr --tokenizer xiuyul/mamba-2.8b-zephyr

#python run.py --instruction_path agent/prompts/jsons/p_cot_id_actree_2s.json --test_start_idx 0 --test_end_idx 1 --result_dir output/ --model BlinkDL/rwkv-5-world --tokenizer BlinkDL/rwkv-5-world
