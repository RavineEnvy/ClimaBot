# ClimaBot AI — REST API-Powered LLM Assistant

> A smart Python chatbot that consumes real-time weather data from a REST API and leverages Prompt Engineering with Llama 3 (via Groq) to deliver tailored, context-aware recommendations.

---

## About The Project

**ClimaBot** demonstrates how to bridge traditional software architectures and Large Language Models (LLMs). Instead of relying on static model knowledge, the application fetches live weather data from an external REST API (Open-Meteo) and dynamically injects this context into the prompt sent to the LLM.

### Concepts & Technologies Applied

- **Python 3.10+**
- **REST API Consumption:** HTTP requests using the `requests` library to consume Open-Meteo's public endpoint.
- **Context Injection (Grounding):** Enriching the LLM prompt with real-time, structured data (temperature and wind speed) to eliminate hallucinations.
- **Prompt Engineering:** System instructions (persona definition), strict response length constraints (maximum 3 sentences), and structured output guidance.
- **LLM Provider:** Integration with the `llama-3.3-70b-versatile` model using the official **Groq** SDK.
- **Security Best Practices:** Environment variable management via `python-dotenv` and API key protection using `.gitignore`.

---

# Made By:

| <img loading="lazy" src="https://avatars.githubusercontent.com/u/160347173?v=4" width="115"><br><sub><a href="https://github.com/RavineEnvy">Guilherme Freire</a></sub> |
| :---: |
