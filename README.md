🤖 AI Publication Assistant

A multi-agent AI system built with CrewAI that analyzes GitHub repositories and suggests improvements for better discoverability and publication readiness.

🎯 What It Does

Give it any GitHub repository URL and it will:

Analyze the README structure and content
Suggest better titles, summaries, and tags
Identify missing sections
Score publication readiness out of 10
🧠 Multi-Agent Architecture
Agent	Role
Repo Analyzer	Reads and analyzes the GitHub README
Content Improver	Suggests better titles, tags, and summaries
Reviewer / Critic	Reviews suggestions and produces final report
🛠️ Tools Used
GitHub README Fetcher — custom tool to fetch README via URL
Serper Search Tool — for additional context and information
OpenRouter LLM — powers all 3 agents (Llama/Mistral models)
⚙️ Orchestration

Built with CrewAI using a sequential process flow where each agent passes its output as context to the next agent.

🚀 Setup Instructions
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/publication-assistant.git
cd publication-assistant
2. Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
3. Install dependencies
pip install -r requirements.txt
4. Set up API keys

Create a .env file:

OPENROUTER_API_KEY=your-openrouter-api-key
SERPER_API_KEY=your-serper-api-key
5. Run the system
python main.py
📊 Sample Output

When given a GitHub URL, the system produces:

Improved project title
Better project summary
Relevant tags
Key improvement suggestions
Publication readiness score out of 10
🗂️ Project Structure
publication-assistant/
├── src/
│   ├── agents.py    # Agent definitions
│   ├── tools.py     # Custom tools
│   ├── tasks.py     # Task definitions
│   └── crew.py      # Crew and orchestration
├── main.py          # Entry point
├── requirements.txt # Dependencies
├── .env             # API keys (not pushed)
└── README.md        # This file
📦 Requirements
Python 3.10+
OpenRouter API key (free at https://openrouter.ai
)
Serper API key (free at https://serper.dev
)
