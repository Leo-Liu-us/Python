class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        val = {'M':1000, 'D':500, 'C':100,\
                        'L':50, 'X':10, 'V':5, 'I':1,}
        res = 0
        len_s = len(s)
        idx = 0
        
        #traverse s
        for idx in range(0, len_s-1):
            curr_ch, next_ch = s[idx], s[idx + 1]
            
            if (val[curr_ch] < val[next_ch]):
                res -= val[curr_ch]
            else:
                res += val[curr_ch]
            idx += 1
        #add the last digit
        res += val[s[-1]]

        return res