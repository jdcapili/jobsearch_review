var wordBreak = function(s, wordDict) {
    let dict = new Set(wordDict);
    let f = [true];
    let word;
    for (let i = 1; i < s.length; i++) {
        for (let j = 0; j < i; j++) {
            word = s.slice(j,i);
            if (f[j] && dict.has(word)) {
                f[i] = true;
                console.log(word,f)
                break;
            }else{
                f[i] = false;
                
            }
        }
    }
    console.log(f[-1])
    return f[-1];
}

wordBreak("aaaaaaa",
["aaaa", "aaa"]);
wordBreak("applepenapple",
["apple", "pen"])
