class Solution:
    def massage(self, nums):

        if len(nums) == 0:
            return 0
        elif len(nums) == 1 or len(nums) == 2:  # 终于找到问题所在了，elif len(nums) == 1 or 2将会一直执行，
            # 代码应为 elif len(nums) == 1 or len(nums) == 2
            return max(nums)
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        else:
            return max(nums[0] + self.massage(nums[2:]), nums[1] + self.massage(nums[3:]))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().massage(nums))
