class HashTable{
    constructor(size=53){
        this.keymap = new Array(size);
    }

    hashFunc(key){
        let total = 0;
        let WeirdPrime = 31;
        for( let i = 0; i < Math.min(key.length, 100); i++){
            let char = key[i];
            let value = char.charCodeAt(0) - 96;
            total = (total * WeirdPrime + value) % this.keymap.length
        }
        return total
    }

    get(key){

    }
}