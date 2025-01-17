const http = new easyHTTP;


http.get('https://jsonplaceholder.typicode.com/posts', function(err, posts) {
    if(err) {
        console.log(err)
    } else {
        console.log(posts)
    }
})


http.get('https://jsonplaceholder.typicode.com/posts/11', function(err, post) {
    if(err) {
        console.log(err)
    } else {
        console.log(post)
    }
})


const data = {
    title: "Custom Post",
    body: "Custom Body"
}


http.post('https://jsonplaceholder.typicode.com/posts', data, function(err, post) {
    if(err) {
        console.log(err)
    } else {
        console.log(post)
    }
})


http.put('https://jsonplaceholder.typicode.com/posts/5', data, function(err, post) {
    if(err) {
        console.log(err);
    } else {
        console.log(post)
    }
})


http.delete('https://jsonplaceholder.typicode.com/posts/1', function(err, post) {
    if(err) {
        console.log(err)
    } else {
        console.log(post)
    }
})