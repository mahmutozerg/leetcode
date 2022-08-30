class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter1, counter2 = 0,-1
        while s.endswith(" "):
            s = s[:len(s)-1]
        if len(s) == 1:
            return 1

        while True:
            try:
                if s[counter2] !=" ":
                    counter1+=1
                    counter2-=1
                else:
                    return counter1
            except:
                return counter1


sol = Solution()
print(sol.lengthOfLastWord("day"))



