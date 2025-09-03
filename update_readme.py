import os
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

def make_medal_svg(label, count, color, emoji):
    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="0 0 200 200">
      <circle cx="100" cy="100" r="90" fill="{color}" stroke="black" stroke-width="4"/>
      <text x="100" y="95" font-size="60" text-anchor="middle" dominant-baseline="middle">{emoji}</text>
      <text x="100" y="165" font-size="40" text-anchor="middle" fill="white" font-weight="bold">{count}</text>
      <title>{label}: {count}</title>
    </svg>
    """

# Generate medal SVGs
gold_svg = make_medal_svg("Gold", data['user_medals_summary_gold_count'], "#FFD700", "🥇")
silver_svg = make_medal_svg("Silver", data['user_medals_summary_silver_count'], "#C0C0C0", "🥈")
bronze_svg = make_medal_svg("Bronze", data['user_medals_summary_bronze_count'], "#CD7F32", "🥉")

# Save them into medals/ folder
os.makedirs("medals", exist_ok=True)
with open("medals/gold.svg", "w", encoding="utf-8") as f: f.write(gold_svg)
with open("medals/silver.svg", "w", encoding="utf-8") as f: f.write(silver_svg)
with open("medals/bronze.svg", "w", encoding="utf-8") as f: f.write(bronze_svg)

# Format stats
stats_md = f"""
<div align="center">

## 📈 My Live Zindi Stats

![Rank](https://img.shields.io/badge/🏆%20Rank-{data['rank']}-blueviolet?style=for-the-badge)
![Points](https://img.shields.io/badge/⭐%20Points-{data['points']}-ff69b4?style=for-the-badge)
![Best Rank](https://img.shields.io/badge/🥇%20Best%20Rank-{data['best_rank']}-brightgreen?style=for-the-badge)
![Country](https://img.shields.io/badge/🌍%20Country-{data['country'].replace(' ', '%20')}-orange?style=for-the-badge)

<!-- 🏅 Big Medals -->
<div style="display:flex;justify-content:center;gap:40px;margin-top:20px;">
<img src="medals/gold.svg" width="160"/>
<img src="medals/silver.svg" width="160"/>
<img src="medals/bronze.svg" width="160"/>
</div>

<br>

<img src="{data['avatar']}" width="300" style="border-radius:50%;margin-top:10px;"/>

_Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC_

</div>
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
