class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0
        i = 0
        while i < len(s):
            if (len(s))>1 and i+1< (len(s)):
                print(number)

                if s[i] == "I":
                    if s[i+1] == "V" or s[i+1] == "X":
                        number += roman_dict[s[i+1]]-roman_dict[s[i]]
                        i+=1
                    else:
                        number += roman_dict[s[i]]
                elif s[i] == "X":
                    if s[i+1] == "L" or s[i+1] == "C":
                        number += roman_dict[s[i+1]]-roman_dict[s[i]]
                        i+=1
                    else:
                        number += roman_dict[s[i]]
                elif s[i] == "C":
                    if s[i + 1] == "D" or s[i + 1] == "M":
                        number += roman_dict[s[i + 1]] - roman_dict[s[i]]
                        i += 1
                    else:
                        number += roman_dict[s[i]]

                else:
                    number += roman_dict[s[i]]
            else:
                number += roman_dict[s[i]]

            i+=1
        return number




sol = Solution()
print(sol.romanToInt("DCXXI"))
