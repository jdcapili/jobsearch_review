// abstract data types
// big O notation of DLL is worse than SLL but you can traverse through it better
// import Node from "./node"

class Node {
    constructor(val = null) {
        this.value = val;
        this.next = null;
        this.prev = null;
    }
}

// a = new Node(5)
// console.log(a.value)

class DoublyLinkedLists{
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(val){
        let node = new Node(val);
        if(!this.head){
            this.head = node;
            this.tail = node;
        }else{
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        }

        this.length ++;
        return this
    }

    pop(){
        let node = this.tail;
        if(this.tail){
            if(this.length > 1){
                this.tail = node.prev;
                this.tail.next = null;
                node.prev = null;
            }else{
                this.tail = null;
                this.head = null;
            }
            this.length --;
        }
        return node
        
    }

    shift(){
        let node = this.head;
        if(!node){
            return node
        }else if(this.head === this.tail){
            this.head = null
            this.tail = null
        }else{
            this.head = node.next;
            this.head.prev = null;
            node.prev = null;
        }
        this.length --;
        return node
    }

    unshift(val){
        let node = new Node(val);
        if(!this.head){
            this.head = node;
            this.tail = node;
        }else{
            node.next = this.head;
            this.head.prev = node;
            this.head = node;
        }

        this.length ++;
        return this
    }

    insertAtIndex(){

    }

    removeAtIndex(){

    }

    getIndex(){

    }

    setIndex(){

    }
}

dll = new DoublyLinkedLists();
console.log(dll.push(2))
console.log(dll.push(3))
console.log(dll.pop())
console.log(dll.unshift(3))
console.log(dll.shift())
console.log(dll)


