import json
import logging
import os

logger = logging.getLogger(__name__)

def save_to_json(data,file_name):
    with open(file_name,'w',encoding= 'utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=4)


    logger.info(f"Data successfully saved to {os.getcwd()}\\{file_name}")