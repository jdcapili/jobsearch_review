// ============================================================================
// Implementation Exercise: Queue
// ============================================================================
//
// -------
// Prompt:
// -------
//
// Implement a Queue and all of its methods below!
//
// ------------
// Constraints:
// ------------
//
// Make sure the time and space complexity of each is equivalent to those 
// in the table provided in the Time and Space Complexity Analysis section
// of your Stack reading!
//
// -----------
// Let's Code!
// -----------

class Node {
  constructor(val = null){
    this.next = null;
    this.value = val;
  }

}

class Queue {
  constructor(){
    this.front = null;
    this.back = null;
    this.length = 0;
  }

  enqueue(inp){
    let node = new Node(inp);
    if(!this.front){
      this.front = node;
      this.back = node;
    }else{
      let temp = this.back;
      temp.next = node;
      this.back = node;
    }

    this.length ++;
    return this.length;
  }

  dequeue(){
    if(!this.front) return null
    let temp = this.front;
    if(this.length == 1){
      this.front = null
      this.back = null
    }else{
      this.front = temp.next;
    }
    
    this.length --;
    return temp.value
  }

  size(){
    return this.length
  }

}

exports.Node = Node;
exports.Queue = Queue;