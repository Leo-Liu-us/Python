# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 13:44:18 2015

@author: Leo
Code test from Continuum Analytics
find all anagrams of a given word from a specified file
"""

from itertools import permutations
import unittest


def generate_all_permutations( word ):
    '''
    generate all possible permutations of word
    input:  word of string
    output: set of word which is a rearrangement of word
    '''
    perm_set = set([])
    
    perm_list = list( permutations( word ) )
    
    for item in perm_list:
        perm_set.add("".join( item ))
        
    return perm_set
        

def find_anagrams(path, original_word):
    '''
    find all anagrams of original_word from a file specified by path
    input:      path: path of file
    input:      original_word:  source word
    output:     list of anagrams
    '''
    if not original_word:
        return
 
    perm_set = generate_all_permutations(original_word)
    
    with open(path, 'r') as f:
        results = [ word.strip("\n") for word in f \
                    if word.strip("\n") in perm_set]
        
    return results
    
#------------------------------------------------------------------------------    
#------------------------------unit test---------------------------------------
#------------------------------------------------------------------------------
    
class GenerateAllPermutationTest( unittest.TestCase ):
    '''
    Unit test for function: generate_all_permutation
    '''
    def test_generate_all_permutations_empty( self ):
        '''
        test empty input
        '''
        word = ''
        result = set([])- generate_all_permutations(word)
        self.assertEqual( len(result), 0 )
        
    def test_generate_all_permutations_1char( self ):
        '''
        test input word with 1 character
        '''
        word = 'a'
        result = set(["a"])- generate_all_permutations(word)
        self.assertEqual( len(result), 0 )
        
    def test_generate_all_permutations_2char( self ):
        '''
        test input word with 2 char
        '''
        #different charcters
        word = 'ab'
        result = set(["ab","ba"])- generate_all_permutations(word)
        self.assertEqual( len(result),0 )
        
        #repeat charcters
        word = 'aa'
        result = set(["aa"])- generate_all_permutations(word)
        self.assertEqual( len(result),0 )
        
    def test_generate_all_permutations_3char( self ):
        '''
        test input word with 3 char
        '''
        #different charcters
        word = 'abc'
        result = set(["abc","acb","bac","bca","cab","cba"]) - \
                    generate_all_permutations(word)
        self.assertEqual(len(result),0)
        
        #repeat charcters
        word = 'aab'
        result = set(["aab","aba","baa"]) - generate_all_permutations(word)
        self.assertEqual( len(result), 0 )  
        
        #3 repeat chars
        word = 'aaa'
        result = set(["aaa"]) - generate_all_permutations(word)
        self.assertEqual( len(result), 0 ) 
        
class FindAnagramsTest( unittest.TestCase ):
    '''
    Unit test for function: find_anagram
    '''
    def test_find_anagrams_empty( self ):
        '''
        test for empty input
        '''
        
        #empty file path
        path = ''
        word = 'empires'
        self.assertRaises( IOError, find_anagrams, path, word)
        
        #path does not exist
        path = 'random/path/word.txt'
        word = 'empires'
        self.assertRaises( IOError, find_anagrams, path, word)
        
        #empty input word
        path = './words.txt'
        word = ''
        result = find_anagrams( path, word )
        self.assertEqual( result, None )
    
    def test_find_anagrams_success( self ):
        '''
        testing for sucess
        '''
        #constructe testing data
        with open('./test_words.txt',"w") as f:
            f.write("abc\n")
            f.write("acb\n")
            f.write("bac\n")
            f.write("bca\n")
            f.write("cab\n")
            f.write("cba\n")
            
            f.write("aaa\n")
            f.write("abcd\n")
            
        #do the testing
        path = './test_words.txt'
        word = 'abc'
        result = find_anagrams(path, word)
        
        self.assertEqual( len(result), 6)
        

        
if __name__ == "__main__":
    unittest.main()
        
    
