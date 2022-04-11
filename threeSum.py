class Solution:
    def threeSum(self, nums):
        # O(n**2)
        # naive loop through list
        output = []

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        candidate = [nums[i], nums[j], nums[k]]

                        candidate.sort()

                        if candidate not in output:
                            output.append(candidate)

        return output


if __name__ == '__main__':
    s = Solution()

    print(s.threeSum(nums=[3, -2, 1, 0]))

    # sliding window

"""
# Two pointers
a pointer at each end of list 
"""

