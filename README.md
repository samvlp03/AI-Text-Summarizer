# Text Summarizer App

The **Text Summarizer App** is a full-stack web application that allows users to generate concise summaries of large text passages using advanced AI models. The project is built with a Django REST Framework backend and a React frontend, and integrates with the Ollama platform to run the Llama 3.2 1B model locally for text summarization.

## Key Features

- **AI-Powered Summarization:** Generate short, medium, or long summaries from any input text using the Llama 3.2 1B model via Ollama.
- **User Authentication:** Secure registration, login, and JWT-based authentication for personalized summary history.
- **Summary Management:** View, favorite, and manage all your generated summaries in your account.
- **Export Options:** Download summaries in PDF, Word (.docx), or JSON formats.
- **Customizable Output:** Choose summary length, tonality, and advanced generation parameters.
- **Modern UI:** Responsive React frontend with dark mode and Material UI components.

## How It Works

1. **User submits text** via the frontend and selects summary options.
2. **Frontend sends a request** to the Django REST API.
3. **Backend processes the request** and communicates with the Ollama server running the Llama 3.2 1B model.
4. **AI model generates a summary** which is returned to the backend.
5. **Backend saves the summary** to the database and returns it to the frontend.
6. **User can view, favorite, or export** their summaries from their account dashboard.

## Project Structure

- `summarizer_backend/` — Django REST Framework backend (API, models, authentication, Ollama integration)
- `summarizer-frontend/` — React frontend (UI, authentication, summary management)
- `.env` — Environment variables for backend configuration

## Technologies Used

- **Backend:** Django, Django REST Framework, SimpleJWT, Ollama Python client
- **Frontend:** React, Material UI, Axios
- **AI Model:** Llama 3.2 1B via Ollama
- **Export:** python-docx, pdfkit

## Typical Use Case

1. Register or log in to your account.
2. Paste or type the text you want to summarize.
3. Choose summary length and style.
4. Click "Summarize" to generate a summary.
5. View your summary, mark as favorite, or export it in your preferred format.

## Requirements

- Python 3.10+
- Node.js 18+
- Ollama installed and running locally with the Llama 3.2 1B model

## Getting Started

See the full setup instructions in this README for backend and frontend installation, environment configuration, and running the app locally.

---

This project demonstrates how to combine modern AI models with robust web technologies to deliver practical, user-friendly NLP
