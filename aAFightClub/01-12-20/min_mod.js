// R R D
// L L D
// U U R

// GOAL: write recur func that travels through all possible paths from top left to bottom right

function traverse(graph, memo, row = 0, col = 0,visited = new Set()){
    const pos = row + ',' + col;
    if(pos in memo) {
        
        return memo[pos];
    }
    if(visited.has(pos))return 0;
    
    //  if we are at the bottom right, return
    if(row === graph.length -1 && col === graph[0].length -1) return 1;
    if(col < 0 || col >= graph[0].length) return 0;
    if(row < 0 || row >= graph.length) return 0;
    if(graph[row][col] === "W") return 0;
    visited.add(pos);

    // TODO maybe? other base cases?

    let numWays = 0;
    // move right
    numWays += traverse(graph, memo, row, col+1,new Set(visited));

    // move down
    numWays += traverse(graph, memo, row+1, col,new Set(visited));

    // move left
    numWays += traverse(graph, memo, row, col - 1,new Set(visited));

    // move up
    numWays += traverse(graph, memo, row - 1, col,new Set(visited));

    memo[pos] = numWays;
    return numWays
}



graph = [
    [0, 0, 0, 0],
    [0, "W", "W", 0],
    [0, 0, 0, 0],
    [0, "W", "W", 0],
    [0, 0, 0, 0],
]
let mem = {}
console.log(traverse(graph,mem))