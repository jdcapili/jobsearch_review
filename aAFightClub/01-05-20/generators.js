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
