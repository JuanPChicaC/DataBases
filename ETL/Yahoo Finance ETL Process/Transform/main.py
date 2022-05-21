from common import config, Extracted_Information, logger
import argparse
from pandas import read_json, concat
from os import remove, path, mkdir
import json
import logging

console = logging.StreamHandler()
logging.getLogger().addHandler(console)

def dict_available_files(selected_type_asset,selected_letter_option, files_list):
    
    filename_structure = config("Extract")["web scrapper"]["filename_extraction"]
    
    available_files = {}
    
    for type_asset in selected_type_asset:
        available_files[type_asset] = []
        
        for letter in selected_letter_option:    
            
            filename = filename_structure.format(
                content = letter,
                type_asset = type_asset
                )
            
            if filename in files_list:
                available_files[type_asset].append( filename ) 
    
    return available_files
    

def opening_extracted_file(filename):
    
    extraction_dir_location = config("Extract")["web scrapper"]["extraction_location"]
    
    return read_json(
        '../Extract/{}/{}'.format(
            extraction_dir_location,
            filename
            )
        )

def delete_extracted_file(filename):
    
    extraction_dir_location = config("Extract")["web scrapper"]["extraction_location"]
    
    return remove(
        '../Extract/{}/{}'.format(
            extraction_dir_location,
            filename
            )        
        )

def open_file(path):
    
    with open(path,"r") as file:
        json_info = json.loads(
            file.read()
            )    
        file.close()
    
    return json_info

def save_json_file(json_file,path):
    
    with open(path,"w+") as file:
        json.dump(
            json_file,
            file,
            indent = 4
            )

def main(selected_type_asset,selected_letter_option, files_list, drop = True):
    
    logging.info(
        "Intializing transformation layer"
        )
    
    files_info = dict_available_files(
        selected_type_asset,
        selected_letter_option,
        files_list
        )

    transform_config = config("Transform")["transformation config"]

    if not path.isdir(transform_config["transformation location"]):
        
        mkdir(
            transform_config["transformation location"]
            )

    type_asset_file_path = "{}/{}".format(
        transform_config["transformation location"],
        transform_config["type asset file"]
        )
    
    exchange_file_path = "{}/{}".format(
        transform_config["transformation location"],
        transform_config["exchange file"]
        )
    
    type_asset_to_save = []
    exchange_to_save = []
    
    for type_asset in files_info.keys():
                
        df = concat(
                [opening_extracted_file(file) for file in files_info[type_asset]],
                ignore_index = True
            )
        
        initial_amount_records = len(df)
        
        logging.info(
            f'initializing the transformation of {type_asset} data'
            )
        
        df.drop_duplicates(
            inplace =  True,
            subset = config("Transform")["drop duplicates options"]["columns criteria"],
            keep = config("Transform")["drop duplicates options"]["keep"]
            )
        
        duplicate_records = initial_amount_records - len(df)
        
        logging.info(
            f"{duplicate_records} records duplicated records of {type_asset} were droppped"
            )
        
        type_asset_to_save = type_asset_to_save + df["type"].unique().tolist()
        exchange_to_save = exchange_to_save + df["exchange"].unique().tolist()
        
        if drop:
            
            delete_df = df[df["last price"] == config("Transform")["empty identifier"]]

            delete_df.to_json(
                "{}/{}".format(
                    transform_config["transformation location"],
                    transform_config["filename data to delete"].format(
                        type_asset = type_asset
                        )
                    ),
                orient="records",
                )
            
            no_records_delete = len(delete_df)
            
            logging.info(
                f"there will be {no_records_delete} potential records of {type_asset} to drop from the database"
                )
    
        df = df[df["last price"] != config("Transform")["empty identifier"]]

        df.to_json(
            "{}/{}".format(
                transform_config["transformation location"],
                transform_config["filename new data"].format(
                    type_asset = type_asset
                    )
                ),
            orient="records",
            )
        
        logging.info(
            f"information of {type_asset} already been saved to load into the database" 
            )
        
        [delete_extracted_file(file) for file in files_info[type_asset]]
    
    type_asset_to_save = list(
        dict.fromkeys(
            type_asset_to_save
            )
        )
    
    exchange_to_save = list(
        dict.fromkeys(
            exchange_to_save
            )
        )
    
    save_json_file(
        type_asset_to_save,
        type_asset_file_path
        )
    
    save_json_file(
        exchange_to_save,
        exchange_file_path
        )

    logger.info(
        "information about type of assets an exchanges is already saved to load into the database"
        )
        
    
if __name__ == "__main__":
    
    extracted_information = Extracted_Information()
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "transform_type_asset",
        help = """the type of financial assets that want to be
        used to transforme the extracted information""",
        type = str,
        choices = extracted_information.type_options + ["all"]
        )
    
    parser.add_argument(
        "transform_content_letter",
        help = """the letter that want to be used to transfrom
        the extracted information""",
        type = str,
        choices = extracted_information.letter_options + ["all"]
        )
    
    parser.add_argument(
        "drop_value",
        help = """if 'y' the transform process will define the list of asset 
        that will be dropped from the DB. In other case, nothing will be dropped""",
        type = str,
        choices = list(
            config("Transform")["configuration options"]["drop files options"].keys()
            )
        )
    
    args = parser.parse_args()
    
    selected_type_asset = [args.transform_type_asset] if args.transform_type_asset != 'all' else extracted_information.type_options
    
    selected_letter_options = [args.transform_content_letter] if args.transform_content_letter != 'all' else extracted_information.letter_options
    
    main(
        selected_type_asset,
        selected_letter_options,
        extracted_information.extracted_files,
        drop = bool(
            config("Transform")["configuration options"]["drop files options"][args.drop_value]
            )
        )

    