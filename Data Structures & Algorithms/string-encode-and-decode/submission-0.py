class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for elem in strs:
            output = output + str(len(elem)) +"#" + elem
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        # print("---"+s)
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = s[i:j]
            elem = s[j+1: j+1+ int(length)]
            # print("---i->"+str(i))
            # print("---j-->"+str(j))
            # print("---"+elem)
            res.append(elem)
            i = j + 1 + int(length)
        return res
