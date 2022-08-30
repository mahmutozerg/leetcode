class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        indices = []

        for i in range(len(nums)):
            if nums[i] == val:
                indices.append(nums[i])

        for i in indices:
            nums.remove(i)

        return len(nums)


