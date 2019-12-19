class Solution:
    def maxNumberOfBalloons(self, text):
        ball = {}
        for char in "balloon":
            if char not in ball: ball[char] = 0
                
        for char in text:
            if char in ball: ball[char] += 1
        print(ball)
        count = None
        for key in ball:
            
            if key is "l" or key is "o":
                if count is None: count = ball[key] // 2
                elif ball[key] // 2 <= count: count = ball[key] // 2
            else:
                if count is None: count = ball[key]
                elif ball[key] <= count: count = ball[key]
            print(key, ball[key],count)
                
        return count

# alternate solution

class Solution:
    def maxNumberOfBalloons(self, text):
        ball = {}
        for char in "balloon":
            if char not in ball: ball[char] = 0
                
        for char in text:
            if char in ball: ball[char] += 1
        
        return min(ball['b'], ball['a'], ball['l'] // 2, ball['o'] // 2, ball['n'])


# alt 2

class Solution:
    def maxNumberOfBalloons(self, text):
        dicti = {}
        for i in range(len(text)):
            if text[i] in "balloon":
                if text[i] not in dicti: dicti[text[i]] = 0
                dicti[text[i]] += 1
        if len(dicti) != 5: return 0
        c = math.inf
        for k,value in dicti.items():
            if k == "l" or k == "o":
                c = min(c, value//2)
            else:
                c = min(c,value)
        
        return c

test = Solution()
print(test.maxNumberOfBalloons("balon"))