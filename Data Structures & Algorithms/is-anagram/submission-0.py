class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = dict()
        countT = dict()
        if (len(s) != len(t)):
            return False
        for char in s:
            countS[char] = countS.get(char, 0) + 1
        countS = sorted(countS.items())
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        countT = sorted(countT.items())
        for i in range(len(countS)):
            popS = countS.pop()
            popT = countT.pop()
            if(popS[0] != popT[0]) or (popS[1] != popT[1]):
                return False
        return True
