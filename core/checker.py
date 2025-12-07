#checker.py
import requests
import urllib3
from bs4 import BeautifulSoup
from core.logger import exception_log as log
# from utils.http_utils import create_session, disable_certificate_warning


# disable_warn = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
disable_warn = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def web_request(TARGET, SESSION_UTIL):
    """
    Sends a Web Request to specified URL
    TARGET: URL/Domain TLD
    SESSION_UTIL: Configured Session (You can modify Session in utils.http_utils.py)
    """
    
    session = SESSION_UTIL
    r = session.get(f"http://{TARGET}/")
    if r.status_code:
        soup = BeautifulSoup(r.text, "html.parser") 
        if soup.title:
            return TARGET, r.status_code, soup.title.string
        elif not soup.title:
            return TARGET, r.status_code, None
    # else:
    #     return TARGET, r.status_code, ""
    
def target_lister(FILE):
    """
    Reads Targets (-t) File and Lists the URLs/Domains as Python List
    """
    
    target_list = []
    with open(FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if len(line) < 3:
                continue
            else:
                target_list.append(line)
    return target_list

def target_check(TARGET_LIST, SESSION_INPUT):
    """
    Uses target_lister() & web_request() methods to generate results as a dictionary list type
    TARGET_LIST: Input FILE for target_lister()
    SESSION_INPUT: SESSION_UTIL config for target_lister()
    """
    
    INPUT_LIST = target_lister(TARGET_LIST)
    OUTPUT_LIST= []
    for INPUT in INPUT_LIST:
        try:
            target, status, title = web_request(INPUT, SESSION_UTIL=SESSION_INPUT)
            OUTPUT_LIST.append({
                "subdomain_address" : f"http://{target}/",
                "status_code" : status,
                "subdomain_title" : title
            })
        except Exception as e:
            log(e)
    return OUTPUT_LIST

    
    
    
    
    
    
    