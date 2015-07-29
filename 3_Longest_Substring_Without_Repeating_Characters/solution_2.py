class Solution:
    # @param {string} s
    # @return {integer}
    # use sliding window to record the start and end 
    # of substring
    # traverse s
    # for ch in s
    #     if ch in the sliding window:
    #          increase the start until s[start] == ch
    #          decrease the current length
    #     add ch to the sliding window
    #     increase current length by 1
    #     update max_len if current length is bigger than max_len

    def lengthOfLongestSubstring(self, s):
        max_len, start, end, current_len = 0, 0, 0, 0
    	for ch in s:
    		index = s[start:end].find(ch)
    		if index != -1:
    			start = start + index + 1
    			current_len = end-start
    		end += 1
    		current_len = end - start
    		max_len = max(max_len, current_len)
    	return max_len