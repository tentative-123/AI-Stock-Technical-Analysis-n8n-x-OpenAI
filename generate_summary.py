import os
import openai

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(stock_list):
    prompt = f"以下是今天符合技術分析條件的選股清單：\n" + "\n".join(stock_list) + \
             "\n請以專業分析師的語氣，撰寫一段繁體中文的技術面分析，並包含操作建議。"

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ AI 分析失敗：{e}"
