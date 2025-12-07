import requests
# from config.config_loader import config_process
import urllib3

# def disable_certificate_warning():
#     return urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_session(proxy, agent, ssl, timeout):
    # config = config_process()
    
    session = requests.Session()
    
    session.headers.update({
        "User-Agent": agent
    })
    proxy = proxy
    if proxy:
        session.proxies = {"http": proxy, "https": proxy}
    session.verify = ssl
    session.request_timeout = timeout

    return session