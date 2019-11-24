// review promises

// console.log('hi')

// setTimeout(() => {
//     console.log('times up!')
// },0)

// console.log('bye')
// would still execute hi, bye, times up

console.log('hi');

timeout();

console.log('end')


function timeout(){
    console.log('hey')
    setTimeout(()=> console.log('waiting'), 1000)
    console.log('hello')
}