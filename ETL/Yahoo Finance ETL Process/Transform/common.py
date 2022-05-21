import json
import logging
import os
import re
from pandas import DataFrame

logging.basicConfig(
    filename = "Log.log",
    filemode = "w",
    format = "%(asctime)s | %(module)s | %(levelname)s | %(message)s",
    level = logging.INFO
    )

logger = logging.getLogger(__name__)

__config = {
    "Extract" : None,
    "Transform" : None
    }

def config(layer):
    
    
    global __config

    assert layer in __config.keys(), "Invalid layer option select between: {}".format(', '.join(__config.keys()))
    
    
    if not __config[layer]: 
        
        with open(f"../{layer}/config.json", mode = "r") as file:
            __config[layer] = json.loads(
                file.read()
                )
            file.close()
    
    return __config[layer]


class Extracted_Information():
    
    def __init__(self):
        
        
        
        self.extracted_files = os.listdir(
            "../Extract/{}".format(
                config("Extract")["web scrapper"]["extraction_location"]
                )
            )
        
        self.files_tuple_info = [
            re.findall(
                r"{}".format(
                    config("Extract")["web scrapper"]["filename_extraction"].format(
                        content = "(.*?)",
                        type_asset = "(.*?)"
                        )
                    ),
                filename            
                )[0]
            for filename in self.extracted_files
            ]
    
        files_content = DataFrame(
            columns = ['letter','type'],
            data = self.files_tuple_info
            )
    
        self.dict_ = {
            type_ : dataframe['letter'].tolist()
            for type_, dataframe in files_content.groupby('type')
            }
    
        self.type_options = list(
            self.dict_.keys()
            )
    

    @property
    def letter_options(self):
        
        letter_options = []
    
        for type_option in self.type_options:
            for letter in self.dict_[type_option]:
                if letter not in letter_options:
                    letter_options.append(
                        letter
                        )
                    
        letter_options.sort()
    
        return letter_options
    