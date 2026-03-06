# 🏥 AI-Integrated Medical Chatbot

> A RAG-powered medical assistant that leverages semantic search over medical literature to deliver accurate, context-aware responses.

---

## 📖 Overview

This chatbot is built on a **Retrieval-Augmented Generation (RAG)** architecture, combining the power of large language models with a FAISS vector database for fast and accurate semantic search across medical knowledge bases.

You can expand its knowledge simply by adding more medical books to the `books/` directory — the more content you add, the richer and more accurate its responses become.

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Framework | `LangChain` |
| LLM (Chat Model) | `OpenAI-compatible` via Hugging Face |
| Embedding Model | `Sentence Transformers` via Hugging Face |
| Vector Database | `FAISS` |
| Environment Config | `python-dotenv` |
| Containerization | `Docker` |

---

## 🚀 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/) installed and running
- A Hugging Face API key (or compatible OpenAI key)

### Steps

**1. Clone the repository**
```````bash
git clone https://github.com/your-username/AI-Integrated-medical-chatbot.git
cd AI-Integrated-medical-chatbot
` ``

**2. Set up environment variables**
``````bash
cp .env.example .env
# Open .env and fill in your API keys
` ``

**3. Build the Docker image**
`````bash
docker compose up --build
` ``

**4. Start the container**
````bash
docker compose up
` ``

**5. Stop the container**
```bash
docker compose down
` ``

---

## 📚 Adding Medical Knowledge

Drop any medical PDF books or documents into the `books/` directory before building the image. The system will automatically index them into the FAISS database during startup.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source. See `LICENSE` for more information.
```

> **Note:** The ` ``` ` closing fences above have a space added to prevent rendering — remove the space when using in your actual file.