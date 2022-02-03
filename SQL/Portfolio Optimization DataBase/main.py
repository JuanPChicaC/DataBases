# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:44:58 2022

@author: juanp
"""

import logging
logging.basicConfig(level=logging.INFO)
import subprocess


logger = logging.getLogger(__name__)

def main():
    
    database_creation()
    
    logger.info(
        'The database is already been created'
        )
    
    database_update()

    logger.info(
        'The beggining information is already been loaded'
        )
    

def database_creation():
    
    subprocess.run(
        [
            'python',
            'database_creation.py'
            ]
        )
    

def database_update():
    subprocess.run(
        [
            'python',
            'database_update.py'
            ]
        )



if __name__ == '__main__':
    
    main()
    