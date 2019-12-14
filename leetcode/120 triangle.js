var minimumTotal = function(triangle) {
    if(triangle.length == 0) return 0;
    
    let [j,sum,lvl] = [0,triangle[0][0],null];
    
    for(let i = 1; i < triangle.length; i++){
        lvl = triangle[i]
        console.log(lvl,j,sum)
        if(lvl[j] >= lvl[j+1]){
            sum += lvl[j+1];
            j++;
        }else{
            sum += lvl[j]; 
        }
    }
    
    return sum;
};

let tri = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
];

minimumTotal(tri)