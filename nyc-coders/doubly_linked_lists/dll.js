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

    print(){
        let current = this.head;
        while(current){
            process.stdout.write(`${current.value} -> `);
            current = current.next;
        }
        console.log(current)

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

    insertAtIndex(index, val){
        // check if index is within the range
        if(index === 0){
            this.unshift(val)
        }else if(index === this.length -1){
            let poppedNode = this.pop();
            this.push(val);
            this.tail.next = poppedNode;
            poppedNode.prev = this.tail;
        }else{
            let counter = 1
            let current = this.head.next;
            while(counter != index){
                current = current.next;
                counter++;
            }

            let node = new Node(val);
            let prevNode = current.prev;
            let nextNode = current;
            prevNode.next = node;
            nextNode.prev = node;
            node.prev = prevNode;
            node.next = nextNode;
            this.length++;

        }

        return this
    }

    removeAtIndex(){

    }

    getIndex(){

    }

    setIndex(){

    }
}

dll = new DoublyLinkedLists();
dll.push(1);
dll.push(2);
dll.push(3);
dll.print();
dll.insertAtIndex(1,4)
dll.print();
// console.log(dll.pop())
// console.log(dll.unshift(3))
// console.log(dll.shift())
// console.log(dll)


