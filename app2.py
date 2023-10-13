from datetime import datetime, timedelta

GRAPHIC_MODE = "markers"
url = "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx"
valuta_list = ["USD", "EUR"]
dates = []
start_date_str = "2022-10-01"
end_date_str = "2023-10-01"


start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
current_date = start_date
while current_date <= end_date:
    dates.append(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=30)