// async function myFunc() {
//     const promise = new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve('Hello2')
//         }, 2000);
//     })
//     const error = false
//     if(!error) {
//         const res = await promise;
//         return res
//     } else {
//         return 'Not Working'
//     }
// }

// myFunc()
//     .then(res => console.log(res))
//     .catch(err => console.log(err))


async function getUser() {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts');

    const data = await response.json()

    return data
}

getUser().then(res => console.log(res));