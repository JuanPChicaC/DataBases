from requests import get
from common import config, logger
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from pandas import DataFrame
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--headless')
options.add_argument('--disable-gpu')

class TickerPage():
    
    def __init__(self, 
                 endpoint, 
                 content = "",
                 beggining_record = "0",
                 type_asset = "all",
                 rows_amount = str(
                     config()["queries"]["rows_limit"]
                     ),
                 max_rows_loaded = str(
                     config()["queries"]["max_rows_loaded"]
                     ) 
                 ):
        
        self.endpoint = endpoint
        self.content = content
        self.beggining_record = int(beggining_record) if beggining_record != "" else 0 
        self.rows_amount = int(rows_amount)
        self.type_asset = type_asset
        self.max_rows_loaded = int(max_rows_loaded)
        self.open = False
        self._dirver = None
        
        self._urls = config()["urls"]
        self._queries = config()["queries"]
        self._html = None

        self.visit(
            self.endpoint, 
            content = self.content, 
            beggining_record = self.beggining_record, 
            rows_amount = self.rows_amount,
            type_asset = type_asset,
            max_rows_loaded = self.max_rows_loaded
            )

    @property
    def records_amount(self):
        
        records_amount_list = self._select(
            self._queries["header information"]["tag"]
            )
        
        record_location = 0 if self.type_asset == 'all' else self._queries["header information"]["data"][self.type_asset]["location"]
        
        print(records_amount_list)
        print(record_location)
        
        records_amount_text = [record.get_text() for record in records_amount_list][record_location] 
        
        records_amount = re.findall(
            r"\((.*?)\)",
            records_amount_text
            )
        
        records_amount = int(records_amount[0])
        
        return records_amount
    
    
    @property
    def header_record_amount_dict(self):
        
        records_amount_list = self._select(
            self._queries["header information"]["tag"]
            )
        
        records_amount_list = [
            info_amount.get_text() 
            for info_amount in records_amount_list 
            if info_amount.get_text() != ""
            ]
        
        
        return {
            text[:text.find(" (")] : int(text[text.find(" (") + 2:text.find(")")])
            for text in records_amount_list
            }
    
    
    
    @property
    def table_content(self):
        
        symbols_table = []
        
        table_information = self._queries["table information"]
        
        symbols_table_html = self._find(
            table_information["tag"]
            )
        
        rows_information = table_information["rows information"]

        components_information = rows_information["components"]
        
        for row in symbols_table_html.find_all(rows_information["tag"]):
            
            row_content = row.find_all(
                components_information["tag"]
                )
            
            symbols_table.append(
                {
                    attribute : row_content[
                        components_information["data"][attribute]["location"]
                        ].get_text()
                    for attribute in components_information["data"].keys()
                    }
                )
            
        return symbols_table
    
    def _find(self, tag, class_name = None):
        return self._html.find(
            tag,
            class_ = class_name
            )

    def _find_all(self, tag, class_name = None):
        return self._html.find_all(
            tag,
            class_ = class_name
            )
        
    def _select(self, query):
        return self._html.select(query)
        
    def visit(
            self, 
            endpoint, 
            content = "", 
            beggining_record = "0",
            type_asset = "all",
            rows_amount = str(
                config()["queries"]["rows_limit"]
                ),
            max_rows_loaded = str(
                config()["queries"]["max_rows_loaded"]
                )             
            ):
        
        self.endpoint = endpoint
        self.content = content
        self.beggining_record = int(beggining_record)
        self.rows_amount = int(rows_amount)        
        self.type_asset = type_asset
        self.max_rows_loaded = int(max_rows_loaded)
        
        type_url = type_asset if type_asset == 'all' else self._queries["header information"]["data"][self.type_asset]["label"]
        
        self.open_()
        
        
        
        self.url = self._urls[endpoint].format(
            type = type_url,
            content = content,
            beggining_record = beggining_record,
            rows_amount = rows_amount
            )
        
        try: 
            
            self._driver.get(
                self.url                
                )

        except HTTPError:
            
            logger.error(
                f"HTTPError : {self.url}",
                exc_info=True
                )
    
        self._html = BeautifulSoup(
            self._driver.page_source,
            'html.parser'
            )
    
    def open_(self):
        
        if not self.open:
        
            self._driver = webdriver.Chrome(
                executable_path = r"{}".format(
                    config()["web scrapper"]["driver name"]
                    ),
                chrome_options = options
                )
            
            self.open = True
    
    def close_(self):
        if self.open:
            
            self._driver.quit()
            self.open = False
            