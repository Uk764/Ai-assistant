# 🤖 AI Chatbot — FastAPI + Groq Backend

A beginner-friendly AI chatbot backend built with **Python**, **FastAPI**, and the **Groq API** (free).
It receives messages from a frontend or API client, sends them to an AI model, and returns a reply.

---

## 📁 Project Structure

```
chatbot-backend/
├── .env                  ← Your secret API key (never share this)
├── requirements.txt      ← List of packages to install
├── run.py                ← Starts the server
└── app/
    ├── __init__.py       ← Marks this folder as a Python package (keep empty)
    ├── main.py           ← Creates the FastAPI app and sets up routes
    └── routers/
        ├── __init__.py   ← Marks this folder as a Python package (keep empty)
        └── chat.py       ← The main chatbot logic lives here
```

---

## ⚙️ Requirements

- Python 3.10 or newer
- A free Groq API key from [console.groq.com](https://console.groq.com)
- VS Code (recommended editor)

---

## 🚀 Setup Guide (Step by Step)

### 1. Clone or download this project

Put the project folder somewhere on your computer, e.g. your Desktop.

### 2. Open in VS Code

```
File → Open Folder → select chatbot-backend
```

### 3. Open the terminal in VS Code

```
Terminal → New Terminal
```

### 4. Create a virtual environment

A virtual environment keeps this project's packages separate from the rest of your computer.

```bash
python -m venv venv
```

### 5. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` appear at the start of the terminal line. ✅
Always make sure this is active before running any commands.

### 6. Install packages

```bash
python -m pip install -r requirements.txt
```

Wait 1–2 minutes for everything to install.

### 7. Add your API key

Create a file called `.env` in the root folder and add:

```
GROQ_API_KEY=gsk_paste-your-key-here
```

Get your free key at [console.groq.com](https://console.groq.com) → API Keys → Create Key.

### 8. Start the server

```bash
python run.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Started reloader process
```

### 9. Open in browser

Go to:
```
http://localhost:8000/docs
```

You'll see the interactive API page where you can test your chatbot. ✅

---

## 🌐 API Endpoints

### `GET /health`
Check if the server is running.

**Response:**
```json
{ "status": "ok" }
```

---

### `POST /api/chat`
Send a message and get a reply from the AI.

**Request body:**
```json
{
  "messages": [
    { "role": "user", "content": "Hello! What can you do?" }
  ],
  "system": "You are a helpful assistant.",
  "max_tokens": 1024
}
```

**Response:**
```json
{
  "reply": "Hi! I can answer questions, help you write, explain concepts, and much more!"
}
```

---

### How the `messages` array works

Every message has a `role` and `content`:
- `"user"` — something the human typed
- `"assistant"` — a previous reply from the AI

To keep conversation history, just keep adding to the array:

```json
{
  "messages": [
    { "role": "user", "content": "My name is John." },
    { "role": "assistant", "content": "Nice to meet you, John!" },
    { "role": "user", "content": "What is my name?" }
  ]
}
```

The AI will remember the context and reply: *"Your name is John!"*

---

## 🧪 Testing with the Docs Page

1. Go to `http://localhost:8000/docs`
2. Click **POST /api/chat**
3. Click **Try it out**
4. Edit the request body with your message
5. Click **Execute**
6. Scroll down to see the AI's reply

---

## 🔧 Common Problems & Fixes

| Problem | Fix |
|---|---|
| `pip` not recognized | Use `python -m pip` instead of `pip` |
| `No module named 'groq'` | Make sure `(venv)` is active, then run `python -m pip install -r requirements.txt` |
| `(venv)` not showing | Run `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac) |
| `Failed to Load Page` in browser | Use `http://localhost:8000/docs` not `http://0.0.0.0:8000` |
| `GROQ_API_KEY` error | Check your `.env` file exists and the key is pasted correctly with no spaces |
| Port 8000 already in use | Change `port=8000` to `port=8001` in `run.py` |

## 🛑 Stopping the Server

Press `Ctrl + C` in the terminal to stop the server.

---

## 🔄 Starting Again Next Time

Every time you open a new terminal, you need to activate the virtual environment first:

```bash
# Step 1 — activate venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac

# Step 2 — start the server
python run.py
```

---

## 🚢 What to Build Next

Once your backend is working, here are the next steps:

| Feature | What it means |
|---|---|
| **HTML Frontend** | A simple webpage with a chat box that talks to this backend |
| **React Frontend** | A more advanced chat UI built with React |
| **Save conversations** | Store chat history in a database so it persists |
| **User login** | Let multiple users have their own chat history |
| **Deploy online** | Put your chatbot on the internet so anyone can use it |

---

## 📚 Useful Links

- [Groq Console](https://console.groq.com) — manage your free API key
- [FastAPI Docs](https://fastapi.tiangolo.com) — learn more about FastAPI
- [Groq Models](https://console.groq.com/docs/models) — see all available AI models
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) — official beginner tutorial

---

## 🤝 Need Help?

If you get an error, copy the full error message from the terminal and search it online or ask an AI assistant. The most important part of the error is usually the last 2–3 lines.
