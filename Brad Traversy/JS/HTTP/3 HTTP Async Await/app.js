const http = new EasyHTTP;

/*
http.get('https://jsonplaceholder.typicode.com/posts')
    .then(data => console.log(data))
    .catch(err => console.log(err))
*/

const data = {
    name: 'John Doe',
    username: 'john',
    email: "john@gmail.com"
}


/*
http.post('https://jsonplaceholder.typicode.com/posts', data)
    .then(data => console.log(data))
    .catch(err => console.log(err))
*/


/*
http.put('https://jsonplaceholder.typicode.com/posts/2', data)
    .then(data => console.log(data))
    .catch(err => console.log(err))
*/

/*
http.delete('https://jsonplaceholder.typicode.com/posts/2')
.then(() => console.log('Resource Deleted'))
.catch(err => console.log(err))
*/