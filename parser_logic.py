import re

def extract_google_play_ids(html_content):
    pattern = r'\/store\/apps\/details\?id=([a-zA-Z0-9._]+)'
    matches = re.findall(pattern, html_content)
    return list(dict.fromkeys(matches))

def extract_app_store_ids(html_content):
    patterns = [
        r'\/app\/[^"\'\s<>]*\/id(\d{6,})',
        r'(?:apps\.apple\.com|itunes\.apple\.com)[^"\'\s<>]*\bid(\d{6,})'
    ]
    all_ids = []
    for p in patterns:
        all_ids.extend(re.findall(p, html_content))
    return list(dict.fromkeys(all_ids))

def get_page_title(html_content):
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if title_match:
        return title_match.group(1).strip()
    return None
