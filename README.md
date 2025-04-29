# ai-agent-api
A lightweight FastAPI server that connects to the Groq LLM API to generate AI responses from user questions.

Features :
- 🔥 FastAPI backend

- 🤖 Integration with Groq large language models (LLM)

- 📄 Simple REST API (POST /ask)

- 🔒 Secure with .env environment variables

- 🛠 Easy to deploy anywhere (VPS, Railway, Render, etc.)

## Getting Started
1. Clone the repository
    ```bash
    git clone https://github.com/your-username/ai-agent-api.git
    ```
    ```bash
    cd ai-agent-api
    ```
2. Create a Virtual Environment
    ```bash
    python -m venv .venv
    ```
    Activate the Virtual Environment
    - On Windows (CMD):
        ```bash
        .venv\Scripts\activate
        ```
    - On Windows (PowerShell):
        ```bash
        .\.venv\Scripts\Activate.ps1
        ```
    - On macOS / Linux:
        ```bash
        source .venv/bin/activate
        ```
3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Set up environment variables
    ```bash
    cp .env.example .env
    ```
    Then edit .env and add your Groq API key:
    ```bash
    GROQ_API_KEY=your_groq_api_key_here
    ```
    You can get your Groq API key here: https://console.groq.com/keys
5.  Run the server
    ```bash
    uvicorn app:app --reload
    ```
    Server will start at: http://127.0.0.1:8000/

    Access API docs at: http://127.0.0.1:8000/docs

    Test the root endpoint: GET /

    Ask questions: POST /ask

## API Usage
POST /ask

Request body:
```json
{
  "question": "What is quantum computing?"
}
```
Response:
```json
{
  "answer": "Quantum computing is a type of computation that leverages quantum mechanics..."
}
```

## Project Structure
```bash
├── app.py            # Main FastAPI app
├── .env.example      # Example environment file
├── requirements.txt  # Python dependencies
├── README.md         # This readme file
├── Procfile          # For deployment
└── .gitignore        # Git ignore settings
```

Made with ❤️ using FastAPI and Groq.