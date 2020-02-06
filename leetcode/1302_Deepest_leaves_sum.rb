# @param {TreeNode} root
# @return {Integer}

# time complexity = O(mxn) where m is number of levels and n is number of nodes in a level
# space complexity = O(mxn) same as time?
def deepest_leaves_sum(root)
    sum = 0
    stack = [root]
    while stack.length > 0 do
        next_level=[]
        level_sum = 0
        stack.each do |node|
            next_level << node.left if node.left
            next_level << node.right if node.right
            level_sum += node.val
        end
        sum = level_sum
        stack = next_level
    end
    
    return sum
end