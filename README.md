# StockBot 系統架構

這是一套模組化的 AI 股票分析與選股機器人系統，支援每日自動推播與使用者互動查詢。

## 📁 資料夾結構總覽

- `main.py`: 系統主入口（每日排程或測試啟動）
- `strategies/`: 各種策略模組，繼承 `BaseStrategy`
- `strategy_manager.py`: 策略註冊與統一管理
- `ai/`: 使用 GPT 進行財報與新聞分析摘要
- `fundamentals/`: 擷取基本面資料來源
- `news/`: 擷取新聞與摘要模組
- `discord_bot/`: 未來支援 Slash 指令與互動
- `database/`: SQLite or Google Sheet 紀錄每日推播
- `backtest/`: 基於紀錄進行策略績效回測
- `config.py`: 統一讀取 `.env` 設定檔

## 🧩 開發協作建議

請使用 `Cursor` 或 `Copilot` 開發，每個模組皆含 type hints 與 docstring，便於自動補全與重構。
