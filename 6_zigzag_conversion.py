class Solution(object):
    def convert(self, s, numRows):
        strs = [[] for i in range(numRows)]
        if numRows == 1:
            return s
        for i, ch in enumerate(s):
            if i % (2*numRows-2) in range(numRows):
                strs[i % (2*numRows-2)] += ch
            else:
                strs[2*numRows-2-i % (2*numRows-2)] += ch
        # print(strs)
        combine_str = "".join(["".join(ss) for ss in strs])
        return str(combine_str)

s = input("Enter the string\n")
numRows = input("Enter the row number\n")
sln = Solution()
s_zigzag = sln.convert(s, int(numRows))
print(s_zigzag)
