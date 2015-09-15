class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #reference http://articles.leetcode.com/2010/11/finding-minimum-window-in-s-which.html
        s_len, t_len = len(s), len(t)
        #sliding window
        start= 0
        #count variable to see how many ch from s[start:end+1] in t
        count = 0
        #init the min window length
        min_window_len = sys.maxint
        
        #dict to store the occurence of each ch in t.
        needToFind = {}
        #dict to store the occurence of each ch in sliding window
        hasFound = {}
        
        #init needToFind dict
        for ch in t:
            needToFind[ch] = needToFind.get(ch, 0) + 1
          
        '''  
        Each time we advance the end pointer (pointing to an element x),
        we increment hasFound[x] by one. 
        '''
        for end in range(s_len):
            if s[end] not in needToFind:
                continue
            
            hasFound[s[end]] = hasFound.get(s[end], 0) + 1
            #increment count by one if hasFound[ch] is less than or equal to needToFind[ch]
            if (hasFound[s[end]] <= needToFind[s[end]]):
                count += 1
            #When the constraint is met (that is, count equals to T¡®s size)
            if count == t_len:
                #immediately shrink the tailing (start) AS FAR RIGHT AS POSSIBLE while maintaining the constraint.
                #case1: s[start] not in needToFind
                #case2: hasFound[s[start]] is greater than needToFind[s[start]]
                while( needToFind.get(s[start], 0) == 0 or hasFound[s[start]] > needToFind[s[start]]):
                    #case 2:
                    if not (needToFind.get(s[start], 0) == 0):
                        hasFound[s[start]] -= 1
                        
                    start += 1
                
                '''
                check if hasFound[x] is greater than needToFind[x].
                If it is, we can decrement hasFound[x] by one and advancing begin pointer without breaking the constraint. 
                On the other hand, if it is not, we stop immediately as advancing begin pointer breaks the window constraint.
                '''
                if end-start+1 < min_window_len:
                    min_start = start
                    min_end = end
                    min_window_len = end-start+1
                    
        if min_window_len == sys.maxint:
            return ""
        else:
            return s[min_start:min_end+1]