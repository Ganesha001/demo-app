let score = 0;
let gameArea = document.getElementById("game-area");
let scoreDisplay = document.getElementById("score");
let panda = document.getElementById("panda");
let presents = document.querySelectorAll(".present");

// Function to randomize present position
function movePresent(present) {
    const xPos = Math.random() * (gameArea.offsetWidth - present.offsetWidth);
    const yPos = Math.random() * (gameArea.offsetHeight - present.offsetHeight);
    present.style.left = `${xPos}px`;
    present.style.top = `${yPos}px`;
}

// Add event listener to each present
presents.forEach(present => {
    present.addEventListener("click", function() {
        score += 10;
        scoreDisplay.textContent = score;

        // Move the present to a new random position
        movePresent(present);

        // Check if the score reaches 100
        if (score >= 100) {
            showPanda();
        }
    });
});

// Show Panda when score reaches 100
function showPanda() {
    panda.classList.remove("hidden");
}

// Start the game by moving presents to random positions
presents.forEach(present => {
    movePresent(present);
});
