class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        filtered = "".join(char.lower() for char in s if char.isalnum())
        return filtered == filtered[::-1]
        