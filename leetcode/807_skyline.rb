# @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
    row = Array.new(grid.length,0)
    col = Array.new(grid[0].length,0)
    
    for i in 0...grid.length do
       for j in 0...grid[0].length do
          row[i] = [row[i],grid[i][j]].max()
          col[j] = [col[j],grid[i][j]].max()
       end
    end
    
    res = 0
    for i in 0...grid.length do
       for j in 0...grid[0].length do
          res += [row[i],col[j]].min() - grid[i][j]
       end
    end
    return res
end