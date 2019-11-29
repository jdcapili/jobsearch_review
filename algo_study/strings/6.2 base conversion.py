import string
def baseConversion(s, b1, b2):
    bases = { "0":0, "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9, 
    "A":10, "B":11, "C":12, "D":13, "E":14, "F":15,  }

    # "10" -> 1 x 10**1 + 0 x 10**0
    # "1010" -> 1 x 2**3 + 0 x 2**2 + 1 x 2**1 + 0 x 2**0

    val = 0
    for i, char in enumerate(s[::-1]):
        print(val,char,i)
        val += bases[char] * (b1)**i
    # print(val)
    res,i = "",0
    if b2 == 1: 
        print("1" * val)
        return "1" * val
    else:
        while ((b2)**i) < val:
            i+=1
    
    
    print(i)
    for j in reversed(range(i)):
        print(val - (b2) ** j,j,val)
        fact = b2
        while (fact * (b2**j)) > val:
            fact -= 1

        if (val - (b2) ** j) >= 0:
            val -= fact * (b2) ** j
            res += string.hexdigits[fact % b2]
        else:
            res += string.hexdigits[fact % b2]

    print(val,i,res)

baseConversion("102",3,1)