import os
from strategy import run_strategy
from generate_summary import generate_summary
from send_discord import send_to_discord

if __name__ == "__main__":
    # 1. 執行選股策略
    result_lines = run_strategy()

    if len(result_lines) <= 1:
        send_to_discord("今日沒有符合條件的股票。")
    else:
        # 2. 用 OpenAI 做文字總結
        summary = generate_summary(result_lines[1:])  # 不含標題那一行

        # 3. 傳送到 Discord
        full_message = "**📊 今日選股結果：**\n" + "\n".join(result_lines) + "\n\n" + "**🤖 AI 分析：**\n" + summary
        send_to_discord(full_message)
