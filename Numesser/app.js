let min = 1, 
    max = 10, 
    winningNum = getRandomNum(min, max),
    guessLeft = 3;

const game = document.querySelector('#game'),
      minNum = document.querySelector('.min-num'),
      maxNum = document.querySelector('.max-num'),
      guessBtn = document.querySelector('#guess-btn'),
      guessInput = document.querySelector('#guess-input'),
      message = document.querySelector('.message');

minNum.textContent = min
maxNum.textContent = max

loadAllEvent();

function loadAllEvent() {
    game.addEventListener('mousedown', function(e){
        if (e.target.className === 'play-again') {
            window.location.reload();
        }
    })
    guessBtn.addEventListener('click', function(){
        let guess = parseInt(guessInput.value);
        if (guess > max || guess < min || isNaN(guess)) {
            setMessage(`Please enter a number between ${min} and ${max}`, 'red');
            return;
        };
        if (guess === winningNum) {
            gameOver(true, `${winningNum} is correct, You Won!`);
        } else {
            guessLeft -= 1

            if (guessLeft === 0) {
                gameOver(false, `Game Over, you lost. The correct number was ${winningNum}`);
            } else {
                guessInput.style.borderColor = 'red';
                setMessage(`${guess} is Incorrect, you have ${guessLeft} guesses left`, 'red');
                guessInput.value = ""
            }
        }
    })
}

function setMessage(msg, color){
    message.textContent = msg;
    message.style.color = color;
}

function gameOver(won, msg){
    let color;
    won === true ? color = 'green' : color = 'red';
    guessInput.disabled = true;
    guessInput.style.borderColor = color;
    setMessage(msg, color);
    guessBtn.value = 'Play Again';
    guessBtn.className += 'play-again';
};

function getRandomNum(min, max){
    return Math.floor(Math.random() * (max-min+1) + min);
}