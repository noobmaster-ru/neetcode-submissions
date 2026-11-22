class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch for ch in s if ch.isalnum()).lower()
        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[len(cleaned)-1-i]:
                return False
        return True
