class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        counter = 0
        if needle == "":
            return 0

        if needle in haystack:
            while needle != haystack[:len(needle)]:
                haystack = haystack[1:]
                counter+=1

            return counter



        return -1


sol = Solution()
print(sol.strStr( haystack = "hello", needle = "ll"))