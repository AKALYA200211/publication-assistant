import requests
from collections import Counter
import re

def fetch_readme(github_url: str) -> str:
    """
    Fetches the README content from a GitHub repository URL.
    Example input: https://github.com/username/repo-name
    """
    try:
        parts = github_url.rstrip("/").split("/")
        username = parts[-2]
        repo = parts[-1]

        raw_url = f"https://raw.githubusercontent.com/{username}/{repo}/main/README.md"
        response = requests.get(raw_url)

        if response.status_code != 200:
            raw_url = f"https://raw.githubusercontent.com/{username}/{repo}/master/README.md"
            response = requests.get(raw_url)

        if response.status_code == 200:
            return response.text[:3000]
        else:
            return "ERROR: Could not fetch README. Check the URL."

    except Exception as e:
        return f"ERROR: {str(e)}"


def extract_keywords(text: str) -> str:
    """
    Extracts simple keywords from text.
    """
    stopwords = set([
        "the", "a", "an", "and", "or", "but", "in", "on", "at",
        "to", "for", "of", "with", "is", "are", "was", "were",
        "this", "that", "it", "as", "be", "by", "from", "use",
        "using", "used", "can", "will", "have", "has", "you",
        "your", "we", "our", "they", "their", "how", "what",
        "which", "when", "where", "all", "also", "more", "than"
    ])

    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    filtered = [w for w in words if w not in stopwords]
    most_common = Counter(filtered).most_common(10)
    keywords = [word for word, count in most_common]

    return ", ".join(keywords)
