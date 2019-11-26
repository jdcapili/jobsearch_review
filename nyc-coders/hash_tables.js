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

    set(key,value){
        let idx = hashFunc(key)
        // check if anything exists this.keymap[idx]
        if(!this.keymap[idx]){
            // if undefined, initialize array
            // push [key, value]
            this.keymap[idx] = []
        }
        this.keymap[idx].push([key, value]);
    }

    get(key){
        let idx = hashFunc(key);
        if(!this.keymap[idx]) return undefined
        else{
            this.keymap[idx].forEach((subarr) => {
                if(subarr[0] === key) return subarr[1]
            })
            return undefined
        }
    }
}