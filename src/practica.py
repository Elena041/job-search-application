import requests
import logging

logger = logging.getLogger(__name__)

def get_vacancy(search_text:str,exclude_word:str) -> list:
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": search_text,
        "exclude": exclude_word,
        "search_field": "name",
        "area": 1,
        "period": 1,
        'only_with_salary': True,
        "per_page": 100,
        "page": 0
    }

    vacancies = []
    while True:
        response = requests.get(url,params=params)
        data = response.json()
        vacancies += data["items"]

        if data["pages"] == params["page"]:
            break
        else:
            params["page"] += 1

        result = []
        for vac in vacancies:
            vacancy_data = {
                "name": vac["name"],
                "salary": vac['salary']['from'] if vac['salary']['from'] is not None else 'Not specified',
                "url": vac["url"]
            }

            result.append(vacancy_data)

        logger.info(f"Found {len(result)} vacancies")
        return result





