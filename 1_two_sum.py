class Solution(object):
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            for j in range(i+1, len(nums)):
                b = nums[j]
                if i != j and a+b == target:
                    return [i, j]

sln = Solution()
nums = input("Enter your data\n")
nums = [int(x) for x in nums.split()]
target = input("Enter your target\n")
target = int(target)
print(sln.twoSum(nums, target))
