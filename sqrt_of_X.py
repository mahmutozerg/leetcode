class Solution:
    def mySqrt(self, x: int) -> int:
        upper = x/2
        left = 1
        middle = upper/2
        res = middle*middle
        if x>0 and x<=4:
            return 1
        elif x == 0:
            return 0

        while True:
            if int(res) == x:
                break
            if res > x:
                upper = middle
                middle = middle/2
            elif res < x:
                left = middle
                middle = (left+upper)/2

            res = middle*middle





        return int(middle)


sol = Solution()
print(sol.mySqrt(0))