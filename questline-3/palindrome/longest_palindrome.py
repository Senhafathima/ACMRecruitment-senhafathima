# longest_palindrome.py

def longest_palindrome(s: str) -> str:
    """
    Finds the longest palindromic substring in a given string.

    :param s: Input string
    :return: Longest palindromic substring
    """
    if not s or len(s) == 0:
        return ""

    start, end = 0, 0

    def expand_from_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # length of palindrome

    for i in range(len(s)):
        len1 = expand_from_center(i, i)      # odd length palindrome
        len2 = expand_from_center(i, i + 1)  # even length palindrome
        max_len = max(len1, len2)

        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


# Example usage
if __name__ == "__main__":
    test_str = "babad"
    print("Input:", test_str)
    print("Longest Palindromic Substring:", longest_palindrome(test_str))
