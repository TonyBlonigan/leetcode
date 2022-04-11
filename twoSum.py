class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        # FindCatchedComplimentIndex
        n_to_i_cache = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in n_to_i_cache:
                return [i, n_to_i_cache[compliment]]
            else:
                n_to_i_cache[nums[i]] = i

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        # O(n**2)
        len_nums = len(nums)
        for i in range(0, len_nums - 1):
            for j in range(i + 1, len_nums):

                sum_i_j = nums[i] + nums[j]

                if sum_i_j == target:
                    return [i, j]
