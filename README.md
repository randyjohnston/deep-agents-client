# Deep Agents Client

A command-line client for chatting with a deployed Deep Agents server via the LangGraph SDK. Responses stream back to the terminal in real time, and all messages in a session share a single thread so the agent maintains conversation context.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- A LangSmith API key with access to the deployed agent

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Copy the example env file and add your API key:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and set `LANGSMITH_API_KEY` to your key.

## Running

```bash
uv run main.py
```

The client creates a new thread and drops you into a chat loop. Type your message and press Enter — the agent's response streams back token by token.

```
Thread: 019e4b1c-e27b-7df1-93cc-3263817b60d5
Type 'exit' or 'quit' to end.

You: Hello!
Assistant: Hi! How can I help you today?

You: exit
```

Type `exit` or `quit` (or press Ctrl+C) to end the session.
