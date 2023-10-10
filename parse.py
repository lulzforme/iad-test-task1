import matplotlib.pyplot as plt
import datetime
import requests
def get_info(code, date):
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date.strftime('%d/%m/%Y')}" ##ссылка на сайт с датой + "f" выступает в роли вставки значения даты в ссылку
    response = requests.get(url)
    if response.status_code == 200: ##Код статуса верной отработки
        content = response.content.decode("windows-1251") ##декодирование данных с сайта 
        start_tag = f"<CharCode>{code}</CharCode>"##нахождение желаемого кода вадюты
        start_index = content.find(start_tag)
        if start_index != -1:##пока не найдём желаемое
            value_start = content.find("<Value>", start_index) + len("<Value>") ##нахождение индекса 
            value_end = content.find("</Value>", value_start)
            rate = float(content[value_start:value_end].replace(",",".")) ##нужна замена на точку из-за ошибки в типе данных == ValueError: could not convert string to float: '21,0825' 
            return rate
    return 0