import torch
from transformers import TextStreamer

def generate_from_huggingface_completion(
    agent,
    prompt: str,
    tokenizer,
    model_endpoint: str,
    temperature: float,
    top_p: float,
    max_new_tokens: int,
    stop_sequences: list[str] | None = None,
) -> str:
    answer = ''
    tokenizer = tokenizer.tokenizer
    model = agent.hgf_model
    model.eval()
    print('~' * 60)
    print(prompt)
    print('=' * 60)
    inputs = tokenizer.encode(prompt, return_tensors='pt').cuda()
    all_tokens = prompt_tokens = inputs.shape[-1]
    while ('<|endoftext|>' not in answer and
        '<|im_end|>' not in answer and
        all_tokens - prompt_tokens < max_new_tokens):
        if hasattr(model, 'embedding'):
            model.embedding = model.embedding.to(inputs.device)
        with torch.no_grad():
            out_logits = model(inputs)
        if isinstance(out_logits, torch.Tensor):
            last_logits = out_logits[:, -1]
        else:
            last_logits = out_logits.logits[:, -1]
        pred_vocab = last_logits.argmax(dim=-1)
        out_token = tokenizer.decode(pred_vocab)
        print(out_token, end='', flush=True)
        answer += out_token
        inputs = torch.concat((inputs, pred_vocab.unsqueeze(0)), -1)
        all_tokens = inputs.shape[-1]
    return answer


def generate_from_huggingface(
    agent,
    prompt: str,
    tokenizer,
    model_endpoint: str,
    temperature: float,
    top_p: float,
    max_new_tokens: int,
    stop_sequences: list[str] | None = None,
) -> str:
    answer = ''
    tokenizer = tokenizer.tokenizer
    inputs = tokenizer.encode(prompt, return_tensors='pt').cuda()
    prompt_tokens = inputs.shape[-1]
    model = agent.hgf_model
    gen_config = agent.hgf_gen_config
    gen_config.update(
        max_new_tokens=max_new_tokens
    )
    print(gen_config)
    print('~' * 60)
    print(prompt)
    print('=' * 60)
    model.eval()
    inputs = tokenizer(prompt, return_tensors='pt')
    streamer = TextStreamer(tokenizer)
    res_tokens = model.generate(**inputs.to('cuda'),
        generation_config=gen_config,
        streamer=streamer
    )
    out_tokens = res_tokens[0][prompt_tokens:]
    out_text = tokenizer.decode(out_tokens)
    return out_text
