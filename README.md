# 🤖 AI Publication Assistant

A multi-agent AI system built with CrewAI that analyzes GitHub 
repositories and suggests improvements for better discoverability 
and publication readiness.

## 🎯 What It Does

Give it any GitHub repository URL and it will:
- Analyze the README structure and content
- Suggest better titles, summaries, and tags
- Identify missing sections
- Score publication readiness out of 10

## 🧠 Multi-Agent Architecture

| Agent | Role |
|-------|------|
| Repo Analyzer | Reads and analyzes the GitHub README |
| Content Improver | Suggests better titles, tags, and summaries |
| Reviewer / Critic | Reviews suggestions and produces final report |

## 🛠️ Tools Used

- **GitHub README Fetcher** — custom tool to fetch README via URL
- **Keyword Extractor** — custom tool to extract key terms
- **Groq LLM** — powers all 3 agents (llama-3.3-70b-versatile)

## ⚙️ Orchestration

Built with **CrewAI** using sequential process flow where each 
agent passes its output as context to the next agent.

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/publication-assistant.git
cd publication-assistant
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install crewai crewai-tools groq langchain-groq requests python-dotenv
```

### 4. Set up API keys
Create a `.env` file:
```
GROQ_API_KEY=your-groq-api-key
SERPER_API_KEY=your-serper-api-key
```

### 5. Run the system
```bash
python main.py
```

## 📊 Sample Output

When given a GitHub URL the system produces:
- Improved project title
- Better project summary
- 8-10 relevant tags
- Top 5 action items
- Publication readiness score out of 10

## 🗂️ Project Structure
```
publication-assistant/
├── src/
│   ├── agents.py    # Agent definitions
│   ├── tools.py     # Custom tools
│   └── crew.py      # Crew and task setup
├── main.py          # Entry point
├── requirements.txt # Dependencies
└── README.md        # This file
```

## 📦 Requirements

- Python 3.10+
- Groq API key (free at console.groq.com)
- Serper API key (free at serper.dev)