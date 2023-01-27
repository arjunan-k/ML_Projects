// function* sayNames() {
//     yield 'Jill'
//     yield 'John'
//     yield 'Appu'
// }

// const name = sayNames()
// console.log(name.next())
// console.log(name.next())
// console.log(name.next())
// console.log(name.next())


function* idGenerator() {
    let i = 1
    while(true) {
        yield i++
    }
}

const id = idGenerator();
console.log(id.next())
console.log(id.next())
console.log(id.next())
console.log(id.next())