import yfinance as yf
from datetime import datetime

# 데이터 가져오기
asset_pool = {'QQQ': 'Nasdaq 100', 'TQQQ': 'Nasdaq 3X Long', 'NVDA': 'NVIDIA', 'SOXL': 'Semi 3X Bull'}

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
    
    html = f"<html><head><meta charset='utf-8'><meta name='google-site-verification' content='38-xbGp8vqze8MfoAinJeJoI-maoeT_-qE9TXa7XekQ' /></head><body>"
    for item in results:
        html += f"<div>{item['symbol']}: {item['price']:.2f} ({item['pct']:.2f}%)</div>"
    html += f"<p>Update: {now}</p></body></html>"
    return html

if __name__ == "__main__":
    # 1. index.html 생성
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(get_data())
    
    # 2. sitemap.xml 생성 (이게 없어서 아까 에러난 겁니다)
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://tech.us-dividend-pro.com/</loc>
        <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
        <priority>1.0</priority>
    </url>
</urlset>"""
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
