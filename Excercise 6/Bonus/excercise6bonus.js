// Game variables
let lives = 3;
let score = 0;
const colors = ['red', 'green', 'blue'];
let correctColor;

// DOM elements
const target = document.getElementById('targetColor');
const options = document.getElementById('options');
const message = document.getElementById('message');
const livesDisplay = document.getElementById('lives');
const gameOver = document.getElementById('gameOver');
const finalScore = document.getElementById('finalScore');

// Start a new round
function newRound() {
    // Pick random color
    correctColor = colors[Math.floor(Math.random() * 3)];
    target.style.backgroundColor = correctColor;
    
    // Create options
    options.innerHTML = '';
    colors.forEach(color => {
        const div = document.createElement('div');
        div.style.backgroundColor = color;
        div.onclick = () => checkGuess(color);
        options.appendChild(div);
    });
}

// Check player's guess
function checkGuess(guess) {
    if (guess === correctColor) {
        score++;
        message.textContent = "Correct!";
    } else {
        lives--;
        livesDisplay.textContent = lives;
        message.textContent = "Wrong!";
        
        if (lives <= 0) {
            endGame();
            return;
        }
    }
    setTimeout(newRound, 1000);
}

// End the game
function endGame() {
    gameOver.style.display = 'block';
    finalScore.textContent = score;
    options.innerHTML = '';
    target.style.backgroundColor = 'white';
}

// Reset the game
function resetGame() {
    lives = 3;
    score = 0;
    livesDisplay.textContent = lives;
    gameOver.style.display = 'none';
    newRound();
}

// Start the game
newRound();