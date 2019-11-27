def interconvert(num):
    dict = {1:"1",2:"2",3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 0:"0",
    "1":1,"2":2,"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
    
    if type(num) == str:
        res = 0
        for i in range(len(num)):
            if num[i] != "-":
                res = (res *  10 + dict[num[i]])

        if num[0] == "-":
            return res * -1
    else:
        print('hey')
        n = num if num >= 0 else num * -1
        print(n)
        res = ""
        while n:
            print(n)
            res = dict[n % 10] + res
            print(res)
            n = n // 10

        return "-" + res if num < 0 else res



print(interconvert(123))