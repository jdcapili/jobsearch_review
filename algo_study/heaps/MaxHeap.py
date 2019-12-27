class Maxheap:
    def __init__(self):
        self.arr = [None]
    
    def deleteMax(self):
        len_arr = len(self.arr)
        if len_arr == 1: return
        if len_arr == 2:
            return self.arr.pop()
        
        max_val = self.arr[1]
        self.arr[1] = self.arr.pop()
        self.siftdown(1)
        return max_val

    def siftdown(idx):
        c_val = self.arr[idx]
        len_arr = len(self.arr)
        left_idx = idx * 2
        right_idx = (idx * 2) + 1
        right_v = self.arr[right_idx]
        if left_idx >= len_arr:
            left_v = -float("inf")
        else:
            left_v = self.arr[left_idx]

        if right_idx >= len_arr:
            right_v = -float("inf")
        else:
            right_v = self.arr[right_idx]

        if left_v < c_val and right_v < c_val: return

        swap_idx = idx

        if left_v > right_v:
            swap_idx = left_idx
        else:
            swap_idx = right_idx

        self.arr[idx], self.arr[swap_idx] = self.arr[swap_idx], self.arr[idx]
        self.siftdown(swap_idx)