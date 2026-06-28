import requests
from datetime import datetime

# ---------- 1. 拼出 API 地址 ----------
url = "https://api.open-meteo.com/v1/forecast"

# 北京的经纬度
params = {
    "latitude": 39.9042,          # 纬度
    "longitude": 116.4074,        # 经度
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    #          温度(℃)         湿度(%)            风速(km/h)
    "timezone": "Asia/Shanghai",  # 时区
    "forecast_days": 1,           # 只要今天的
}

# ---------- 2. 发送请求 ----------
r = requests.get(url, params=params)

# ---------- 3. 把返回的 JSON 转成 Python 字典 ----------
data = r.json()

# ---------- 4. 从字典里把天气数据揪出来 ----------
current = data["current"]
temp = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind = current["wind_speed_10m"]
time = current["time"]

# ---------- 5. 打印出来 ----------
print(f"📍 北京天气")
print(f"🕐 更新时间：{time}")
print(f"🌡️  温度：{temp}℃")
print(f"💧 湿度：{humidity}%")
print(f"💨 风速：{wind} km/h")

# ---------- 6. 保存到文件（复习！）---------
today = datetime.now().strftime("%Y%m%d")
filename = f"weather_beijing_{today}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"北京天气 ({time})\n")
    f.write(f"温度：{temp}℃\n")
    f.write(f"湿度：{humidity}%\n")
    f.write(f"风速：{wind} km/h\n")

print(f"✅ 已保存到 {filename}")