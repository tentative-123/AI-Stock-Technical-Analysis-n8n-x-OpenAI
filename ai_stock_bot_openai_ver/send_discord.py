import os
import requests

def send_to_discord(content):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("❌ 未設定 DISCORD_WEBHOOK_URL")
        return

    payload = {
        "content": content
    }

    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print("✅ 成功發送到 Discord")
    else:
        print(f"❌ Discord 發送失敗：{response.status_code} {response.text}")
