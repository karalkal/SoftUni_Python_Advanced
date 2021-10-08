def palindrome(word, not_needed):
    for i in range(len(word) // 2):  # if odd len, middle char is disregarded
        if word[i] != word[len(word) - 1 - i]:
            return f"{word} is not a palindrome"
    return f"{word} is a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
