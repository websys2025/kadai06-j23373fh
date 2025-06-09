import requests

APP_ID = "dde9a961122c8f6febe8635db27473f025dc0d99"

def main():
    # 事業所・企業統計調査のstatsDataId
    stats_data_id = "0003143687"  # 平成29年事業所・企業統計調査

    # APIのURL
    url = "https://api.e-stat.go.jp/rest/3.0/app/getStatsData"

    # パラメータ設定
    params = {
        "appId": APP_ID,
        "statsDataId": stats_data_id,
        "metaGetFlg": "Y",      # メタ情報を取得
        "cntGetFlg": "N",
        "sectionHeaderFlg": "1",
        "startPosition": "1",
        "limit": "10"           # 取得件数制限（10件）
    }

    # APIリクエスト
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("API request failed:", response.status_code)
        return

    data = response.json()

    # 結果表示（簡易表示）
    if "GET_STATS_DATA" in data:
        stats_data = data["GET_STATS_DATA"]
        print("統計名:", stats_data.get("STATISTICAL_DATA", {}).get("STAT_NAME", "不明"))
        print("取得件数:", stats_data.get("RESULT", {}).get("COUNT", "不明"))
        # データ部を確認
        data_section = stats_data.get("STATISTICAL_DATA", {}).get("DATA_INF", {}).get("VALUE", [])
        if not data_section:
            print("データが見つかりません。")
            return

        print("\n最初の10件のデータサンプル：")
        for i, item in enumerate(data_section, start=1):
            label = item.get("@area")
            value = item.get("$")
            print(f"{i}: 地域コード={label}, 値={value}")

    else:
        print("統計データが見つかりません。")

if __name__ == "__main__":
    main()

