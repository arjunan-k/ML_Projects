document.querySelector('.get-jokes').addEventListener('click', loadJokes);

function loadJokes(e) {
    const number = document.querySelector('input[type="number"]').value;
    const count = parseInt(number);

    for(i=0; i < count; i++) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `https://api.chucknorris.io/jokes/random`, true);
        xhr.onload = function() {
            if(this.status === 200) {
                const response = JSON.parse(this.responseText);
                const li = document.createElement('li');
                li.innerHTML = response.value;
                document.querySelector('.jokes').appendChild(li);
            }
        }
        xhr.send()
    }
    e.preventDefault();
}