class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = s
        mod = True
        
        while mod:
            
            new_res = ""
            subs = ""

            for char in res:
                if len(subs) == k:
                    subs = char
                    mod = True
                elif not subs or subs[-1] == char:
                    subs += char
                else:
                    new_res += subs
                    subs = char
                    
            if len(subs) == k:
                subs = ""
            res = new_res + subs
        return res
                