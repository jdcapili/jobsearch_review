def sumOfSubmatrices(mat):
    res = []
    for i in range(len(mat)):
        cur_row_sum = 0
        outrow = []
        cur_row = mat[i]
        for j in range(len(cur_row)):
            cur_row_sum += cur_row[j]
            row_ele = cur_row_sum + res[i-1][j] if i != 0 else cur_row_sum
            outrow.append(row_ele)
        res.append(outrow)
    
    return res

print (sumOfSubmatrices([[1,2],[3,4]]))