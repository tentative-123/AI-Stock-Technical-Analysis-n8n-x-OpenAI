"""
StockBot 主入口：
1. 執行指定策略（預設 triangle5ma）
2. 整合財報、新聞、AI 分析模組
"""

from strategy_manager import get_strategy
from ai.summary_generator import generate_stock_summary
from fundamentals.fetch_fundamentals import get_fundamentals
from news.fetch_yahoo import fetch_news
from news.summarize_news import summarize_news

def run_daily(strategy_name: str = "triangle5ma", params: dict = {}):
    strategy = get_strategy(strategy_name)
    print(f"執行策略: {strategy.name}")
    stock_list = strategy.run(params=params)

    for stock in stock_list:
        print(f"分析 {stock['name']} ({stock['code']})")
        fund_summary = get_fundamentals(stock['code'])
        news_list = fetch_news(stock['code'])
        news_summary = summarize_news(news_list)
        ai_comment = generate_stock_summary(
            stock_code=stock['code'],
            strategy=strategy_name,
            key_points=[fund_summary, news_summary]
        )
        print("---")
        print(ai_comment)
