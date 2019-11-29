import string
def baseConversion(s, b1, b2):
    bases = { "0":0, "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9, 
    "A":10, "B":11, "C":12, "D":13, "E":14, "F":15,  }

    # "10" -> 1 x 10**1 + 0 x 10**0
    # "1010" -> 1 x 2**3 + 0 x 2**2 + 1 x 2**1 + 0 x 2**0

    val = 0
    for i, char in enumerate(s[::-1]):
        print(char,i)
        val += bases[char] * (b1+1)**i

    res,i = "",0
    
    while ((b2+1)**i) < val:
        i+=1
    
    
    print(i)
    for j in reversed(range(i)):
        print(val - (b2+1) ** j,j)
        if (val - (b2+1) ** j) >= 0:
            res += string.hexdigits[b2]
            val -= (b2+1) ** j
        else:
            res += string.hexdigits[0]

    print(res)

baseConversion("100",9,1)