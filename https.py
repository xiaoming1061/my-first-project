import requests

# 1. 发请求，拿到 HTML
r = requests.get("https://cn.bing.com/search", params={"q": "猫"})

# 2. 写入本地文件
with open("bing_cat.html", "w", encoding="utf-8") as f:
    f.write(r.text)

print("✅ 已保存到 bing_cat.html")