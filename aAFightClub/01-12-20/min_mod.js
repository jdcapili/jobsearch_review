// R R D
// L L D
// U U R

// GOAL: write recur func that travels through all possible paths from top left to bottom right

function traverse(graph, row = 0, col = 0){
    //  if we are at the bottom right, return
    if(row === graph.length && col === graph[0].length -1) return 1;
    if(col >= graph[0].length) return 0;
    if(row >= graph.length) return 0;

    // TODO maybe? other base cases?

    let numWays = 0;
    // move right
    numWays += traverse(graph, row, col+1);

    // move down
    numWays += traverse(graph, row+1, col);

    return numWays
}



graph = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

console.log(traverse(graph))