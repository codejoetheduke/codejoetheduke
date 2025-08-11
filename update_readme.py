import requests
from datetime import datetime

username = "CodeJoe"
url = f"https://api.zindi.africa/v1/users/{username}"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

r = requests.get(url, headers=headers)
data = r.json()['data']

# Format stats
stats_md = f"""
**Zindi Stats (Updated {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC)**  

🏆 Rank: {data['rank']}  
⭐ Points: {data['points']}  
🥇 Best Rank: {data['best_rank']}  
🌍 Country: {data['country']}  

<img src="{data['avatar']}" alt="Zindi Avatar" width="100"/>
"""

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace between markers
start_marker = "<!--ZINDI_STATS_START-->"
end_marker = "<!--ZINDI_STATS_END-->"
before = readme.split(start_marker)[0]
after = readme.split(end_marker)[-1]
new_readme = f"{before}{start_marker}\n{stats_md}\n{end_marker}{after}"

# Write README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
