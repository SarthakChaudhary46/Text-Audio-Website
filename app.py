from flask import Flask, request, render_template, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            # Generate a unique filename for each audio file
            filename = f"{uuid.uuid4().hex}.mp3"
            # Create the audio file using gTTS
            tts = gTTS(text=text, lang='en')
            tts.save(f"static/{filename}")  # Save to the static folder
            audio_file = filename  # Store the filename for use in the template
    return render_template('index.html', audio_file=audio_file)

@app.route('/download/<filename>')
def download(filename):
    # Serve the file for download
    return send_file(f'static/{filename}', as_attachment=True)

if __name__ == '__main__':
    # Ensure the static folder exists
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
