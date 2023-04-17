import argparse
from datetime import datetime, timedelta

import requests
from colorama import just_fix_windows_console, Fore, Style


just_fix_windows_console()

parser = argparse.ArgumentParser(description="Fetch most starred repositories from GitHub API")
parser.add_argument("-d", "--days", type=int, nargs="?", default=7, help="Number of days to retrieve repositories from (default: 7)")
parser.add_argument("-l", "--language", type=str, nargs="?", default=None, help="Filter repositories by language (default: None)")
args = parser.parse_args()

days = args.days
language = args.language

base_url = "https://api.github.com"

date_from = (datetime.now() - timedelta(days=days)).isoformat()

endpoint = f"{base_url}/search/repositories?q=created:>{date_from}"
if language:
    endpoint += f"+language:{language}"
endpoint += "&sort=stars&order=desc"

response = requests.get(endpoint)

if response.status_code == 200:

    data = response.json()

    incomplete_results = data["incomplete_results"]
    
    if incomplete_results:
        print("Incomplete results, try to provide a lower number of days")
    else:
        # Extract the top 10 most starred repositories from the response
        most_starred_repos = data['items'][:10]

        icons = {
            "Python": "🐍",
            "JavaScript": "🌐",
            "Java": "☕",
            "Ruby": "💎",
            "Go": "🔍",
            "C++": "⚙️",
            "C#": "🔢",
            "C": "🔢",
            "TypeScript": "📜",
            "Shell": "💻",
            "CSS": "🎨",
            "HTML": "📝",
            "PHP": "🔌",
            "Swift": "🚀",
            "Kotlin": "📱",
            "Rust": "🔒",
            "Vue": "🖼️",
            "Scala": "🧠",
            "Perl": "🐪",
            "Objective-C": "📱",
            "Jupyter Notebook": "🔬",
            "TeX": "📄",
            "PowerShell": "💻",
            "Lua": "🌙",
            "Haskell": "🔺",
            "MATLAB": "🔬",
            "R": "📊",
            "Dart": "🎯",
            "Vue.js": "🖼️",
            "CoffeeScript": "☕",
            "Elixir": "🔧",
            "Clojure": "🚿"
        }

        print(f"\n{Fore.YELLOW}Top 10 New and Trending Repositories in the Last {days} Days:{Style.RESET_ALL}\n")
        for i, repo in enumerate(most_starred_repos, start=1):
            description = repo['description'] if repo['description'] is not None else "Not specified"
            language = repo['language'] if repo['language'] is not None else "Not specified"
            print(f"{Fore.CYAN}#{i}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Repository Name:{Style.RESET_ALL} {repo['name']}")
            print(f"{Fore.GREEN}Repository Owner:{Style.RESET_ALL} {repo['owner']['login']}")
            print(f"{Fore.GREEN}Description:{Style.RESET_ALL} {description}")
            print(f"{Fore.YELLOW}Number of Stars:{Style.RESET_ALL} {repo['stargazers_count']}")
            print(f"{Fore.BLUE}Repository URL:{Style.RESET_ALL} {repo['html_url']}")
            print(f"{Fore.BLUE}Creation Date:{Style.RESET_ALL} {repo['created_at']}")
            print(f"{Fore.MAGENTA}Language:{Style.RESET_ALL} {icons.get(language, '')} {language}\n")
else:
    print("Failed to fetch new and trending repositories. Response code:", response.status_code)
