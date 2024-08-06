from src.config import SEARCH_TEXT, EXCLUDE_TEXT
from src.practica import get_vacancy
from datetime import datetime
from src.logs import setup_logging
from src.file_manager import save_to_json

logger = setup_logging()

if __name__ == '__main__':
    logger.info("Application starts....")

    date_today = datetime.now().strftime("%Y_%m_%d")
    file_name = f'{date_today}_{SEARCH_TEXT.replace(" ","_")}.json'

    vacancies = get_vacancy(SEARCH_TEXT,EXCLUDE_TEXT)
    save_to_json(vacancies,file_name)

    logger.info("Application finished")
