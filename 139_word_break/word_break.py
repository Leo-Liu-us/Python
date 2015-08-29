class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        #use dynamic programming to solve it
        #state transission:
        #dp[i] = dp[j] and (s[j, i] in wordDict), 0 <= j < i
        
        s_len = len(s)
        dp = [ False for _ in range(s_len + 1)]
        dp[0] = True
        
        for i in range(1, s_len + 1):
            for j in range(0, i):
                dp[i] = dp[j] and (s[j:i] in wordDict)
                if dp[i]:
                    break
                
        return dp[s_len]