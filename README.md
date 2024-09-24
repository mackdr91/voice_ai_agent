# Acme IT Solutions Voice Assistant

This project is a voice assistant for Acme IT Solutions, designed to interact with customers via voice using LiveKit. The assistant is built using Python and integrates with various plugins for voice activity detection (VAD), speech-to-text (STT), text-to-speech (TTS), and language model (LLM) functionalities.

## Features

- Voice Activity Detection using Silero VAD
- Speech-to-Text using OpenAI STT
- Text-to-Speech using OpenAI TTS
- Language Model integration using OpenAI LLM
- Customizable chat context for the assistant

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/acme-voice-assistant.git
    cd acme-voice-assistant
    ```

2. Install dependencies using Pipenv:
    ```sh
    pipenv install
    ```

3. Create a `.env` file in the root directory and add your environment variables (if any).

## Usage

1. Activate the Pipenv shell:
    ```sh
    pipenv shell
    ```

2. Run the application:
    ```sh
    python main.py
    ```

## Configuration

The main configuration for the assistant is done in the `main.py` file. You can customize the initial chat context and other parameters as needed.

## Project Structure

- `main.py`: The main entry point of the application.
- `Pipfile`: Specifies the dependencies for the project.
- `Pipfile.lock`: Locks the dependencies to specific versions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
