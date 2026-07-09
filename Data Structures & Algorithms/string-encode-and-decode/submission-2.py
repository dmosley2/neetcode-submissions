class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            ans += str(len(string)) + '#'
            ans += string
        return ans
    def decode(self, s: str) -> List[str]:
        # print(str(len(s)) + " " + s)
        ans = []
        length = 0
        index = 0
        length, delim, string = s.partition('#')
        # print(length + " " + delim + " " + string)
        while length != "":
            s1 = ""
            index = 0
            # index += len(length) + len(delim)
            for i in range(int(length)):
                s1 += string[index]
                index += 1
            # print(index)
            ans.append(s1)
            length, delim, string = string[index:].partition('#')
            # print(length + " " + delim + " " + string)
            # print(ans)
        return ans
            




