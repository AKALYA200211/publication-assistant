from crewai import LLM, Agent
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="openrouter/meta-llama/llama-3.1-8b-instruct",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7
)
# ─────────────────────────────────────────
# Agent 1: Repo Analyzer
# ─────────────────────────────────────────
repo_analyzer = Agent(
    role="GitHub Repository Analyzer",
    goal=(
        "Fetch and analyze the README of a GitHub repository. "
        "Extract the project title, description, purpose, "
        "technologies used, and identify missing sections."
    ),
    backstory=(
        "You are an expert technical analyst who specializes "
        "in reading GitHub repositories. You have a sharp eye "
        "for what makes a README clear and complete."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# ─────────────────────────────────────────
# Agent 2: Content Improver
# ─────────────────────────────────────────
content_improver = Agent(
    role="AI Content Improvement Specialist",
    goal=(
        "Using the analyzed README, suggest a better project title, "
        "improved summary, relevant tags, and structural improvements."
    ),
    backstory=(
        "You are a technical content writer with deep experience "
        "in AI/ML projects. You know how to make a project stand "
        "out on platforms like GitHub and Ready Tensor."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# ─────────────────────────────────────────
# Agent 3: Reviewer / Critic
# ─────────────────────────────────────────
reviewer = Agent(
    role="Technical Publication Reviewer",
    goal=(
        "Review the improvement suggestions and verify quality. "
        "Flag anything vague or missing. Produce a final clean report."
    ),
    backstory=(
        "You are a strict but fair technical reviewer who has evaluated "
        "hundreds of AI project publications. You ensure every suggestion "
        "is specific and genuinely useful to the project author."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)