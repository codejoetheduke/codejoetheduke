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
<div align="center">

## 📈 My Live Zindi Stats

![Rank](https://img.shields.io/badge/🏆%20Rank-{data['rank']}-blueviolet?style=for-the-badge)
![Points](https://img.shields.io/badge/⭐%20Points-{data['points']}-ff69b4?style=for-the-badge)
![Best Rank](https://img.shields.io/badge/🥇%20Best%20Rank-{data['best_rank']}-brightgreen?style=for-the-badge)
![Country](https://img.shields.io/badge/🌍%20Country-{data['country'].replace(' ', '%20')}-orange?style=for-the-badge)

<br><br>

<!-- 🏅 Medals (Bigger & Centered) -->
<div style="display:flex;justify-content:center;gap:20px;margin-top:10px;">
  
<img src="https://img.shields.io/badge/🥇%20Gold-{data['user_medals_summary_gold_count']}-FFD700?style=for-the-badge&logo=googlechrome&logoColor=black&logoWidth=40" height="60"/>
<img src="https://img.shields.io/badge/🥈%20Silver-{data['user_medals_summary_silver_count']}-C0C0C0?style=for-the-badge&logo=googlechrome&logoColor=black&logoWidth=40" height="60"/>
<img src="https://img.shields.io/badge/🥉%20Bronze-{data['user_medals_summary_bronze_count']}-CD7F32?style=for-the-badge&logo=googlechrome&logoColor=black&logoWidth=40" height="60"/>

</div>

<br>

<img src="{data['big_avatar']}" width="360" style="border-radius:50%;margin-top:10px;"/>

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
