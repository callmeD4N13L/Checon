# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from urllib.parse import urljoin
# import time
# from config.config_loader import config_process

# def selenium_session():
#     config = config_process()
#     level = config.get("level", 2)
#     options = webdriver.ChromeOptions()
#     # --headless meaning do not open chrome window
#     options.add_argument("--headless") 
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     return driver, level