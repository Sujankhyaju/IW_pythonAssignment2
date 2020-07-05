# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed

def is_palindrome(word):
    if word == word[::-1]:
        return "Palindrome"

    else:
        return "Not Palindrome"

word =input("Enter a word::")
print(is_palindrome(word))
