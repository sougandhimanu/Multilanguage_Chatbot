# 🌐 Multilanguage Chatbot

A **Streamlit-based multilingual AI chatbot** that allows users to register, log in, communicate with an AI assistant in multiple languages, and maintain their own chat history.

The chatbot uses a **GPT API** for generating responses and the **Serper API** to retrieve web search results when the user asks for dynamic or current information.

---

## ✨ Features

* 🔐 User registration and login
* 👤 Individual user accounts
* 💬 AI-powered conversations
* 🌍 Multilingual support
* 🔎 Web search for dynamic/current information
* 📝 Persistent chat history
* 🚪 Logout functionality
* 🗑️ Account deletion
* 🖥️ Streamlit-based user interface

---

## 🌍 Supported Languages

The chatbot currently supports:

* 🇺🇸 English
* 🇪🇸 Spanish
* 🇫🇷 French

The application automatically detects the language of the user's message using **LangDetect**.

The message is then:

```text
User Input
     ↓
Language Detection
     ↓
Translate to English
     ↓
GPT Chatbot
     ↓
Translate Response
     ↓
Display Response
```

---

## 🤖 APIs Used

### 1. GPT API

The chatbot uses a GPT-compatible API to generate AI responses.

The API is called through:

```python
openai.ChatCompletion.create()
```

The GPT response is generated from the user's translated input.

### 2. Serper API

The **Serper API** is used to perform web searches when the chatbot needs dynamic or current information.

Examples include:

* Latest news
* Cricket schedules
* IPL information
* Live cricket scores
* Football matches
* Match results

The application sends the search query to:

```text
https://google.serper.dev/search
```

The top three search results are returned to the chatbot interface.

---

## 🔑 API Credentials

API credentials are stored locally in a file named:

```text
cred.json
```

Example structure:

```json
{
    "api_base": "YOUR_API_BASE_URL",
    "api_key": "YOUR_GPT_API_KEY",
    "serper_key": "YOUR_SERPER_API_KEY"
}
```

### ⚠️ Security

**Never upload `cred.json` to GitHub.**

The file contains sensitive API credentials and should remain local.

Add the following to your `.gitignore`:

```text
cred.json
```

The repository intentionally does **not** contain `cred.json`.

---

## 🏗️ Project Structure

```text
Multilanguage_Chatbot/
│
├── app.py
├── chatbot.py
├── database.py
├── requirements.txt
├── readme.md
├── .gitignore
│
└── cred.json              # Local only - DO NOT upload
```

### `app.py`

The main Streamlit application.

It handles:

* Login
* Registration
* Language selection
* User input
* Translation
* Chat interface
* Chat history
* Logout
* Account deletion

### `chatbot.py`

Handles the chatbot functionality.

It contains:

* GPT API integration
* Serper web search integration
* Dynamic search detection
* GPT response processing
* Web search fallback

### `database.py`

Handles user and chat data.

It provides functions for:

```python
register_user()
authenticate_user()
add_chat()
get_chat_history()
delete_user()
```

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

## 🔄 How the Chatbot Works

The application follows this workflow:

```text
                    ┌──────────────────┐
                    │   Streamlit App  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Login / Register │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Chat Page     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ User enters text │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Language Detect  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Translate to EN  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    GPT API       │
                    └────────┬─────────┘
                             │
                  ┌──────────┴──────────┐
                  │                     │
            Normal response       Dynamic query /
                  │                GPT uncertain
                  │                     │
                  │                     ▼
                  │              ┌──────────────┐
                  │              │ Serper API   │
                  │              └──────┬───────┘
                  │                     │
                  └──────────┬──────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Translate result │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Display response │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Save chat history│
                    └──────────────────┘
```

---

## 🔎 Dynamic Web Search

The chatbot can trigger a web search when the user's query appears to require current information.

Some predefined dynamic queries include:

```text
ipl schedule
ipl 2025 schedule
match schedule
cricket schedule
live cricket score
match result
football match
yesterday's news
latest news
```

The chatbot can also trigger a search when GPT returns responses indicating uncertainty, such as:

```text
I'm not sure
I don't know
cannot help
don't have information
I'm unable to
I am not able
I recommend checking
I suggest visiting
```

When a search is triggered, the application uses the **Serper API** and displays the top three search results.

---

## 🛠️ Technologies Used

| Technology                    | Purpose                    |
| ----------------------------- | -------------------------- |
| **Python**                    | Application development    |
| **Streamlit**                 | Web interface              |
| **OpenAI-compatible GPT API** | AI-generated responses     |
| **Serper API**                | Web search                 |
| **LangDetect**                | Language detection         |
| **Googletrans**               | Translation                |
| **Requests**                  | HTTP requests to Serper    |
| **JSON**                      | Credential configuration   |
| **Database**                  | User and chat data storage |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sougandhimanu/Multilanguage_Chatbot.git
```

Move into the project directory:

```bash
cd Multilanguage_Chatbot
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configure API Credentials

Create a file named:

```text
cred.json
```

in the project root.

Add your credentials:

```json
{
    "api_base": "YOUR_API_BASE_URL",
    "api_key": "YOUR_GPT_API_KEY",
    "serper_key": "YOUR_SERPER_API_KEY"
}
```

Replace the placeholder values with your actual credentials.

### Important

Do **not** upload this file to GitHub.

Make sure `.gitignore` contains:

```text
cred.json
```

---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application runs on Streamlit's default port:

```text
http://localhost:8501
```

---

## 👤 Registration

New users can create an account by selecting **Register**.

The user provides:

* Username
* Password

After successful registration, the user can log in.

---

## 🔐 Login

Existing users can select **Login** and provide their credentials.

After successful authentication, they are redirected to the chatbot page.

---

## 💬 Chatting

After logging in:

1. Select a language.
2. Enter your message.
3. Click **Send**.
4. The application detects the input language.
5. The input is translated into English.
6. The GPT API generates a response.
7. If necessary, the Serper API performs a web search.
8. The response is translated back into the selected language.
9. The conversation is saved to the database.

---

## 📝 Chat History

Each user's conversations are stored separately.

The chat history displays:

```text
Timestamp
User message
Bot response
```

The latest conversations are displayed first.

---

## 👤 Account Management

Users can:

### Logout

Ends the current session and returns the user to the login page.

### Delete Account

Deletes the user's account and associated user information according to the database implementation.

---

## 🔒 Security

This project uses API credentials that must be kept private.

For production deployments, consider:

* Never committing `cred.json`
* Using environment variables or a secrets manager
* Hashing user passwords
* Validating user input
* Implementing API rate limiting
* Handling API failures securely
* Using a production-ready database
* Avoiding sensitive information in logs

---

## 🚀 Future Improvements

Possible improvements include:

* 🎤 Voice input
* 🔊 Text-to-speech
* 🌎 Additional language support
* 🌓 Dark/light mode
* 🗂️ Multiple conversations per user
* 🗑️ Individual chat deletion
* 📤 Chat export
* 📎 File/document upload
* 🔍 Chat history search
* 🧠 Conversation memory
* ⚡ Streaming GPT responses
* 🔐 Stronger authentication and password hashing
* ☁️ Cloud database support
* 🌐 Deployment to Streamlit Cloud or another hosting platform

---

## 📌 Example

### User asks:

```text
What is the latest cricket news?
```

The application can recognize this as a dynamic query and trigger the web search.

```text
User
  ↓
Language Detection
  ↓
Translation
  ↓
GPT
  ↓
Dynamic Query Detected
  ↓
Serper Web Search
  ↓
Top 3 Results
  ↓
Response Displayed
  ↓
Chat Saved
```

---

## 📄 License

This project can be released under the **MIT License**.

If you choose to use the MIT License, add a `LICENSE` file to the repository.

---

## ⭐ Contributing

Contributions and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Open a Pull Request.

---

## 📬 Feedback

If you find a bug or have suggestions for improving the chatbot, open an issue in the GitHub repository.
