class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        while left <= right and right < len(s):
            if len(set(s[left:right+1])) < len(s[left:right+1]):
                left+=1
            else:
                result = max(result,len(s[left:right+1]))
                right+=1

        return result