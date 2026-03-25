import os
from crewai import Crew, Task, Process
from dotenv import load_dotenv
from src.agents import repo_analyzer, content_improver, reviewer
from src.tools import fetch_readme, extract_keywords

load_dotenv()

def run_crew(github_url: str):

    # ─────────────────────────────────────────
    # Fetch README content first
    # ─────────────────────────────────────────
    print("\n📥 Fetching README from GitHub...\n")
    readme_content = fetch_readme(github_url)

    if "ERROR" in readme_content:
        print(readme_content)
        return

    keywords = extract_keywords(readme_content)

    # ─────────────────────────────────────────
    # Task 1: Analyze the README
    # ─────────────────────────────────────────
    task1 = Task(
        description=(
            f"Analyze the following GitHub README content carefully.\n\n"
            f"README CONTENT:\n{readme_content}\n\n"
            f"Extract and report:\n"
            f"1. Project title\n"
            f"2. What the project does (purpose)\n"
            f"3. Technologies and tools used\n"
            f"4. Existing sections in the README\n"
            f"5. Missing sections (e.g. installation, usage, license)\n"
            f"6. Overall clarity score out of 10\n"
        ),
        expected_output=(
            "A structured analysis report with: project title, purpose, "
            "technologies, existing sections, missing sections, "
            "and a clarity score out of 10."
        ),
        agent=repo_analyzer,
    )

    # ─────────────────────────────────────────
    # Task 2: Improve the content
    # ─────────────────────────────────────────
    task2 = Task(
        description=(
            f"Based on the README analysis, suggest improvements.\n\n"
            f"Keywords found: {keywords}\n\n"
            f"Please provide:\n"
            f"1. A better project title (more descriptive)\n"
            f"2. An improved project summary (3-4 sentences)\n"
            f"3. 8-10 relevant tags for discoverability\n"
            f"4. Recommended sections to add\n"
            f"5. One suggested visual improvement "
            f"(e.g. diagram, badge, screenshot)\n"
        ),
        expected_output=(
            "A content improvement report with: improved title, "
            "better summary, tags list, recommended sections, "
            "and visual improvement suggestion."
        ),
        agent=content_improver,
        context=[task1],
    )

    # ─────────────────────────────────────────
    # Task 3: Review and produce final report
    # ─────────────────────────────────────────
    task3 = Task(
        description=(
            "Review all the analysis and suggestions from the previous tasks.\n\n"
            "Check for:\n"
            "1. Are the suggestions specific and actionable?\n"
            "2. Are the tags relevant and accurate?\n"
            "3. Is the improved summary actually better?\n"
            "4. Any important missing recommendations?\n\n"
            "Then produce a FINAL REPORT with:\n"
            "- Final improved title\n"
            "- Final improved summary\n"
            "- Final tags list\n"
            "- Top 5 action items for the project author\n"
            "- Overall publication readiness score out of 10\n"
        ),
        expected_output=(
            "A clean final report with: final title, final summary, "
            "final tags, top 5 action items, and a publication "
            "readiness score out of 10."
        ),
        agent=reviewer,
        context=[task1, task2],
    )

    # ─────────────────────────────────────────
    # Assemble the Crew
    # ─────────────────────────────────────────
    crew = Crew(
        agents=[repo_analyzer, content_improver, reviewer],
        tasks=[task1, task2, task3],
        process=Process.sequential,
        verbose=True,
    )

    print("\n🚀 Starting multi-agent analysis...\n")
    result = crew.kickoff()

    print("\n" + "="*60)
    print("✅ FINAL REPORT")
    print("="*60)
    print(result)
    return result