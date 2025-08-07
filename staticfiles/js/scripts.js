// frontend/static/js/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Welcome to NammaJal!");
    // Future interactivity can be added here
});

function togglePassword(inputId) {
    const inputField = document.getElementById(inputId);
    const type = inputField.getAttribute('type') === 'password' ? 'text' : 'password';
    inputField.setAttribute('type', type);
}

let isRecording = false; // Variable to track the recording state
let mediaRecorder;

function toggleSpeechRecognition() {
    if (!isRecording) {
        startRecording(); // Start recording if not already recording
    } else {
        stopRecording(); // Stop recording if currently recording
    }
}

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            // Change the icon to indicate recording
            document.getElementById('audio-icon').src = "{% static 'images/recording-icon.png' %}";

            // Handle the data when recording stops
            mediaRecorder.ondataavailable = (event) => {
                const formData = new FormData();
                formData.append('audio', event.data, 'audio.wav');

                fetch('/read-aloud/', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is included
                    }
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    // Process the response (e.g., update the UI based on command result)
                })
                .catch(error => console.error('Error:', error));
            };

            isRecording = true; // Update the recording state
        })
        .catch(error => console.error('Error accessing media devices.', error));
}

function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop(); // Stop the recording
        isRecording = false; // Update the recording state

        // Change the icon back to the original
        document.getElementById('audio-icon').src = "{% static 'images/audio-icon.png' %}";
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



// End of new read-aloud functionality