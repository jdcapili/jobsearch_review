// review promises

// console.log('hi')

// setTimeout(() => {
//     console.log('times up!')
// },0)

// console.log('bye')
// would still execute hi, bye, times up

// console.log('hi');

// timeout();

// console.log('end')


// function timeout(){
//     console.log('hey')
//     setTimeout(()=> console.log('waiting'), 1000)
//     console.log('hello')
// }


// PROMISE has 2 terminal states
// - resolved
// - rejected
// Promise has 2 intermediate state
// -pending

// const task1 = new Promise((resolve, reject) =>{
//     setTimeout(() => {
//         console.log('bye');
//         resolve(42);
//     },1000)
// });

// task1.then(task2)//.catch(task3)

// function task2(resolution){
//     console.log('value is', resolution)
//     console.log('two')
// }

// function task3(){
//     console.log('three')
// }

// Always handle promise rejections

// 