import re

input_text = [
    "-I was quick to judge him, but it wasn't his fault.\n",
    "-Is this some kind of joke?! Is it?\n",
    "-Quick, hide here…It is safer.\n"
]
with open("text.txt", mode="w") as file:
    file.writelines(input_text)

with open("text.txt", mode="r") as file:
    text = file.read().lower()

searched_words = input().split()
found_words = {}
for s_word in searched_words:
    word_count = len(re.findall(rf"(\b){s_word}(\b)", text))
    found_words[s_word] = word_count
sorted_dict = dict(sorted(found_words.items(), key=lambda x: -x[1]))
# print(found_words)
# print(sorted_dict)
for k, v in sorted_dict.items():
    print(f"{k} - {v}")
