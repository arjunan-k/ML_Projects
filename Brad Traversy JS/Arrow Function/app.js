const sayHello1 = function() {
    console.log("Hello1")
}

const sayHello2 = () => {
    console.log("Hello2")
}

const sayHello3 = () => 'Hello3'

const sayHello4 = () => {
    return 'Hello4'
}

const sayHello5 = () => ({"msg": "Hello5"})

let sayHello6 = (name) => console.log(`Hello6 ${name}`)
// const sayHello6 = name => console.log(`Hello6 ${name}`)

sayHello1()
sayHello2()
console.log(sayHello3())
console.log(sayHello4())
console.log(sayHello5())
sayHello6('Appu')


const users = ['Nathan', 'John', 'Brad', 'Appu']

/*
const nameLength = users.map(function(name) {
    return name.length
})
const nameLength = users.map((name) => {
    return name.length
})
*/

const nameLength = users.map(name => name.length)

console.log(users)
console.log(nameLength)