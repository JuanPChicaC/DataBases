import json
import logging


logging.basicConfig(
    filename = "Log.log",
    filemode = "w",
    format = "%(asctime)s | %(module)s | %(levelname)s | %(message)s",
    level = logging.INFO
    )

logger = logging.getLogger(__name__)

__config = None

def config():
    
    global __config
    
    if not __config: 
        
        with open("config.json", mode = "r") as file:
            __config = json.loads(file.read())
            file.close()
    
    return __config



