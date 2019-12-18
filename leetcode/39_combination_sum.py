
def combinationSum(candidates, target):

    def helper(ints,subs,idx,target,res):
        if target < 0: return
        if target == 0: 
            res.append(subs)
            return
        for i in range(idx,len(ints)):
            helper(ints,subs + [ints[i]],i,target-ints[i],res)

    res = []
    candidates.sort()
    helper(candidates,[],0, target, res)
    return res
 




print(combinationSum([2,3,5],8))