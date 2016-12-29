class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if "" in strs:
            return ""
        common = ""
        for i, x in enumerate(strs[0]):
            if i == len(strs[1]) or x != strs[1][i]:
                break
            common = strs[0][:i+1]
        for s in strs[2:]:
            if common == "":
                return ""
            for i, ch in enumerate(s):
                if i == len(common) or ch != common[i]:
                    common = s[:i]
                    break
                if i+1 == len(s):
                    common = s
        return common

strs = []
num = input("Enter string number\n")
for i in range(int(num)):
    s = input("Enter a string\n")
    strs.append(s)
sln = Solution()
common = sln.longestCommonPrefix(strs)
print(common)
