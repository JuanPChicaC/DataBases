from common import config,logger
from web_page_objects import TickerPage
import string
import argparse
import logging
import json
from os import path, mkdir
from datetime import datetime, timedelta

console = logging.StreamHandler()
logging.getLogger().addHandler(console)




def fetch_info_by_content(content, ticker_page,type_asset, records_amount, rows_amount_limit,max_rows_loaded):

    scrapped_table = []   

    iteration = 0
    
    start_time = datetime.now()
    
    while iteration*rows_amount_limit < min(records_amount,max_rows_loaded):
        
        ticker_page.visit(
            "search by type, content and records",
            content = content,
            beggining_record = str(
                iteration*rows_amount_limit
                ),
            rows_amount = rows_amount_limit,
            type_asset = type_asset,
            max_rows_loaded = max_rows_loaded
            )
        
        scrapped_table = scrapped_table + ticker_page.table_content
        
        iteration += 1
    
    
    end_time = datetime.now()
    
    extraction_time =  end_time - start_time
    
    extraction_minutes = round(
        extraction_time/timedelta(seconds = 60),
        2
        )
    
    logging.info(
        "{} records founded by content {} and type {} were extracted sucessfully. It takes {} minutes".format(
            records_amount,
            content,
            type_asset,
            extraction_minutes
            )
        )
        
    return scrapped_table

def save_information( filename: str, records : list ):

    records_amount = len(records)
    
    start_time = datetime.now()
    
    if not path.isdir(config()["web scrapper"]["extraction_location"]):
        
        mkdir(
            config()["web scrapper"]["extraction_location"]
            )
    
    filename = "{}/{}".format(
        config()["web scrapper"]["extraction_location"],
        filename
        )
    
    if not path.isfile(filename): 
        
        with open(filename, 'w+') as file:
            json.dump(
                records,
                file,
                indent = 4
                )
    else:
        
        with open(filename,'r') as file:
            
            file_records = json.load(
                file
                )
            file.close()

        file_records = file_records + records

        with open(filename,'w') as file:
            json.dump(
                file_records,
                file,
                indent = 4
                )
            file.close()
    
    end_time = datetime.now()
    
    extraction_time =  end_time - start_time
    
    extraction_minutes = round(
        extraction_time/timedelta(seconds = 60),
        2
        )
    
    logging.info(
        "{} records were saved succesfully in {} file. It takes {} minutes".format(
            records_amount,
            filename,
            extraction_minutes
            )
        )  

def _ticks_scrapper(search_criteria, search_type_assets):
    
    inf_type_assets_dict = config()["queries"]["header information"]["data"]
    
    for content in search_criteria:
        for type_asset in search_type_assets:
            
            logging.info(
                f"Beggining the scrapper for symbols that contain {content}, classified as {type_asset}"
                )
        
            try:
                
                if prev_content != content:

                    prev_content = content

                    ticker_page.visit(
                        "search by name content and records",
                        content = content,
                        type_asset = type_asset
                        )
                
                    records_amount_dict = ticker_page.header_record_amount_dict

                                
            except:
                ticker_page = TickerPage(
                    "search by name content and records",
                    content = content,
                    type_asset = type_asset
                    )
                
                prev_content = content
                records_amount_dict = ticker_page.header_record_amount_dict
                
            
            records_amount = records_amount_dict[
                inf_type_assets_dict[type_asset]["header label"]
                ]
            
            logging.info(
                "there is records {} founded by content {} and type {}".format(
                    records_amount,
                    content,
                    type_asset
                    )
                )

            if not records_amount > 0:
                continue
                        
            rows_amount_limit = ticker_page.rows_amount
            max_rows_loaded = ticker_page.max_rows_loaded
            
            scrapped_table = fetch_info_by_content(
                content, 
                ticker_page,
                type_asset,
                records_amount,
                rows_amount_limit,
                max_rows_loaded
                )
        
            save_information(
                config()["web scrapper"]["filename_extraction"].format(
                    content = content,
                    type_asset = type_asset
                    ),
                scrapped_table
                )
        
    ticker_page.close_()


if __name__ == "__main__": 
    
    parser = argparse.ArgumentParser(
        )
    
    search_content_choices = config()["web scrapper"]["search content options"] 
    
    search_type_asset_choices = list(
        config()["queries"]["header information"]["data"].keys()
        )
    
    parser.add_argument(
        "search_type_asset",
        help = """the type of financial assets that want to be extracted""",
        type = str,
        choices = search_type_asset_choices + ["all"]
        )

    parser.add_argument(
        "search_content",
        help = """the letter or symbol  used to search financial assets
        that will be stracted from yahoo finance web page""",
        type = str,
        choices = search_content_choices + ["all"]
        )


    args = parser.parse_args()
    
    search_type_asset = args.search_type_asset
    
    search_type_asset = [search_type_asset] if search_type_asset != "all" else search_type_asset_choices

    search_content = args.search_content
    
    search_content = [search_content] if search_content != "all" else search_content_choices
    
    
    symbol_table = _ticks_scrapper(
        search_content,
        search_type_asset
        )    
    
    


 




