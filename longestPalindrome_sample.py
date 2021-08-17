"""This code sample is one of many solutions to leetcode problem #5
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution(object):
    def __init__(self):
        pass

    def longestPalindrome(self, input_str):
        """Method that finds the longest palindrome sub string within a given input string
        Args:
            input_str (str) - string that only contains digits and/or english letters
        Returns:
            max_result (str) - longest palindrome substring within input_str
        """
        max_len = 0
        max_result = ""
        for str_ind in range(len(input_str)):
            # for odd palindromes
            left, right = str_ind, str_ind
            while left >= 0 and right < len(input_str) and input_str[left] == input_str[right]:
                if (right - left + 1) > max_len:
                    max_result = input_str[left:right + 1]
                    max_len = right - left + 1
                left -= 1
                right += 1
            # for even palindromes
            left, right = str_ind, str_ind + 1
            while left >= 0 and right < len(input_str) and input_str[left] == input_str[right]:
                if (right - left + 1) > max_len:
                    max_result = input_str[left:right + 1]
                    max_len = right - left + 1
                left -= 1
                right += 1
        return max_result


"""sample run"""

sample_str = 'ziooiz'
out = Solution()
result = out.longestPalindrome(sample_str)
print(result)
