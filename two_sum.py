class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        #n^2 solutions

        # for i in range(len(nums)- 1):
        #     for j in range(i+1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]


        #{1:2, 3:4}
        # a = {1:2, 3:4}. [1, 3]
        # a[1] = 2
        # a[3] = 4

        nums = [2,7,11,15]

        hash_map = {}.  # {2: 0}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in hash_map:
                return [hash_map[comp], i]
            hash_map[nums[i]] = i


