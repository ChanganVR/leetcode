class Solution(object):
    def isPalindrome(self, x):
        palindrome = True
        s = str(x)
        for i, ch in enumerate(s):
            if ch != s[len(s)-i-1]:
                palindrome = False
        return palindrome

x = input('Enter a number\n')
sln = Solution()
print(sln.isPalindrome(int(x)))
