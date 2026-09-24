"""
GitHub Repo Reader — for Bradley to check detailed project context when MEMORY.md says "check GitHub"

Rule: MEMORY.md = high-level truth, GitHub = detailed context
This tool fetches README + file list + recent commits from user's repos (BirOvoz, Prepl, CASMI)

Usage in OpenHands / Open WebUI as tool
"""

import requests
import os
from typing import Dict, List

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")  # optional, for private repos, add to .env

def github_fetch_readme(owner: str, repo: str, branch: str = "main") -> str:
    """Fetch README.md from GitHub repo"""
    # Try main, then master
    for b in [branch, "master", "main"]:
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/{b}/README.md"
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                return r.text[:8000]  # limit to 8k chars to not bloat context
        except Exception as e:
            print(f"Fetch failed {url}: {e}")
    return "README not found"

def github_list_files(owner: str, repo: str) -> List[str]:
    """List top-level files via GitHub API"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return [f"{item['name']} ({item['type']})" for item in data[:30]]
    except Exception as e:
        print(f"List files failed: {e}")
    return []

def github_recent_commits(owner: str, repo: str, n: int = 5) -> List[str]:
    """Get recent commit messages to understand current state vs old README"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page={n}"
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            commits = r.json()
            return [f"{c['commit']['message'][:100]} — {c['commit']['author']['date'][:10]}" for c in commits]
    except Exception as e:
        print(f"Commits fetch failed: {e}")
    return []

def get_project_context(owner: str, repo: str) -> Dict:
    """
    Main function for Bradley: get high-level context from GitHub repo
    Use this when MEMORY.md says "check GitHub repository for detailed context"
    """
    print(f"Fetching GitHub context for {owner}/{repo}...")
    readme = github_fetch_readme(owner, repo)
    files = github_list_files(owner, repo)
    commits = github_recent_commits(owner, repo)
    
    context = f"""
# GitHub Context: {owner}/{repo}

## README (first 8k chars):
{readme[:4000]}

## Top files:
{', '.join(files[:20])}

## Recent commits (current truth vs old README):
{chr(10).join(commits)}

## Note:
This is detailed context from GitHub. MEMORY.md is high-level truth. If GitHub has old code / abandoned branches, prefer MEMORY.md for current status.
"""
    return {
        "readme": readme,
        "files": files,
        "commits": commits,
        "context": context
    }

# Example for OpenHands tool wrapper
def check_github_repo_for_project(
    project_name: str,  # BirOvoz, Prepl, CASMI2026
    owner: str = "ability-spec",
    repo: str = None
) -> str:
    """
    Tool for Bradley: When user asks about BirOvoz/Prepl/CASMI and MEMORY.md says check GitHub,
    use this to fetch real implementation.
    """
    repo_map = {
        "BirOvoz": "BirOvoz",
        "Prepl": "Prepl",
        "CASMI2026": "CASMI2026",
        "Bradley-AI": "Bradley-AI"
    }
    if repo is None:
        repo = repo_map.get(project_name, project_name)
    
    ctx = get_project_context(owner, repo)
    return ctx["context"]

if __name__ == "__main__":
    # Test
    print(get_project_context("ability-spec", "Bradley-AI")["context"][:2000])
