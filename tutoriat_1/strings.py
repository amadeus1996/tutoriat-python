# 1. Reverse a String
def reverse_string(s):
    return s[::-1]

# 2. Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum([1 for char in s if char in vowels])

# 3. Check if a String is a Palindrome
def is_palindrome(s):
    s_cleaned = s.replace(" ", "").lower()
    return s_cleaned == s_cleaned[::-1]

# 4. Count Occurrences of a Substring
def count_substring(s, substring):
    return s.count(substring)

# 5. Remove Whitespace from a String
def remove_whitespace(s):
    s = s.strip()
    l = s.split()
    s = " ".join(l)
    return s

# 6. Convert a String to Uppercase
def to_uppercase(s):
    return s.upper()

# 7. Replace Characters in a String
def replace_characters(s, old, new):
    return s.replace(old, new)

# 8. Check if a String Contains Only Digits
def contains_only_digits(s):
    return s.isdigit()

# 9. First Non-Repeated Character
def first_non_repeated(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# 10. Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 11. Anagram Check
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# 12. Find All Substrings
def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

# 13. Capitalize First Letter of Each Word
def capitalize_words(s):
    return s.title()

# 14. Compress a String
def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return ''.join(compressed)

# 15. Check if One String is a Rotation of Another
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

# 16. Check for Balanced Parentheses
def is_balanced(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")" and stack:
            stack.pop()
        elif char == ")":
            return False
    return len(stack) == 0

# 17. Remove Duplicates in a String
def remove_duplicates(s):
    result = []
    for char in s:
        if char not in result:
            result.append(char)
    return ''.join(result)

# 18. Find the Most Frequent Character
def most_frequent_character(s):
    return max(set(s), key=s.count)

# 19. Check if String is a Valid Shuffle of Two Strings
def is_valid_shuffle(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    i = j = k = 0
    while k < len(s3):
        if i < len(s1) and s1[i] == s3[k]:
            i += 1
        elif j < len(s2) and s2[j] == s3[k]:
            j += 1
        else:
            return False
        k += 1
    return i == len(s1) and j == len(s2)

# Main function to test all the problems
def main():
    print("1. Reverse String:", reverse_string("hello"))
    print("2. Count Vowels:", count_vowels("apple"))
    print("3. Is Palindrome:", is_palindrome("A man a plan a canal Panama"))
    print("4. Count Substring:", count_substring("hello world, hello", "hello"))
    print("5. Remove Whitespace:", remove_whitespace("   hello   "))
    print("6. To Uppercase:", to_uppercase("hello"))
    print("7. Replace Characters:", replace_characters("hello", "l", "x"))
    print("8. Contains Only Digits:", contains_only_digits("12345"))
    print("9. First Non-Repeated Character:", first_non_repeated("swiss"))
    print("10. Longest Word:", longest_word("The quick brown fox"))
    print("11. Are Anagrams:", are_anagrams("listen", "silent"))
    print("12. All Substrings:", all_substrings("abc"))
    print("13. Capitalize Words:", capitalize_words("hello world"))
    print("14. Compress String:", compress_string("aaabbbcc"))
    print("15. Is Rotation:", is_rotation("abcd", "dabc"))
    print("16. Is Balanced:", is_balanced("(()())"))
    print("17. Remove Duplicates:", remove_duplicates("programming"))
    print("18. Most Frequent Character:", most_frequent_character("bananas"))
    print("19. Is Valid Shuffle:", is_valid_shuffle("abc", "def", "adbcef"))

if __name__ == "__main__":
    main()
