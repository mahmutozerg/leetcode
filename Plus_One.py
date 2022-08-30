class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry_index =-1
        if len(digits) == 1:
            if digits[0]+1 == 10:
                digits.insert(0,1)
                digits[1] = 0
            else:
                digits[0] = digits[0]+1


        else:
            digits[-1]+=1
            while digits[carry_index] >=10:
                try:
                    digits[carry_index-1] +=1
                    digits[carry_index] = 0
                    carry_index-=1

                except:
                    digits.insert(0,digits[1])

        return digits


sol = Solution()
print(sol.plusOne( [9,9]))