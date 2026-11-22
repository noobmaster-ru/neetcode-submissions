class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = dict()
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in dct.keys():
                dct[sorted_str].append(string)
            else:
                dct[sorted_str] = [string]
        answer = [arr for arr in dct.values()]
        return answer