document.getElementById('button1').addEventListener('click', getText)
document.getElementById('button2').addEventListener('click', getJson)
document.getElementById('button3').addEventListener('click', getAPI)

function getText() {
    fetch('text.txt')
        .then(res => res.text())
        .then(data => document.getElementById('output').innerHTML = data)
        .catch(err => console.log(err))
}

function getJson() {
    fetch('posts.json')
        .then(res => res.json())
        .then(data => {
            let output = ""
            data.forEach(element => {
                output += `<li>${element.title}, ${element.body}</li>`
            });
            document.getElementById('output').innerHTML = output
            })
        .catch(err => console.log(err))
}


function getAPI() {
    fetch('https://api.github.com/users')
        .then(res => res.json())
        .then(function(data) {
            let output = ""
            data.forEach(user => {
                output += `<li>${user.login}</li>`
            });
            document.getElementById('output').innerHTML = output
            })
        .catch(err => console.log(err))
}


/*
function handleErrors(res) {
    if (!res.ok) throw new Error(res.error);
    return res;
  }
   
fetch('https://devcamper.io/api/v1/bootcamps/34343')
    .then(res => res.json())
    .then(handleErrors)
    .then(res => console.log(res.data))
    .catch(err => console.log(err));
*/