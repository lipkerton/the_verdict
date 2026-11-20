import re
from pathlib import Path


file_path = Path("the-verdict.txt")
text = file_path.open(mode="r", encoding="utf-8").read()
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))

vocab = {token:integer for token,integer in enumerate(preprocessed)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break