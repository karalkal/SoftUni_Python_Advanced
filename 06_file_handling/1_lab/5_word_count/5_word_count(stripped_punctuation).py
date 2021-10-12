import string

input_text = [
    "-I was quick to judge him, but it wasn't his fault.\n",
    "-Is this some kind of joke?! Is it?\n",
    "-Quick, hide here…It is safer.\n"
]
with open("text.txt", mode="w") as file:
    file.writelines(input_text)

# and then read its content and transform it to list
with open("text.txt", mode="r") as file:
    whole_text = file.read().lower()
    stripped_text = ""
    for ch in whole_text:
        if ch not in string.punctuation:
            stripped_text += ch
    text_words = stripped_text.split()
# print(text_words)

searched_words = input().split()
found_words = {}
for s_word in searched_words:
    word_count = text_words.count(s_word)
    found_words[s_word] = word_count
sorted_dict = dict(sorted(found_words.items(), key=lambda x: -x[1]))
# print(found_words)
# print(sorted_dict)
for k, v in sorted_dict.items():
    print(f"{k} - {v}")