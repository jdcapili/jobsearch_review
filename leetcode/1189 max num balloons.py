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


test = Solution()
print(test.maxNumberOfBalloons("balon"))