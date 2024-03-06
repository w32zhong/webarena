import torch

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
    inputs = tokenizer.encode(prompt, return_tensors='pt').cuda()
    while '<|endoftext|>' not in answer: #answer.count('\n') == 0:
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
    return answer
