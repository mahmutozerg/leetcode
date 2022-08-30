class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]< target:
                pass
            else:
                nums.insert(i,target)
                return i

        return len(nums)


sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 7))