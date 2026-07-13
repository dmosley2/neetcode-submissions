class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = len(s) - 1
        p2 = 0
        s = s.lower()
        if len(s) == 1:
            return True
        while p1 > p2:
            while not s[p1].isalnum():
                if p1 <= p2:
                    break
                p1 -= 1
            while not s[p2].isalnum():
                if p2 >= p1:
                    break
                p2 += 1
            if s[p1] != s[p2]:
                return False
            p1 -= 1
            p2 += 1
        return True
