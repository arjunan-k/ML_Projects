const posts = [
    {title: 'Post One', body: 'This is post one'},
    {title: 'Post Two', body: 'This is post two'},
    {title: 'Post Three', body: 'This is post three'},
    {title: 'Post Four', body: 'This is post four'}
]


function createPost(post) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            posts.push(post);
            let error = false
            if (!error) {
                resolve();
            } else {
                reject('Error, something went wrong')
            }
        }, 2000)
    })
}


function getPosts() {
    setTimeout(function(){
        let output = ""
        posts.forEach(function(post){
            output += `<li>${post.title}</li>`
        })
        document.body.innerHTML = output;
    }, 1000)
}


createPost({title: "Post Five", body: "This is post Five"}).then(getPosts).catch(function(error) {
    console.log(error)
});