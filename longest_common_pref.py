class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        temp = strs[0]
        a = 2
        temp2 = ""
        while a:
            for j in strs:
                if temp not in j[0:len(temp)]:
                    temp = temp[:-1]

            if temp2 != temp:
                temp2 = temp
            else:
                break
        return temp2

sol = Solution()
print(sol.longestCommonPrefix(["c","acc","ccc"]))