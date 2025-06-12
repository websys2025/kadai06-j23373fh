import requests

# 東京の緯度・経度
latitude = 35.6895
longitude = 139.6917

# APIエンドポイントとパラメータ設定
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

# APIリクエストの送信
response = requests.get(url, params=params)

# レスポンスが成功したかチェック
if response.status_code == 200:
    data = response.json()
    weather = data.get("current_weather", {})
    
    # 結果の表示
    print("【東京の現在の天気情報】")
    print(f"気温: {weather.get('temperature')}℃")
    print(f"風速: {weather.get('windspeed')} m/s")
    print(f"天気コード: {weather.get('weathercode')}")
    print(f"観測時刻: {weather.get('time')}")
else:
    print("天気データの取得に失敗しました。ステータスコード:", response.status_code)
