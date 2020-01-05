
var sortArrayByParity = function (A) {
    let [o, e] = [[], []];
    for (let ele of A) {
        if (ele % 2 === 0) e.push(ele);
        else o.push(ele)
    }
    return e.concat(o)

};

var sortArrayByParity = function (A) {
    A.sort((a,b) => a % 2 - b % 2)
    return A
};