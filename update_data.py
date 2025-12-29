import yfinance as yf
from datetime import datetime

# 종목별 섹터 분류 (유료 사이트처럼 보이게)
sectors = {
    "MARKET INDEX": ['QQQ', 'TQQQ', 'SQQQ', 'VOO', 'DIA', 'IWM'],
    "MAGNIFICENT 7": ['NVDA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA'],
    "SEMICONDUCTORS": ['SOXL', 'SOXX', 'AVGO', 'AMD', 'ARM', 'MU', 'TSM', 'ASML', 'INTC', 'AMAT', 'LRCX', 'QCOM'],
    "AI & SOFTWARE": ['PLTR', 'ORCL', 'ADBE', 'CRM', 'SNOW', 'NOW', 'WDAY', 'PALO'],
    "FINTECH & BEYOND": ['PYPL', 'SQ', 'V', 'MA', 'COIN', 'NFLX', 'UBER', 'SHOP', 'COST']
}

def get_data():
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    html_content = ""
    for sector_name, symbols in sectors.items():
        html_content += f'<h2 class="sector-title">{sector_name}</h2>'
        html_content += '<div class="grid">'
        
        for s in symbols:
            try:
                t = yf.Ticker(s)
                df = t.history(period='2d')
                if len(df) < 2: continue
                cur = df['Close'].iloc[-1]
                prev = df['Close'].iloc[-2]
                pct = ((cur - prev) / prev) * 100
                
                cls = "up" if pct >= 0 else "down"
                sign = "+" if pct >= 0 else ""
                
                html_content += f"""
                <div class="card">
                    <div class="card-header">
                        <span class="symbol">{s}</span>
                        <span class="pct {cls}">{sign}{pct:.2f}%</span>
                    </div>
                    <div class="price">${cur:,.2f}</div>
                </div>
                """
            except: continue
        html_content += '</div>'

    html = f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3030006828946894" crossorigin="anonymous"></script>
        <title>NASDAQ PREMIUM TERMINAL</title>
        <style>
            :root {{ --bg: #05070a; --card-bg: #11141b; --border: #1e222d; --text: #d1d4dc; --accent: #2962ff; }}
            body {{ background-color: var(--bg); color: var(--text); font-family: 'Trebuchet MS', sans-serif; margin: 0; padding: 20px; }}
            .container {{ max-width: 1200px; margin: 0 auto; }}
            header {{ border-bottom: 2px solid var(--accent); padding-bottom: 20px; margin-bottom: 40px; text-align: left; }}
            h1 {{ font-size: 38px; color: #ffffff; margin: 0; letter-spacing: -1px; }}
            .update-tag {{ font-size: 14px; color: #848e9c; margin-top: 5px; }}
            .sector-title {{ font-size: 18px; color: var(--accent); margin: 40px 0 15px 0; border-left: 4px solid var(--accent); padding-left: 10px; text-transform: uppercase; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
            .card {{ background: var(--card-bg); border: 1px solid var(--border); padding: 15px; border-radius: 6px; transition: all 0.2s ease; }}
            .card:hover {{ background: #1c212d; border-color: #3b72ff; transform: translateY(-2px); }}
            .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
            .symbol {{ font-weight: bold; font-size: 16px; color: #fff; }}
            .price {{ font-size: 24px; font-weight: 700; color: #ffffff; }}
            .pct {{ font-size: 13px; font-weight: bold; padding: 2px 6px; border-radius: 4px; }}
            .up {{ color: #00ffaa; background: rgba(0, 255, 170, 0.1); }}
            .down {{ color: #ff3b3b; background: rgba(255, 59, 59, 0.1); }}
            footer {{ margin-top: 80px; padding: 40px; text-align: center; font-size: 12px; color: #444; border-top: 1px solid var(--border); }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>TECH TERMINAL PRO</h1>
                <div class="update-tag">LIVE MARKET DATA • {now} KST</div>
            </header>
            {html_content}
            <footer>
                <p>Designed for professional traders. Data updated every hour.</p>
                <p>© 2025 US-DIVIDEND-PRO. All rights reserved.</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(get_data())
    
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://tech.us-dividend-pro.com/</loc><priority>1.0</priority></url></urlset>'
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
