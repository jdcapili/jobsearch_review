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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictSet = set(wordDict)
        
        def check(st,dictSet, memo={}):
            if st in memo: return memo[st]
            if not st: return True
            curr = ""
            for idx,char in enumerate(st):
                curr += char
                if curr in dictSet and check(st[idx+1::],dictSet):
                    memo[curr] = True
                    return memo[curr]

                  
            memo[st] = False
            return memo[st]
        
        return check(s,dictSet)
        