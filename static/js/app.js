// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // Handle TTS (Text-to-Speech)
    document.getElementById("ttsButton").addEventListener("click", function() {
        const text = prompt("Enter the text for Text-to-Speech:");
        if (text) {
            fetch('/api/tts', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);
                } else {
                    alert('Something went wrong.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        } else {
            alert("Please enter some text.");
        }
    });

    // Handle STT (Speech-to-Text)
    document.getElementById("sttButton").addEventListener("click", function() {
        fetch('/api/stt', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            if (data.text) {
                alert('You said: ' + data.text);
            } else {
                alert('No speech detected or an error occurred.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

});
