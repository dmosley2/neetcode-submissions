class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        set_nums = set()
        for i in range(len(nums)):
            if nums[i] not in set_nums:
                set_nums.add(nums[i])
        for i in range(len(nums)):
            curLen = 0
            num = nums[i]
            if (num-1) not in set_nums:
                curLen+=1
                while (num+1) in set_nums:
                    curLen+=1
                    num+=1
            if curLen > ans:
                ans = curLen
        return ans
        