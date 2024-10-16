class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)-1,0,-1):
            if target - nums[index] in nums and index != nums.index(target-nums[index]):
                return [nums.index(target-nums[index]),index]
            else:
                continue
