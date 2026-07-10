class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0]  * len(nums)
        ans = [0] * len(nums)
        # print(suffix)
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums) - 2, 0, -1):
            suffix[i] = suffix[i+1] * nums[i]
        print(prefix)
        print(suffix)
        for i in range(len(nums)):
            if i == 0:
                ans[i] = suffix[i+1]
            elif i == (len(nums) - 1):
                ans[i] = prefix[i-1]
            else:
                ans[i] = prefix[i-1] * suffix[i+1]
        return ans

        