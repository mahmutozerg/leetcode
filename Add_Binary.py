
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = list()
        res_str = str()
        if len(a) < len(b):
            a,b=b,a

        for i in a:
            res.append(int(i))

        counter = len(res)-1

        for j in range(len(b)-1,-1,-1):
            res[counter] += int(b[j])
            counter-=1
        counter = len(res)-1

        while counter >=0:
            if res[counter] > 1:
                temp = res[counter]
                res[counter] = temp%2
                if counter-1 >=0:
                    res[counter-1] += temp //2
                else:
                    res.insert(0,temp//2)

            counter-=1
        for i in res:
            res_str+=str(i)

        return res_str



sol = Solution()
print(sol.addBinary("1010","1011"))