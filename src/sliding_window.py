from pathlib import Path
import tiktoken


file_path = Path("the-verdict.txt")
the_verdict_text = file_path.open(encoding="utf-8").read()

tokenizer = tiktoken.get_encoding("gpt2")
tokens = tokenizer.encode(the_verdict_text)
print(len(tokens))

enc_sample = tokens[50:]
print(len(enc_sample))

context_size = 4
x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]
print(f"x: {x}")
print(f"y:      {y}")

for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]
    print(f"{context} ----> {desired}")
