# **README.md**

```markdown
# AI Multi-Agent Demo  
A teaching & workshop project demonstrating how **multiple AI agents** can work together in a pipeline:

1. **StockDataAgent** – fetches S&P 500 market data  
2. **NewsAgent** – retrieves or accepts a news article  
3. **SummaryAgent** – summarizes the article  
4. **SentimentAgent** – analyzes summary sentiment  
5. **DecisionAgent** – produces a *toy* investment suggestion  

This project is designed for educational purposes to show the internal structure of AI systems—not for financial use.

---

## 🚀 Features

- **Multi-agent architecture** (each agent is an isolated class)  
- **Clean and production-style Python modules** with docstrings and type hints  
- **Utility layer** for shared functionality  
- **Jupyter Notebook** that walks through the pipeline step by step  
- **`uv`-based Python project** for fast dependency installation and reproducibility  
- **Optional LLM support** for improved summarization  

---

## 📦 Project Structure

```

ai-multi-agent-demo/
├─ ai_agents/
│  ├─ **init**.py
│  ├─ utils.py
│  ├─ stock_agent.py
│  ├─ news_agent.py
│  ├─ summary_agent.py
│  ├─ sentiment_agent.py
│  └─ decision_agent.py
├─ ai_multi_agent_demo_notebook.ipynb
├─ pyproject.toml
└─ README.md

````

---

## 🛠 Installation (using `uv`)

This project uses **uv** (https://github.com/astral-sh/uv), a fast Python package manager and runner.

### Install dependencies:

```bash
uv sync
````

### Optional: install LLM support (OpenAI)

```bash
uv add openai --extra llm
```

---

## ▶️ Running the Demo

### Launch the Jupyter Notebook:

```bash
uv run notebook
```

Then open `ai_multi_agent_demo_notebook.ipynb`.

---

## 🧠 How the Pipeline Works

### 1. StockDataAgent

Fetches recent S&P 500 data using `yfinance` and computes a simple recent return.

### 2. NewsAgent

Gets a news article either:

* From a URL, or
* Via manual copy-paste text (recommended during workshops)

### 3. SummaryAgent

Summarizes the article using a simple extractive method (first N sentences).
You can replace this with an LLM for more advanced summarization.

### 4. SentimentAgent

Runs sentiment analysis using a HuggingFace Transformers model.
Classifies into **POSITIVE**, **NEGATIVE**, or **NEUTRAL**.

### 5. DecisionAgent

Produces a *toy* investment suggestion such as:

* “Consider increasing exposure (buy bias)”
* “Consider reducing exposure (sell bias)”
* “No clear signal (neutral/hold)”

This step is **NOT financial advice**—it's only for demonstrating multi-agent AI.

---

## 📁 Notebook Walkthrough

The included notebook demonstrates:

* How each agent works internally
* How they pass data to each other
* How the whole pipeline creates an interpretable decision

Each code cell is preceded by a Markdown explanation to help students follow along.

---

## 🧩 Extending the Project

You can easily add:

* More agents (e.g., risk assessment agent, alternative news sources)
* LLM-based summarization
* LLM-based reasoning for investment suggestions
* Visualizations of sentiment vs. market movement
* Agent-to-agent messaging frameworks (e.g., LangGraph style)

If you want help implementing any of these, just ask!

---

## ⚠️ Disclaimer

This project is **strictly educational**.
It is **not** intended for real investment decisions or financial advice.

---

## 📄 License

MIT License (or add your preferred license)