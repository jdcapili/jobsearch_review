var wordBreak = function(s, wordDict) {
  let curStr = ""
  let dictSet = new Set(wordDict);
  for(let char of s){
      if(dictSet.has(curStr)){
          curStr = ""
      }else{
          curStr += char;
      }
  }
}
