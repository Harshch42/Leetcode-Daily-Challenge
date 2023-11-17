class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # res = 0

        # for i in range(n // 2 + 1):
        #     res = max(res , nums[i] + nums[n - i - 1])

        # return res


        ###### TWO POINTER
        # nums.sort()
        # n = len(nums)
        # res = 0
        # i = 0
        # j = n - 1

        # while i <= j - 1:
        #     res = max(res, nums[i] + nums[j])

        #     i += 1
        #     j -= 1

        # return res