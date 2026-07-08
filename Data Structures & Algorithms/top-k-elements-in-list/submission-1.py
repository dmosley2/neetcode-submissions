class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array_of_lists = [[] for i in range(len(nums) + 1)]
        results = []
        #key is number, value is frequency
        hash_map = {}
        for num in nums:
            if not num in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        for key in hash_map.keys():
            val = hash_map.get(key)
            array_of_lists[val].append(key)
        for i in range(len(array_of_lists) - 1, 0, -1):
            for j in range(len(array_of_lists[i])):
                results.append(array_of_lists[i][j])
                if len(results) == k:
                    return results


        