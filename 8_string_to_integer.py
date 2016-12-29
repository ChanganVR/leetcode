class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        positive = True
        if s.startswith('+'):
            s = s[1::]
        elif s.startswith('-'):
            s = s[1::]
            positive = not positive
        for i, ch in enumerate(s):
            if not ch.isdigit():
                s = s[:i]
                break
        if not s:
            return 0
        s = s[-1::-1]
        if not s.isdigit():
            return 0
        num = 0
        for i, x in enumerate(s):
            num += 10**(i) * int(x)
        if positive:
            if num > 2**31-1:
                num = 2**31-1
            return num
        else:
            if num > 2**31:
                num = 2**31
            return -num

s = input("Enter the string\n")
sln = Solution()
s = sln.myAtoi(s)
print(s)
