import requests
import time

def parse_date_array_and_valutes_change(dates_quantity: int,
                                        url: str,
                                        accepted_valutes = None,
                                        url_sleep_time = 0.5
                                        ) -> tuple[list[str], dict]:
    '''
    each index: int datas_valutes_change["<some_valute>"] accords to date_array position
    '''

    date_array = []
    datas_valutes_change = {}  # записаны {"код валюты": [n1, n2, ..., dates_quantity]}
    for i in range(dates_quantity):
        res = requests.get(url, headers={'Accept': 'application/json'})

        if res.status_code == 200:
            date_array.append(res.json()["Date"])

            valutes_single_day = res.json()["Valute"]
            for valute_name, valute_info in valutes_single_day.items():

                if accepted_valutes is None:
                    valute_value = valute_info.get("Value", 0)
                    datas_valutes_change.setdefault(valute_name, []).append(valute_value)

                elif valute_name in accepted_valutes:
                    valute_value = valute_info.get("Value", 0)
                    datas_valutes_change.setdefault(valute_name, []).append(valute_value)


            url = get_next_url(res.json()["PreviousURL"])
            time.sleep(url_sleep_time)

    return date_array, datas_valutes_change


def get_next_url(prev_url: str, connection = "https:") -> str:
    prev_url.replace("\/", "/")
    return connection + prev_url
