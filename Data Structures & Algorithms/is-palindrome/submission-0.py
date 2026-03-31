class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join(c for c in s if c.isalnum() == True).lower()
        pointer1 = 0
        pointer2 = len(clean_str) - 1
        for i in range(len(clean_str)):
            if pointer1 != pointer2:
                if clean_str[pointer1] != clean_str[pointer2]:
                    return False
                pointer1 += 1
                pointer2 -= 1
        return True
        