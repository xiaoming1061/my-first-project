import aiohttp    # 异步版 requests
import asyncio

async def get_weather(city, lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m",
        "timezone": "Asia/Shanghai"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as r:
            data = await r.json()
            print(data)
            temp = data["current"]["temperature_2m"]
            return f"{city}: {temp}℃"

async def main():
    # 三个城市同时查！
    results = await asyncio.gather(
        get_weather("北京", 39.9, 116.4),
        get_weather("上海", 31.2, 121.5),
        get_weather("广州", 23.1, 113.3),
    )
    for r in results:
        print(r)

asyncio.run(main())