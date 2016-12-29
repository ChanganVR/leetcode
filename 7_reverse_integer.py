class Solution(object):
    def reverse(self, x):
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(-x)[::-1])
        if x < -2**31 or x > 2**31-1:
            x = 0
        return x

x = input("Enter an integer\n")
x = int(x)
sln = Solution()
x = sln.reverse(x)
print(x)
