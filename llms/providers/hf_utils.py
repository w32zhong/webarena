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
    inputs = tokenizer.encode(prompt, return_tensors='pt').cuda()
    while answer.count('\n') == 0:
        breakpoint()
        out_logits = model(inputs)
        last_logits = out_logits[:, -1]
        pred_vocab = last_logits.argmax(dim=-1)
        out_token = tokenizer.decode(pred_vocab)
        print(out_token.replace('\n', '<NL>'), end='', flush=True)
        answer += out_token
        inputs = torch.concat((inputs, pred_vocab.unsqueeze(0)), -1)
    return answer
