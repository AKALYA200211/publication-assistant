from src.crew import run_crew

if __name__ == "__main__":
    print("="*60)
    print("🤖 AI Publication Assistant")
    print("="*60)

    github_url = input("\nEnter GitHub repo URL: ").strip()

    if not github_url:
        print("❌ No URL entered. Please try again.")
    else:
        run_crew(github_url)