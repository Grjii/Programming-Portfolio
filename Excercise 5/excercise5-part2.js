const sounds = ['Ah-ha', 'Back of the net', 'Bang out to forder','Dan', 'Email of the evening', 'Hello partridge', 'I ate so much egg', 'Im confused' ];

sounds.forEach(sound => {
    const btn = document.createElement('button');
    btn.classList.add('btn');
    btn.innerText = sound;
    
    btn.addEventListener('click', () => {
        document.getElementById(sound).play();
    });
    
    document.getElementById('buttons').appendChild(btn);
});