const posts = [
    {title: 'Post One', body: 'This is post one'},
    {title: 'Post Two', body: 'This is post two'},
    {title: 'Post Three', body: 'This is post three'},
    {title: 'Post Four', body: 'This is post four'}
]


// function createPost(post) {
//     setTimeout(function() {
//         posts.push(post)
//     }, 2000)
// }

// function getPosts() {
//     setTimeout(function(){
//         let output = ""
//         posts.forEach(function(post){
//             output += `<li>${post.title}</li>`
//         })
//         document.body.innerHTML = output;
//     }, 1000)
// }

// createPost({title: "Post Five", body: "This is post Five"})

// getPosts()


function createPost(post, callback) {
    setTimeout(function() {
        posts.push(post)
        callback()
    }, 2000)
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

createPost({title: "Post Five", body: "This is post Five"}, getPosts)