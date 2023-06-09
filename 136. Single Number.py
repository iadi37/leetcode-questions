class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # d = {}

        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1

        # for k, v in d.items():
        #     if v == 1:
        #         return k

        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]

        return ans