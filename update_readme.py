import os
import requests
from datetime import datetime
from PIL import Image, ImageDraw
from io import BytesIO

username = "CodeJoe"
url = f"https://api.zindi.africa/v1/users/{username}"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

# Fetch user data
r = requests.get(url, headers=headers)
data = r.json()['data']

# Download avatar
avatar_url = data['big_avatar']
avatar_res = requests.get(avatar_url, headers=headers)
os.makedirs("assets", exist_ok=True)
avatar_path = "assets/avatar.png"

# Round avatar
im = Image.open(BytesIO(avatar_res.content)).convert("RGBA")
mask = Image.new("L", im.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, im.size[0], im.size[1]), fill=255)
im.putalpha(mask)
im.save(avatar_path)

# Format stats in a table (avatar left, stats right)
stats_md = f"""
<div align="center">

## 📈 My Live Zindi Stats

<table>
<tr>
<td width="250" align="center">
  <img src="{avatar_path}" width="200"/>
</td>
<td align="center">

![Rank](https://img.shields.io/badge/🏆%20Rank-{data['rank']}-blueviolet?style=for-the-badge)<br>
![Points](https://img.shields.io/badge/⭐%20Points-{data['points']}-ff69b4?style=for-the-badge)<br>
![Best Rank](https://img.shields.io/badge/🥇%20Best%20Rank-{data['best_rank']}-brightgreen?style=for-the-badge)<br>
![Country](https://img.shields.io/badge/🌍%20Country-{data['country'].replace(' ', '%20')}-orange?style=for-the-badge)<br><br>

<!-- 🏅 Medals -->
<div style="display:flex;justify-content:center;gap:25px;margin-top:15px;">
  <img src="https://img.shields.io/badge/🥇%20Gold-{data['user_medals_summary_gold_count']}-FFD700?style=for-the-badge" height="60"/>
  <img src="https://img.shields.io/badge/🥈%20Silver-{data['user_medals_summary_silver_count']}-C0C0C0?style=for-the-badge" height="60"/>
  <img src="https://img.shields.io/badge/🥉%20Bronze-{data['user_medals_summary_bronze_count']}-CD7F32?style=for-the-badge" height="60"/>
</div>

</td>
</tr>
</table>

<br>

_Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC_

</div>
"""

# Update README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start_marker = "<!--ZINDI_STATS_START-->"
end_marker = "<!--ZINDI_STATS_END-->"
before = readme.split(start_marker)[0]
after = readme.split(end_marker)[-1]
new_readme = f"{before}{start_marker}\n{stats_md}\n{end_marker}{after}"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
