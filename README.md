# Flask Text-to-Speech Application

This project is a simple Flask web application that converts text to speech using **gTTS (Google Text-to-Speech)**. The application takes user input as text, converts it to speech, and allows users to download the audio.

## Features
- **Text-to-Speech**: Converts user input into speech using the Google Text-to-Speech API.
- **Downloadable Audio**: Allows the user to download the audio as an MP3 file.

## Requirements
Before running this app locally, you need to install the following dependencies:

- **Flask**: A lightweight Python web framework.
- **gTTS**: Python library to interact with Google Text-to-Speech API.

### Install Dependencies
Run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Application Locally

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```
