import yfinance as yf
from datetime import datetime

# 데이터 가져올 리스트
asset_pool = {
    'QQQ': 'Nasdaq 100', 'TQQQ': 'Nasdaq 3X Long', 
    'NVDA': 'NVIDIA', 'SOXL': 'Semi 3X Bull'
}

def get_data():
    results = []
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    for s, n in asset_pool.items():
        try:
            t = yf.Ticker(s)
            df = t.history(period='2d')
            cur = df['Close'].iloc[-1]
            prev = df['Close'].iloc[-2]
            pct = ((cur - prev) / prev) * 100
            results.append({'symbol': s, 'name': n, 'price': cur, 'pct': pct})
        except: continue
    
    # --- 여기서부터 HTML 시작 (애드센스 코드 포함) ---
    html = f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3030006828946894" crossorigin="anonymous"></script>
        
        <meta name="google-site-verification" content="38-xbGp8vqze8MfoAinJeJoI-maoeT_-qE9TXa7XekQ" />
        
        <title>NASDAQ TECH TERMINAL</title>
        <style>
            body {{ background: #000; color: #0f9; font-family: monospace; padding: 20px; }}
            .card {{ border: 1px solid #0f9; padding: 10px; margin-bottom: 10px; display: inline-block; width: 200px; }}
            .up {{ color: #f33; }} .down {{ color: #3af; }}
        </style>
    </head>
    <body>
        <h1>> NASDAQ_TECH_TERMINAL_V3</h1>
        <p>LAST_UPDATE: {now}</p>
        <hr>
    """
    for item in results:
        cls = "up" if item['pct'] >= 0 else "down"
        html += f"""
        <div class="card">
            <b>{item['symbol']}</b><br>
            Price: ${item['price']:,.2f}<br>
            Change: <span class="{cls}">{item['pct']:.2f}%</span>
        </div>
        """
    html += """
        <hr>
        <p style="font-size:12px; color:#555;">본 사이트는 실시간 기술주 데이터를 제공합니다.</p>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    # 1. index.html 생성
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(get_data())
    
    # 2. sitemap.xml 생성
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>http://tech.us-dividend-pro.com/</loc><priority>1.0</priority></url>
</urlset>'''
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
