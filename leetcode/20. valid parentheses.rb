def is_valid(s)
    
  paren = {')' => '(', '}' => '{', ']' => '['}
  return false if paren[s[0]]
  stack = []
  i = 0
    
  while i < s.length do
      if !paren[s[i]]
          stack.push(s[i])
      elsif stack[-1] === paren[s[i]]
          stack.pop
      else
          return false
      end
      i += 1
      
  end
    
  stack.empty? ? true : false
    
end