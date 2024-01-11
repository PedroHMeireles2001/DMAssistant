# DMAssitant

## Description
This Python script serves as a conversational assistant for Dungeon Masters (DMs) in Dungeons & Dragons 5th Edition (D&D 5e). It leverages OpenAI's GPT-4 language model and the OpenAI API for text-based interactions. Users can input messages through the command line, and the script generates contextually relevant responses using GPT-4. The generated text responses are then converted into speech using OpenAI's text-to-speech (TTS) model, providing an immersive experience for DMs.

## Prerequisites
1. [OpenAI API Key](https://beta.openai.com/signup/)
2. Python 3.6 or later
3. Install required Python packages by running: `pip install openai playsound python-dotenv`

## Usage
1. Clone or download the repository.
2. Create a `.env` file using the command: `echo OPENAI_API_KEY=your_api_key > .env` (replace `your_api_key` with your actual OpenAI API key).
3. Run the script using the command: `python script_name.py`

## Troubleshooting
If you encounter any issues, consider the following steps:

1. **API Key**: Ensure that your OpenAI API key is correctly set in the `.env` file.

2. **Package Installation**: Confirm that the required Python packages are installed. Run: `pip install openai playsound python-dotenv`

3. **Environment Variables**: Check if the environment variables are loading correctly from the `.env` file using `dotenv.load_dotenv()`.

4. **OpenAI API Limits**: Be mindful of OpenAI API usage limits. If you exceed your limits, you may need to upgrade your account or wait for the limits to reset.

5. **Internet Connection**: Ensure you have a stable internet connection, as the script relies on online services.

6. **OpenAI Model Availability**: Verify that the GPT-4 model is available and accessible through the OpenAI API.

7. **OpenAI Credits**: verify if you have enough credits in your OpenAI account

## Important Note
Ensure that you comply with OpenAI's usage policies and guidelines when using this script with the OpenAI API.

## Acknowledgments
- [OpenAI](https://beta.openai.com/): For providing the GPT-4 language model and API.
- [python-dotenv](https://pypi.org/project/python-dotenv/): For loading environment variables from a .env file.
- [playsound](https://pypi.org/project/playsound/): For playing audio files in Python.
