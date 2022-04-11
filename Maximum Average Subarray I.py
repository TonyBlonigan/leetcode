class Solution:
    def findMaxAverage(self, nums,k):
        # O(n)
        max_window_sum = -float('inf')

        for i in range(len(nums) - k + 1):
            if i == 0:
                window_sum = sum(nums[i:i + k])
            else:
                window_sum -= nums[i - 1]
                window_sum += nums[i + k -1]

            if window_sum > max_window_sum:
                max_window_sum = window_sum

        return max_window_sum / k


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4))