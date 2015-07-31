class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        
        hay_len, needle_len = len(haystack), len(needle)
        
        # needle's length is bigger than hay's
        if hay_len < needle_len:
            return -1
        
        idx_h = 0
        while(idx_h <= hay_len - needle_len):
            idx_n = 0
            while(idx_n < needle_len):
                if haystack[idx_h + idx_n] == needle[idx_n]:
                    idx_n += 1
                else:
                    break
            if idx_n == needle_len:
                return idx_h
            else:
                idx_h += 1
                
        return -1