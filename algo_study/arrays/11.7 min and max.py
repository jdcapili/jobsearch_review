def find_min_max(arr):
    smol = math.inf
    bigboi = -math.inf
    for n in A:
        smol = min(smol,n)
        bigboi = max(bigboi,n)

    return (smol,bigboi)