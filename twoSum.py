class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(nums)-1
        while 1:

            if temp[i]+temp[j] == target:

                if temp[i] == temp[j]:
                    return [nums.index(temp[i]),nums.index(temp[j],i+1)]
                else:
                    return [nums.index(temp[i]),nums.index(temp[j])]
            elif temp[i]+temp[j] > target:
                j -=1
            elif temp[i]+temp[j]<target:
                i+=1