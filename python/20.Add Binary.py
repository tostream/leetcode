class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result =[]
        remind = 0
        len_a = len(a)
        len_b = len(b)
        loop_count = max(len(a),len(b))
        for i in range(loop_count):
            index = (i+1)*-1
            a_temp = int(a[index]) if len_a > i else 0
            b_temp = int(b[index]) if len_b > i else 0
            temp_res = a_temp + b_temp + remind
            result.append(str(temp_res%2))
            remind=temp_res//2
        if remind == 1 : result.append('1')
        return ''.join(reversed(result))


#time o(n)
#space o(n)