// var DLL = function (key = null, val = null) {
//     this.key = key;
//     this.val = val;
//     this.next = null;
//     this.prev = null;
// }

// // /**
// //  * @param {number} capacity
// //  */
// var LRUCache = function (capacity) {
//     this.head = new DLL();
//     this.tail = new DLL();
//     [this.head.next, this.tail.prev] = [this.tail, this.head]
//     this.lookup = {}
//     this.cur_size = 0;
//     this.max_size = capacity;
// };

// // /** 
// //  * @param {number} key
// //  * @return {number}
// //  */
// LRUCache.prototype.get = function (key) {
//     const {value,next,prev} = this.lookup[key]

//     if (!node) return -1;
//     let [tmpNxt, tmpPrev] = [node.next, node.prev];
//     [tmpNxt.prev, tmpPrev.next] = [tmpPrev, tmpNxt];
//     let tmpLast = this.tail.prev;
//     [tmpLast.next, node.prev, node.next, this.tail.prev] = [node, tmpLast, this.tail, node]
//     return value

// };

// // /** 
// //  * @param {number} key 
// //  * @param {number} value
// //  * @return {void}
// //  */
// LRUCache.prototype.put = function (key, value) {
//     let node;

//     if (key in this.lookup) {
//         node = this.lookup[key];
//         node.val = value;
//         this.lookup[key] = node;
//         console.log(value, this.lookup[key])

//     } else {
//         node = new DLL(key, value);
//         this.lookup[key] = node;
//     }

//     if (this.cur_size < this.max_size) this.cur_size += 1;
//     else {
//         delete this.lookup[this.head.next.key];
//         this.head.next = this.head.next.next;
//     }

//     let tmp = this.tail.prev;
//     [tmp.next, node.prev] = [node, tmp];
//     [this.tail.prev, node.next] = [node, this.tail];


// };



// /**
//  * Your LRUCache object will be instantiated and called as such:
//  * var obj = new LRUCache(capacity)
//  * var param_1 = obj.get(key)
//  * obj.put(key,value)
//  */



// SOLUTION

/**
 * @param {number} capacity
 */
var LRUCache = function (capacity) {
    this._capacity = capacity;
    this._count = 0;
    this._head = null;
    this._tail = null;
    this._hashTable = {};
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
    if (this._hashTable[key]) {
        const { value } = this._hashTable[key];
        const { prev, next } = this._hashTable[key];
        if (prev) { prev.next = next; }
        if (next) { next.prev = prev || next.prev; }

        if (this._tail === this._hashTable[key]) {
            this._tail = prev || this._hashTable[key];
        }

        this._hashTable[key].prev = null;
        if (this._head !== this._hashTable[key]) {
            this._hashTable[key].next = this._head;
            this._head.prev = this._hashTable[key];
        }

        this._head = this._hashTable[key];

        return value;
    }

    return -1;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {
    if (this._hashTable[key]) {
        this._hashTable[key].value = value;
        this.get(key);
    } else {
        this._hashTable[key] = { key, value, prev: null, next: null };
        if (this._head) {
            this._head.prev = this._hashTable[key];
            this._hashTable[key].next = this._head;
        }

        this._head = this._hashTable[key];

        if (!this._tail) {
            this._tail = this._hashTable[key];
        }

        this._count += 1;
    }

    if (this._count > this._capacity) {
        let removedKey = this._tail.key;

        if (this._tail.prev) {
            this._tail.prev.next = null;
            this._tail = this._tail.prev;
            this._hashTable[removedKey].prev = null;
        }

        delete this._hashTable[removedKey];

        this._count -= 1;
    }
};