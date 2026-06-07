"""
Publish 3 PM blog articles to Medium via the Medium API.
Usage:
  1. Generate an integration token at medium.com/me/settings → Security → Integration tokens
  2. Run:  python3 publish_to_medium.py --token YOUR_TOKEN
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Installing dependencies...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4"], check=True)
    import requests
    from bs4 import BeautifulSoup


# ── Articles to publish ─────────────────────────────────────────────────
PORTFOLIO_ROOT = Path(__file__).parent.parent / "work"

ARTICLES = [
    {
        "file": PORTFOLIO_ROOT / "blog-wrong-metric.html",
        "title": "The Wrong Metric Cost Us 6 Months",
        "subtitle": "How measuring the wrong KYC number sent our product team in the wrong direction — and what switching metrics changed about the entire roadmap.",
        "tags": ["Product Management", "Metrics", "Fintech", "KYC", "Product Strategy"],
        "canonical_url": "https://shraddhasingh.dev/work/blog-wrong-metric.html",
    },
    {
        "file": PORTFOLIO_ROOT / "blog-genai-feature-first.html",
        "title": "Which GenAI Feature Do You Build First?",
        "subtitle": "The client wanted AI in the contact center. The most-requested feature had the highest failure cost. Here's the risk-adjusted framework I used to sequence 10+ GenAI features.",
        "tags": ["AI Product Management", "GenAI", "Product Strategy", "Healthcare", "Fintech"],
        "canonical_url": "https://shraddhasingh.dev/work/blog-genai-feature-first.html",
    },
    {
        "file": PORTFOLIO_ROOT / "blog-ai-adoption.html",
        "title": "Why Your Users Won't Adopt Your AI Feature",
        "subtitle": "The most technically impressive AI feature we shipped had the lowest adoption. The fix wasn't a better model — it was one design decision that changed everything.",
        "tags": ["AI Product Management", "User Adoption", "UX", "Product Design", "AI"],
        "canonical_url": "https://shraddhasingh.dev/work/blog-ai-adoption.html",
    },
]


# ── HTML extraction helpers ──────────────────────────────────────────────

def extract_article_html(html_path: Path) -> str:
    """Extract only the readable article body from portfolio HTML files."""
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    # Remove nav, footer, related sections, script, style
    for tag in soup.find_all(["nav", "footer", "script", "style"]):
        tag.decompose()
    for el in soup.find_all(class_=re.compile(r"related|nav-|\.nav")):
        el.decompose()

    # Try to find article body div
    body = (
        soup.find("div", class_="article-body")
        or soup.find("div", class_="content")
        or soup.find("main")
        or soup.find("body")
    )

    if not body:
        return str(soup)

    # Clean up internal links → absolute URLs
    for a in body.find_all("a", href=True):
        href = a["href"]
        if href.startswith("../"):
            a["href"] = "https://shraddhasingh.dev/" + href.replace("../", "")
        elif href.startswith("work/") or href.startswith("./"):
            a["href"] = "https://shraddhasingh.dev/" + href.lstrip("./")

    # Remove author block (personal info already in Medium profile)
    for el in body.find_all(class_="author-block"):
        el.decompose()

    return str(body)


# ── Medium API helpers ────────────────────────────────────────────────────

MEDIUM_API = "https://api.medium.com/v1"


def get_user_id(token: str) -> str:
    resp = requests.get(
        f"{MEDIUM_API}/me",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        timeout=15,
    )
    if resp.status_code != 200:
        print(f"[ERROR] Could not authenticate — HTTP {resp.status_code}")
        print(resp.text)
        sys.exit(1)
    data = resp.json()["data"]
    print(f"[OK] Authenticated as: {data['name']} (@{data['username']})")
    return data["id"]


def publish_post(token: str, user_id: str, article: dict, draft: bool = True) -> dict:
    html_content = extract_article_html(article["file"])
    payload = {
        "title": article["title"],
        "contentFormat": "html",
        "content": f"<h4><em>{article['subtitle']}</em></h4>\n\n{html_content}",
        "tags": article["tags"][:5],  # Medium allows max 5 tags
        "publishStatus": "draft" if draft else "public",
        "canonicalUrl": article.get("canonical_url", ""),
        "notifyFollowers": not draft,
    }
    resp = requests.post(
        f"{MEDIUM_API}/users/{user_id}/posts",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json=payload,
        timeout=30,
    )
    if resp.status_code not in (200, 201):
        print(f"  [ERROR] HTTP {resp.status_code}: {resp.text[:300]}")
        return {}
    return resp.json().get("data", {})


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Publish PM blog posts to Medium")
    parser.add_argument("--token", required=True, help="Medium integration token")
    parser.add_argument("--publish", action="store_true",
                        help="Publish publicly (default: save as draft for review first)")
    parser.add_argument("--article", type=int, choices=[1, 2, 3],
                        help="Publish only article 1, 2, or 3 (default: all three)")
    args = parser.parse_args()

    draft = not args.publish
    status = "DRAFT" if draft else "PUBLIC"
    print(f"\nMedium Publisher — posting as {status}\n{'─'*45}")

    user_id = get_user_id(args.token)

    articles = [ARTICLES[args.article - 1]] if args.article else ARTICLES

    for i, article in enumerate(articles, 1):
        print(f"\n[{i}/{len(articles)}] Publishing: {article['title']}")
        if not article["file"].exists():
            print(f"  [SKIP] File not found: {article['file']}")
            continue

        result = publish_post(args.token, user_id, article, draft=draft)
        if result:
            print(f"  [OK] {status}: {result.get('url', 'URL not returned')}")
            print(f"       ID: {result.get('id')}")
        else:
            print("  [FAIL] Post not created — check error above")

    print(f"\n{'─'*45}")
    if draft:
        print("All posts saved as DRAFTS. Review at medium.com/me/stories/drafts")
        print("Re-run with --publish to go live immediately.")
    else:
        print("All posts published publicly.")


if __name__ == "__main__":
    main()
