#Exterior Modules
import argparse
import os
from datetime import datetime

#Interior Modules
import config.config_loader as loader
import core.checker as checker
import core.concurrent_runner as thread
import core.logger as logger
import utils.http_utils as http
import core.mail_crawler as crawler
import data.exporters.json_exporter as exporter

 
# BANNER = """
#        ____ _               _             
#   / ___| |__   ___  ___| | ___   _    
#  | |   | '_ \ / _ \/ __| |/ / | | |   
#  | |___| | | |  __/ (__|   <| |_| |_  
#   \____|_| |_|\___|\___|_|\_\\__, (_) 
#                                |___/   
#       Open-Source OSINT & Web Scanner
# """
 
now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# OUT_DIR = os.path.join(BASE_DIR, "Results")

def main():
    """
    Main Method
    (Runs in CLI)
    """
    parser = argparse.ArgumentParser(description=f"Checcon v0.1.1 | Connection Checker Tool")
    parser.add_argument("-c","--conf", type=str, help="Config File Path", required=True)
    parser.add_argument("-t", "--target", type=str, help="Target List File Path", required=True)

    args = parser.parse_args()
    config_argument = args.conf
    target_argument = args.target

    if config_argument and target_argument:
        #config handling
        #read  config with config loader
        default_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        config = loader.config_process(JSONFILE=config_argument)
        config_ssl_verify = config.get("ssl_verify", False)
        config_request_timeout = config.get("timeout", 5)
        config = loader.config_process(config_argument)
        config_agent = config.get("user_agent", default_agent)
        config_proxy = config.get("proxy", "").strip()
        config_level = config.get("level", "")
        config_crawl = config.get("mail_finding", False)
        
        #http util session
        session = http.create_session(
            proxy= config_proxy,
            agent= config_agent,
            ssl= config_ssl_verify,
            timeout= config_request_timeout
        )

        #request and check with target_argument
        pool = thread.get_pool(max_workers=5)  
        futures = [pool.submit(checker.target_check,target_argument, session)] 
        results = [future.result() for future in futures]

        #output to json for outputs
        exporter.json_exporter(
            OUTPUT_LIST=results,
            FILENAME=f"Checker_Output_{now}.json"
            )

        #let's crawl
        if config_crawl == True and config_level:
            Crawl_Output = crawler.crawler(
                OUTPUTLIST=results,
                SESSION_UTIL=session,
                LEVEL=config_level            
            )
        exporter.json_exporter(
            OUTPUT_LIST=Crawl_Output,
            FILENAME=f"Intel_Output_{now}.json"
            )
    else:
        raise argparse.ArgumentError
    

if __name__ == "__main__":
    main()
