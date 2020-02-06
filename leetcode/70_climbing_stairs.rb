# @param {Integer} n
# @return {Integer}

# used tabulation. I tried using combinations and time limit exceeded.
# time complexity = O(n)
# space complexity = O(1)
def climb_stairs(n)
    return n if n < 4
    tab = [0,1,2,3] + [0]*(n-3)
    (4..n).each do |idx|
        tab[idx] = tab[idx-1] + tab[idx-2] 
    end
    return tab[-1]
end