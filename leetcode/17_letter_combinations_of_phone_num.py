Class Solution:
    def letterCombinations(self,digits):
        if len(digits) == 0: return []
        keypad = {"2": ["a","b","c"], "3": ["d","e","f"],"4": ["g","h","i"],"5": ["j","k","l"],"6": ["m","n","o"],
        "7": ["p","q","r","s"],"8": ["t","u","v"],"9": ["w","x","y","z"]}

        if digits in keypad: return keypad[digits]

        res = []

        comb = self.letterCombinations(digits[1:])
        for keyA in keypad[digits[0]]:
            res += [keyA+keyB for keyB in comb]

        return res