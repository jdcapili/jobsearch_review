function* foo() {
    yield 'booting'
    for (let i = 0; i < 10; i++){
        yield i
    }
}

a = foo()
console.log(a.next())
console.log(a.next())
console.log(a.next())
console.log(a.next())
console.log(a.next())
console.log(a.next())
console.log(a.next())
console.log(a.next())
console.log(a.next())
console.log(a.next())

arr = ['a','b','c']
for(let i in arr){
    console.log(i)
}