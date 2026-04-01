from pathlib import Path
from random import choice

lines = Path(__file__).with_name("prompts.txt").read_text(encoding="utf-8").splitlines()
print(choice(lines))
