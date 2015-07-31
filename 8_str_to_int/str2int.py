class Solution:
    MAX_INT = 2147483647;
    MIN_INT = -2147483648;

    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.strip(' ')
        if len(str) == 0:
            return 0
            
        first = str[0]
        if first == '+':
            signal = 1
            str = str[1:]
        elif first == '-':
            signal = -1
            str = str[1:]
        else:
            signal = 1
            str = str
         
        print str
        res = 0
        for ch in str:
            if ch.isdigit():
                res *= 10
                res += (ord(ch)-ord('0'))
            else:
                if res * signal > self.MAX_INT:
                    return self.MAX_INT
                elif res * signal < self.MIN_INT:
                    return self.MIN_INT
                else:
                    return res * signal
        
        if res * signal > self.MAX_INT:
            return self.MAX_INT
        elif res * signal < self.MIN_INT:
            return self.MIN_INT
        else:
            return res * signal