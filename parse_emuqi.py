#!/usr/bin/env python3
"""Parse Zyrosite SSR'd HTML to extract images, hero, text, layout structure."""
import re, html, os, sys
from pathlib import Path

PAGES = [
    ("首页 (Homepage)", "/tmp/emuqi_home.html", "http://www.emuqi.com/"),
    ("About - Manufacturer", "/tmp/emuqi_01.html", "http://www.emuqi.com/about-functional-ceramic-ball-water-media-manufacturer"),
    ("Product - Ceramic Materials", "/tmp/emuqi_02.html", "http://www.emuqi.com/product-functional-ceramic-materials"),
    ("Hydrogen Generate Ceramic Ball", "/tmp/emuqi_03.html", "http://www.emuqi.com/hydrogen-generate-ceramic-ball"),
    ("MACA KDF Antibacterial Ball", "/tmp/emuqi_04.html", "http://www.emuqi.com/maca-kdf-antibacterial-ceramic-ball"),
    ("MPH Condensate Neutralizer", "/tmp/emuqi_05.html", "http://www.emuqi.com/mph-condensate-neutralizer"),
    ("Hydrogen Health Application", "/tmp/emuqi_06.html", "http://www.emuqi.com/hydrogen-health-application"),
    ("Hydrogen Water Bottle", "/tmp/emuqi_07.html", "http://www.emuqi.com/hydrogen-water-bottle-or-hydrogen-health"),
    ("Hydrogen Alkaline Water Sachet", "/tmp/emuqi_08.html", "http://www.emuqi.com/hydrogen-health-hydrogen-alkaline-water-sachet"),
    ("Ceramic Hydrogen Tablet", "/tmp/emuqi_09.html", "http://www.emuqi.com/hydrogen-healthceramic-hydrogen-tablet"),
    ("Hydrogen Water Filter Cartridge", "/tmp/emuqi_10.html", "http://www.emuqi.com/hydrogen-healthhydrogen-water-filter-cartridge"),
    ("Hydrogen Foot Bath Tablet", "/tmp/emuqi_11.html", "http://www.emuqi.com/hydrogen-healthhydrogen-foot-bath-tablet"),
    ("Solutions - Hydrogen Agriculture", "/tmp/emuqi_12.html", "http://www.emuqi.com/solutions-hydrogen-agriculture"),
    ("Blog List", "/tmp/emuqi_13.html", "http://www.emuqi.com/blog-list-hydrogen-health"),
    ("Contact", "/tmp/emuqi_14.html", "http://www.emuqi.com/contact-mqtech-hydrogen-health"),
]

SITE_ID = "A0x1OjZW32F81Eg3"

def clean_asset_url(raw):
    u = re.sub(r'/cdn-cgi/image/[^/]+/', '/', raw)
    u = re.sub(r'\s+\d+w,?', '', u)
    u = u.split('?')[0]
    # Truncate at any HTML entity or escaped JSON artifact
    for stopper in ['&', '\\', '&quot;', '",']:
        idx = u.find(stopper)
        if idx > 0:
            u = u[:idx]
    u = u.strip().rstrip(',').rstrip(';')
    return u

def extract_all_image_paths(text):
    # Match full URL up to whitespace, quotes, angle brackets, or backslash
    pattern = r'(?:https?:)?//assets\.zyrosite\.com/[^\s"\\<>]+'
    raw_matches = re.findall(pattern, text)
    clean = set()
    for m in raw_matches:
        c = clean_asset_url(m)
        c = c.split(' ')[0]
        if c.startswith('//'):
            c = 'https:' + c
        # Filter out non-image files
        if c.endswith('.txt') or c.endswith('.css') or c.endswith('.js'):
            continue
        # Must contain the site ID and have a valid image extension
        if SITE_ID in c and re.search(r'\.(png|jpg|jpeg|gif|webp|svg)$', c, re.I):
            clean.add(c)
    return sorted(clean)

def extract_gridpro_backgrounds(html_text):
    """Find all image path references with their context (alt, type).
    Handles both raw JSON and HTML-entity-escaped JSON (&quot;)."""
    results = []
    # Match both "path":[0,"..."] and &quot;path&quot;:[0,&quot;...&quot;]
    for m in re.finditer(r'(?:&quot;path&quot;:\[0,&quot;|"path":\[0,")([^"&]+)', html_text):
        start = max(0, m.start() - 800)
        context = html_text[start:m.start()]
        path = m.group(1)
        # Find alt (both forms)
        alt_match = re.findall(r'(?:&quot;alt&quot;:\[0,&quot;|"alt":\[0,")([^"&]*)', context)
        alt = alt_match[-1] if alt_match else ""
        type_match = re.findall(r'(?:&quot;type&quot;:\[0,&quot;|"type":\[0,")(\w+)', context)
        elem_type = type_match[-1] if type_match else ""
        results.append({"path": path, "alt": alt, "type": elem_type})
    return results

def extract_text_content_near_top(html_text, max_items=40):
    results = []
    seen = set()
    # Method 1: Real HTML tags in SSR'd content
    for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        for hm in re.finditer(rf'<{tag}[^>]*>(.*?)</{tag}>', html_text, re.S):
            text = re.sub(r'<[^>]+>', '', hm.group(1)).strip()
            if text and text not in seen:
                seen.add(text)
                results.append((tag.upper(), text))
    # Method 2: Paragraphs (including <strong> tagged hero text)
    for pm in re.finditer(r'<p[^>]*>(.*?)</p>', html_text, re.S):
        text = re.sub(r'<[^>]+>', '', pm.group(1)).strip()
        if text and len(text) > 10 and text not in seen:
            seen.add(text)
            results.append(('P', text))
    # Method 3: Escaped JSON content blocks (&quot;content&quot;:[0,&quot;...&quot;])
    content_escaped = re.findall(r'&quot;content&quot;:\[0,&quot;((?:[^&]|&(?!quot;))*?)&quot;\]', html_text)
    for c in content_escaped:
        decoded = c.replace('\\&quot;', '"').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            for hm in re.finditer(rf'<{tag}[^>]*>(.*?)</{tag}>', decoded, re.S):
                text = re.sub(r'<[^>]+>', '', hm.group(1)).strip()
                if text and text not in seen:
                    seen.add(text)
                    results.append((tag.upper(), text))
        for pm in re.finditer(r'<p[^>]*>(.*?)</p>', decoded, re.S):
            text = re.sub(r'<[^>]+>', '', pm.group(1)).strip()
            if text and len(text) > 10 and text not in seen:
                seen.add(text)
                results.append(('P', text))
    # Sort: H1 first, then H2, H3, etc., then P
    priority = {'H1': 0, 'H2': 1, 'H3': 2, 'H4': 3, 'H5': 4, 'H6': 5, 'P': 6}
    results.sort(key=lambda x: priority.get(x[0], 9))
    return results[:max_items]

def extract_hero_text(html_text):
    """Extract hero text from the first/initial block's content.
    Looks for the GridTextBox nearest to the top of the page (lowest desktop 'top' value)."""
    # Find escaped content blocks with their position info
    # Pattern: &quot;content&quot;:[0,&quot;...&quot;],&quot;desktop&quot;:[0,{&quot;top&quot;:[0,NNN],
    blocks = []
    for m in re.finditer(r'&quot;content&quot;:\[0,&quot;((?:[^&]|&(?!quot;))*?)&quot;\].*?&quot;desktop&quot;:\[0,\{&quot;top&quot;:\[0,(\d+)\]', html_text, re.S):
        content_raw = m.group(1)
        top_pos = int(m.group(2)) if m.group(2).isdigit() else 9999
        decoded = content_raw.replace('\\&quot;', '"').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        # Extract text
        texts = []
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
            for hm in re.finditer(rf'<{tag}[^>]*>(.*?)</{tag}>', decoded, re.S):
                text = re.sub(r'<[^>]+>', '', hm.group(1)).strip()
                if text and len(text) > 3:
                    texts.append(text)
        if texts:
            blocks.append((top_pos, texts))
    # Sort by position (top to bottom)
    blocks.sort(key=lambda x: x[0])
    # Return first few text blocks (hero area = top ~300px)
    hero_texts = []
    for pos, texts in blocks[:3]:
        hero_texts.extend(texts)
    return hero_texts[:5]

def identify_hero_block(html_text):
    """Hero = first non-logo image path. Also detect video hero (pexels).
    Handles both raw and HTML-entity-escaped JSON."""
    first_img = None
    hero_video = None
    # Match both "path":[0,"..."] and &quot;path&quot;:[0,&quot;...&quot;
    for m in re.finditer(r'(?:&quot;path&quot;:\[0,&quot;|"path":\[0,")([^"&]+\.(?:png|jpg|jpeg|gif|webp))', html_text, re.I):
        path = m.group(1)
        if 'logo' in path.lower():
            continue
        first_img = path
        break
    # Check for hero video (both forms)
    video_match = re.search(r'(?:&quot;videoSrc&quot;:\[0,&quot;|"videoSrc":\[0,")(https://videos\.pexels\.com/[^"&]+)', html_text)
    if video_match:
        hero_video = video_match.group(1)
    initial = re.findall(r'(?:&quot;initialBlockId&quot;:\[0,&quot;|"initialBlockId":\[0,")([^"&]+)', html_text)
    return first_img, initial, hero_video

def build_image_alt_map(grid_images):
    mapping = {}
    for g in grid_images:
        path = g['path']
        if path not in mapping:
            mapping[path] = {'alt': g['alt'], 'type': g['type']}
    return mapping

def analyze_page(name, filepath, url):
    html_text = Path(filepath).read_text(errors='replace')
    all_images = extract_all_image_paths(html_text)
    asset_images = [i for i in all_images if SITE_ID in i]
    seen_basenames = set()
    unique_images = []
    for img in asset_images:
        basename = img.split('/')[-1]
        if basename not in seen_basenames:
            seen_basenames.add(basename)
            unique_images.append(img)
    grid_images = extract_gridpro_backgrounds(html_text)
    texts = extract_text_content_near_top(html_text, max_items=30)
    first_img, initial_block, hero_video = identify_hero_block(html_text)
    hero_texts = extract_hero_text(html_text)
    return {
        'name': name, 'url': url, 'unique_images': unique_images,
        'grid_images': grid_images, 'texts': texts,
        'first_img': first_img, 'initial_block': initial_block, 'hero_video': hero_video,
        'hero_texts': hero_texts,
    }

def format_report(results):
    lines = []
    lines.append("# EMUQI Original Site Audit")
    lines.append("")
    lines.append("> Source: http://www.emuqi.com/ (Zyrosite platform)")
    lines.append("> Fetched via curl from server-rendered HTML (assets.zyrosite.com CDN)")
    lines.append(f"> Pages analyzed: {len(results)}")
    lines.append("")
    for r in results:
        lines.append(f"## {r['name']}")
        lines.append(f"**URL**: `{r['url']}`")
        lines.append("")
        img_alt_map = build_image_alt_map(r['grid_images'])
        # Hero
        lines.append("### Hero区域")
        if r['first_img']:
            hero_url = f"https://assets.zyrosite.com/{SITE_ID}/{r['first_img']}"
            hero_info = img_alt_map.get(r['first_img'], {})
            lines.append(f"- Hero背景图: `{hero_url}`")
            if hero_info.get('alt'):
                lines.append(f"- Hero图alt: \"{hero_info['alt']}\"")
        if r.get('hero_video'):
            lines.append(f"- Hero背景视频: `{r['hero_video']}`")
        if not r['first_img'] and not r.get('hero_video'):
            lines.append("- Hero背景: (未检测到独立背景图，可能为纯色/渐变)")
        # Hero text
        hero_t = r.get('hero_texts', [])
        if hero_t:
            lines.append(f"- Hero文案: {' | '.join(hero_t[:3])}")
        else:
            hero_texts = [t for t in r['texts'][:5] if t[0] in ('H1', 'H2')]
            if hero_texts:
                lines.append(f"- Hero标题: {hero_texts[0][1]}")
                if len(hero_texts) > 1:
                    lines.append(f"- Hero副标题: {hero_texts[1][1]}")
        lines.append("")
        # Body images
        lines.append("### 主体图片")
        body_imgs = [img for img in r['unique_images'] if os.path.basename(img) != r['first_img']]
        body_imgs = [img for img in body_imgs if 'logo' not in img.lower() and 'traffic' not in img.lower()]
        if body_imgs:
            for img in body_imgs:
                basename = img.split('/')[-1]
                info = img_alt_map.get(basename, {})
                alt_str = f" alt=\"{info['alt']}\"" if info.get('alt') else ""
                type_str = f" [{info['type']}]" if info.get('type') else ""
                lines.append(f"- `{img}`{alt_str}{type_str}")
        else:
            lines.append("- (无额外主体图片)")
        lines.append("")
        logo_imgs = [img for img in r['unique_images'] if 'logo' in img.lower()]
        if logo_imgs:
            lines.append(f"### Logo")
            for img in logo_imgs:
                lines.append(f"- `{img}`")
            lines.append("")
        # Layout
        lines.append("### 排版结构")
        h_tags = [(tag, text) for tag, text in r['texts'] if tag.startswith('H')]
        if h_tags:
            lines.append("区块顺序（按标题推断）:")
            for i, (tag, text) in enumerate(h_tags):
                lines.append(f"  {i+1}. {tag}: {text}")
        else:
            lines.append("（未提取到明确标题结构 — 可能为图片为主的页面）")
        if r['initial_block']:
            lines.append(f"\n首屏Block ID: {', '.join(r['initial_block'])}")
        lines.append("")
        lines.append("---")
        lines.append("")
    return '\n'.join(lines)

def main():
    results = []
    for name, filepath, url in PAGES:
        if not Path(filepath).exists():
            print(f"WARNING: {filepath} not found", file=sys.stderr)
            continue
        r = analyze_page(name, filepath, url)
        results.append(r)
        print(f"  {name}: {len(r['unique_images'])} images, {len(r['texts'])} texts", file=sys.stderr)
    report = format_report(results)
    Path("/tmp/original_site_audit.md").write_text(report)
    print(f"\nReport: /tmp/original_site_audit.md ({len(report)} bytes)", file=sys.stderr)

if __name__ == '__main__':
    main()
