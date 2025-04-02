function textToSpeech() {
    let text = document.getElementById('textInput').value;
    let speech = new SpeechSynthesisUtterance();
    speech.text = text
    window.speechSynthesis.speak(speech)
}

const sounds = ['Goat Scream', 'Man Screaming','Dinosaur Scream','Bruh','PS2 Startup','FBI Open Up','Dial Up Internet','Kaching','WOW' ];

sounds.forEach(sound => {
    const btn = document.createElement('button');
    btn.classList.add('btn');
    btn.innerText = sound;
    
    btn.addEventListener('click', () => {
        document.getElementById(sound).play();
    });
    
    document.getElementById('buttons').appendChild(btn);
});