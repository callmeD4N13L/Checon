#mail_crawler.py
import re, requests, urllib3, tld
from bs4 import BeautifulSoup
from tld import get_tld
from typing import List, Tuple
from urllib.parse import urljoin
from core.logger import exception_log as log

disable_warn = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def input_list_parser(OUTPUTLIST):
    INPUTLIST = []
    for OUTPUT in OUTPUTLIST:
        for item in OUTPUT:
            if item["status_code"] == 200 and item["subdomain_title"]:
                INPUTLIST.append(item["subdomain_address"])
    return INPUTLIST
        #####
        # print(OUTPUT)
            # print(type(item["status_code"]), item["status_code"])
        #####

def email_finder(HTMLPARSED):
    """only regexes"""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    page_text = HTMLPARSED.get_text()
    emails = re.findall(email_pattern, page_text)
    emails = list(set(emails))
    return emails


def link_finder(HTMLPARSED):
    links = [a['href'] for a in HTMLPARSED.find_all('a', href=True)]
    links = list(set(links))
    return links

# def crawl_request(TARGET, SESSION_UTIL):
#     """checks urls"""
#     session = SESSION_UTIL
#     r = session.get(TARGET)
#     if r.status_code == 200:
#         html = BeautifulSoup(r.text, "html.parser")
#         page_text = html.get_text()
#         return html, page_text

def crawl_request(TARGET, SESSION_UTIL):
    """checks urls"""
    session = SESSION_UTIL
    try:
        r = session.get(TARGET, timeout=10)
    except Exception as e:
        log(e)
        return None, None


    if r.status_code == 200:
        html = BeautifulSoup(r.text, "html.parser")
        page_text = html.get_text()
        return html, page_text
    return None, None

def is_valid_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")

def crawler(OUTPUTLIST, SESSION_UTIL, LEVEL):
    """
    Impelements BFS algorythm for Depth WebCrawling
    OUTPUTLIST: OUTPUTS of checker module
    SESSION_UTIL: Configured Session (in http_utils.py)
    LEVEL: Level of Depth (LoD)
    """
    final_emails = []
    visited = set()
    next_level_urls = set(input_list_parser(OUTPUTLIST))

    for depth in range(1, LEVEL + 1):
        print(f"[*] DEPTH {depth} — URLs: {len(next_level_urls)}")

        current_level_urls = next_level_urls.copy()
        next_level_urls = set()
        level_emails = []

        for url in current_level_urls:
            if url in visited:
                continue
            visited.add(url)

            html, text = crawl_request(url, SESSION_UTIL)
            if html is None:
                continue

            # Last Layer: extend the emails!!!!
            if depth == LEVEL:
                level_emails.extend(email_finder(html))

            # Former Layers: extend the Links!!!
            if depth < LEVEL:
                links = link_finder(html)
                for link in links:
                    absolute = urljoin(url, link)

                    # Filter Valid URLS
                    if not is_valid_url(absolute):
                        continue

                    if absolute not in visited:
                        next_level_urls.add(absolute)

        final_emails.extend(level_emails)

    return list(set(final_emails)) 