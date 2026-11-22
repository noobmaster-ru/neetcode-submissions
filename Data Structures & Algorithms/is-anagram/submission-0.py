class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mask = [0]*26
        t_mask = [0]*26
        
        for letter in s:
            s_mask[ord(letter) - ord('a')] += 1

        for letter in t:
            t_mask[ord(letter) - ord('a')] += 1
        
        return s_mask == t_mask
            
