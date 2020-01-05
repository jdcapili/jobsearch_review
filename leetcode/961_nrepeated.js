var repeatedNTimes = function (A) {
    let c = {};
    for (let ele of A) {
        if (!(ele in c)) c[ele] = 0;
        c[ele] += 1
    }

    for (let k in c) if (c[k] > 1) return k
};

var repeatedNTimes = function (A) {
    let c = new Set();
    for (let ele of A) {
        if (c.has(ele)) return ele;
        else c.add(ele);
    }

};