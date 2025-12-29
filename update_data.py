if __name__ == "__main__":
    # 1. 인덱스 페이지 생성
    html_content = get_data()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 2. 사이트맵 생성 (구글이 긁어갈 수 있게 확실하게 작성)
    sitemap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://tech.us-dividend-pro.com/</loc>
        <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
        <priority>1.0</priority>
    </url>
</urlset>'''
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print("Files (index.html, sitemap.xml) created successfully!")
