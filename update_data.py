import yfinance as yf
from datetime import datetime

# [3호점: 나스닥 & 반도체 특화 리스트]
asset_pool = {
    'QQQ': 'Nasdaq 100', 'TQQQ': 'Nasdaq 3X Long', 'SQQQ': 'Nasdaq 3X Short',
    'SOXX': 'Semiconductor ETF', 'SOXL': 'Semi 3X Bull', 'NVDA': 'NVIDIA',
    'AMD': 'AMD', 'TSM': 'TSMC', 'ARM': 'ARM Holdings',
    'AAPL': 'Apple', 'MSFT': 'Microsoft', 'GOOGL': 'Alphabet'
}

def get_data():
    results = []
    now = datetime.now().strftime('%b %d, %Y %H:%M')
    for s, n in asset_pool.items():
        try:
            t = yf.Ticker(s)
            df = t.history(period='2d')
            if len(df) >= 2:
                cur = df['Close'].iloc[-1]
                prev = df['Close'].iloc[-2]
                pct = ((cur - prev) / prev) * 100
                results.append({'symbol': s, 'name': n, 'price': cur, 'pct': pct})
        except: continue
    
    html = f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NASDAQ TECH TERMINAL</title>
        <meta name="google-site-verification" content="38-xbGp8vqze8MfoAinJeJoI-maoeT_-qE9TXa7XekQ" />
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3030006828946894" crossorigin="anonymous"></script>
        <style>
            body {{ background: #000000; color: #00ff95; font-family: 'Courier New', monospace; padding: 20px; }}
            .container {{ max-width: 900px; margin: 0 auto; border: 1px solid #00ff95; padding: 20px; box-shadow: 0 0 15px #00ff95; }}
            .header {{ border-bottom: 2px double #00ff95; margin-bottom: 30px; padding-bottom: 10px; }}
            .ticker-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }}
            .card {{ border: 1px solid #004422; padding: 15px; background: #0a0a0a; }}
            .card:hover {{ background: #001100; border-color: #00ff95; }}
            .symbol {{ font-size: 1.2rem; font-weight: bold; color: #fff; }}
            .price {{ font-size: 1.5rem; margin: 10px 0; }}
            .up {{ color: #ff3333; }} .down {{ color: #33aaff; }}
            .footer {{ margin-top: 50px; font-size: 0.7rem; color: #006633; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>> NASDAQ_TECH_TERMINAL_V3.0</h1>
                <p>SYSTEM_STATUS: ONLINE | LAST_UPDATE: {now}</p>
            </div>
            <div class="ticker-grid">
    """
    for item in results:
        cls = "up" if item['pct'] >= 0 else "down"
        html += f"""
        <div class="card">
            <div class="symbol">{item['symbol']}</div>
            <div style="font-size:0.8rem; color:#888;">{item['name']}</div>
            <div class="price">${item['price']:,.2f}</div>
            <div class="{cls}">{"+" if item['pct']>=0 else ""}{item['pct']:.2f}%</div>
        </div>
        """
    html += """
            </div>
            <div class="footer">TERMINAL ACCESS AUTHORIZED // © 2026 NASDAQ TECH CORE</div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    with open('index.html', 'w', encoding='utf-8') as f: f.write(get_data())
    # 사이트맵 주소는 3호점용 주소로 나중에 자동 갱신됩니다.
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://tech.us-dividend-pro.com/</loc><priority>1.0</priority></url></urlset>'
    with open('sitemap.xml', 'w', encoding='utf-8') as f: f.write(sitemap)
