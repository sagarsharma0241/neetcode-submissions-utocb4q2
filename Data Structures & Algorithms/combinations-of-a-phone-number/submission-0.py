class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashMap = {"2":"abc",
                    "3": "def",
                    "4": "ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        def backTrack(i, combo):
            if len(combo) == len(digits):
                res.append(combo)
                return

            for c in hashMap.get(digits[i]):
                backTrack(i + 1, combo + c)

        if digits:
            backTrack(0, "")
        return res       