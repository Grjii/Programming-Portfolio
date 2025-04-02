function textToSpeech() {
    // Get the text entered in the textarea with id 'textInput'
    let text = document.getElementById('textInput').value;
    let speech = new SpeechSynthesisUtterance();
    speech.text = text;
    window.speechSynthesis.speak(speech);
}

// List of sound file ids for the sounds that will be played
const sounds = ['Ah-ha', 'Back of the net', 'Bang out to forder','Dan', 'Email of the evening', 'Hello partridge', 'I ate so much egg', 'Im confused', 'Well be right back'];

// Loop through each sound in the sounds array
sounds.forEach(sound => {
    // Create a new button for each sound
    const btn = document.createElement('button');
    
    // Add a 'btn' class to style the button
    btn.classList.add('btn');
    
    // Set the text of the button to the sound name
    btn.innerText = sound;
    
    // Add an event listener to the button, so when it's clicked, the corresponding sound is played
    btn.addEventListener('click', () => {
        document.getElementById(sound).play();
    });
    
    // Append the button to the div with id 'buttons' in the HTML
    document.getElementById('buttons').appendChild(btn);
});
