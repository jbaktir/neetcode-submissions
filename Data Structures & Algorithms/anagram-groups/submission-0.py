class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i not in strs_dict:
                strs_dict[sorted_i] = [i]
            else:
                strs_dict[sorted_i].append(i)
        return list(strs_dict.values())