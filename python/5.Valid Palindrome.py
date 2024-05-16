class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = s.lower().replace(' ','')
        res = re.sub('\W','',res) # \W mean metacharacter
        res = re.sub('_','',res) # metacharacter doesn't includ underscore
        return res == res[::-1]
