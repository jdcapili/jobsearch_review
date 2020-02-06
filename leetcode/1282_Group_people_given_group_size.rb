# @param {Integer[]} group_sizes
# @return {Integer[][]}
def group_the_people(group_sizes)
    groups = Hash.new {|h,k| h[k] = []}
    res = []
    
    group_sizes.each_with_index do |group_size,idx|
        if groups.has_key?(group_size) && groups[group_size].length == group_size
            res << groups[group_size]
            groups[group_size] = []
        end
        groups[group_size] << idx
    end
    
    groups.each_value do |v|
       res << v if v.length > 0
    end
    
    return res
end