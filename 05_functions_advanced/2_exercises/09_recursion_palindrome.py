def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[len(word) - 1 - index]:  # if odd len, middle char is disregarded
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("abccccba", 0))
print(palindrome("abba", 0))
print(palindrome("peter", 0))

