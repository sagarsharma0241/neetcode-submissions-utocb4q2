class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)

        for elem in strs:
            count = [0] * 26
            for char in elem:
                count[ord(char) - ord("a")] +=1
            output_dict[tuple(count)].append(elem)
        print(output_dict)
        output_list = list(output_dict.values())
        return output_list