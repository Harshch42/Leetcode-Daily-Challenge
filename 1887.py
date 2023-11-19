class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        res = 0
        temp = -1
        count = -1
        
        for i in range(len(nums)):
            if temp != nums[i]:
                temp = nums[i]
                count += 1

            res += count

        return res
