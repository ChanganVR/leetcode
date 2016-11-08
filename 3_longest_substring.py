#!/usr/bin/python3

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = dict() 
        for i, ch in enumerate(s):
            if ch in dic:
                dic[ch].append(i)
            else:
                dic[ch] = [i]
        print(dic)
        min_dist = list()
        for i, ch in enumerate(s):
            index_list = dic[ch]
            min_index = 10000
            for index in index_list:
                if index > i and index < min_index:
                    min_index = index
            if min_index == 10000:
                min_dist.append(len(s) - 1 - i)
            else:
                min_dist.append(min_index - i)
        print(min_dist)
        max_dist = 0
        max_index = 0
        for i, dist in enumerate(min_dist):
            if dist > max_dist:
                max_dist = dist
                max_index = i
        substr = s[max_index:max_index + max_dist]
        print(substr)

print("Enter the string you want to test")
str = input()
sln = Solution()
sln.lengthOfLongestSubstring(str)
