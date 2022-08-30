class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = nums[0]
        indices = []
        for i in range(1,len(nums)):
            if temp == nums[i]:
                indices.append(nums[i])
            else:
                temp = nums[i]

        for i in indices:
            nums.remove(i)

        return len(nums)


sol  =Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))