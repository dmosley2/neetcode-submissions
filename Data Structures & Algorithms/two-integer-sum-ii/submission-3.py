class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1,2]
        l = 0
        r = len(numbers) - 1
        sum = numbers[l] + numbers[r]
        while(sum != target):
            if(sum > target):
                r -= 1
            else:
                l += 1
            sum = numbers[l] + numbers[r]
        ans = [l+1,r+1]
        return ans
        
