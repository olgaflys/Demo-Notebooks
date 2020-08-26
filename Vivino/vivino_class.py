import requests
import json
import time
import pandas as pd

class Spider:
    def __init__(self, url_pattern, headers, pages_to_scrape=10, sleep_interval=-1, content_parser=None):
        self.url_pattern = url_pattern
        self.headers=headers
        self.pages_to_scrape = pages_to_scrape
        self.content_parser = content_parser
        self.sleep_interval=sleep_interval
    
    def scrape_url(self, url):
        try:
            response = requests.get(url, self.headers, timeout=10)
            content = self.get_response_content(response)
            if not self.content_parser is None:
                result = self.content_parser(content)
            else:
                result = content
        except:
            result = None
        print(url, 'is done')
        time.sleep(self.sleep_interval)
        return result # added line
    
    def get_response_content(self, r):
        if (r.status_code == 200):
            return r.content
        return False

def quotes_parser(content):
    soup = content.json()
    df=pd.json_normalize(soup)
    df1=pd.json_normalize(df['explore_vintage.matches'][0])
    return df1
