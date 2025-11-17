# Gemini CLI & Web App

A Python-based tool for interacting with Google's Gemini AI API via command line or web interface.

## Features

- **CLI Tool**: Ask questions directly from your terminal
- **Web Interface**: User-friendly FastAPI-based web app with markdown rendering
- **Error Handling**: Built-in retry logic for rate limits and API errors
- **Secure**: Environment-based API key management

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))

## Installation

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API key**

Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### CLI Mode

Ask a single question from the command line:

```bash
python cli.py "What is machine learning?"
```

**Example:**
```bash
python cli.py "Explain quantum computing in simple terms"
```

### Web Interface

1. **Start the web server:**
```bash
python web_app.py
```

2. **Open your browser** and navigate to:
```
http://localhost:8000
```

3. **Ask questions** through the web form and get formatted responses

### Custom Port (Web)

```bash
PORT=5000 python web_app.py
```

## Error Handling

The tool includes automatic error handling for:

- **Missing API Keys**: Clear error message if `GEMINI_API_KEY` is not set
- **Rate Limits**: Exponential backoff retry (up to 3 attempts)
- **API Errors**: Graceful error messages instead of crashes
- **Empty Responses**: Warnings when no content is generated

## Project Structure

```
gemini-app/
├── app.py             # Core GeminiCLI class with API logic
├── cli.py             # Command-line interface
├── web_app.py         # FastAPI web application
├── requirements.txt   # Python dependencies
├── .env.example       # Template for environment variables
├── templates/
│   └── index.html     # Web UI template
└── README.md          # This file
```

## Troubleshooting

### "API key not found" error
- Ensure `.env` file exists in the project root
- Verify `GEMINI_API_KEY` is set in `.env`
- Check that `python-dotenv` is installed

### Rate limit errors
- The tool automatically retries with exponential backoff
- If persistent, check your API quota at [Google AI Studio](https://ai.google.dev/)

### Module not found errors
- Run `pip install -r requirements.txt`
- Ensure you're using Python 3.8+


## Deployment
Currently working on deployment using fly.io

## Resources

Built with:
- [Google Generative AI](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)