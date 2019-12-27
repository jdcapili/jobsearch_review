class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0: return True
        tab = [True] + [False]*len(s)
        
        for i in range(len(s)): 
            for word in wordDict:
                word_len = len(word)
                if s[i: i+word_len] == word and tab[i]:
                    tab[i+word_len] = True
                    
        return tab[-1]