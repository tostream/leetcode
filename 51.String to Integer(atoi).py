class Solution:
    def myAtoi(self, s: str) -> int:
        checker = s.lstrip()
        neg = False
        if len(checker)<1: return 0
        if checker[0] == '-':
            neg=True
            checker = checker [1:]
        elif checker[0] == '+':
            checker = checker [1:]
        res =[]
        for i in checker:
            if i.isnumeric():
                res.append(i)
            else:
                break
        if len(res)<1: return 0
        result = int(''.join(res))
        if neg: 
            return (2**31)*-1 if result > 2**31 else  result*-1
        else:
            return (2**31)-1 if result > 2**31 -1 else  result
