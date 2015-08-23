class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        

class Trie(object):

    def __init__(self):
        self.trie = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.trie
        for letter in word:
            #If key is in the dictionary, return its value. 
            #If not, insert key with a value of default and return default.
            current = current.setdefault(letter,{})
        #put a marker for the end of a word
        current['end'] = 'end'
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.trie
        #for each letter in word
        #search whether it is in the current dict
        for letter in word:
            if letter not in current:
                return False
            else:
                current = current[letter]
        
        #check marker to see whether it is the prefix
        if 'end' in current.keys():
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.trie
        #for each letter in word
        #search whether it is in the current dict
        for letter in prefix:
            if letter not in current:
                return False
            else:
                current = current[letter]
                
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")