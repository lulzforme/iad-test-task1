import requests
from bs4 import BeautifulSoup
from config import dates, url, valuta_list, GRAPHIC_MODE
import plotly.graph_objs as go


def get_courses_by_day_date(date):
    body = f'''
            <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
              <soap12:Body>
                <GetCursOnDateXML xmlns="http://web.cbr.ru/">
                  <On_date>{date}</On_date>
                </GetCursOnDateXML>
              </soap12:Body>
            </soap12:Envelope> '''

    return requests.post(url, data=body, headers={'Content-Type': 'application/soap+xml; charset=utf-8'})


def get_courses(date_list: list) -> {}:
    courses = {}
    for date in date_list:
        # init dates in dict
        courses[date] = []
        # get valuta course by date
        response = get_courses_by_day_date(date)
        soup = BeautifulSoup(response.text, "xml")
        valuta = soup.find_all('ValuteCursOnDate')
        # fill courses dict with list comprehension
        [
            courses[date].append({val.VchCode.string: val.Vcurs.string})
            for val in valuta if val.VchCode.string in valuta_list
        ]
    return courses


def draw_graphics(courses: dict):
    data = {}
    fig = go.Figure()
    for date, valutas in courses.items():
        for valuta in valutas:
            for key, value in valuta.items():
                if key not in data.keys():
                    data[key] = []
                data[key].append(float(value))

    for key, value in data.items():
        fig.add_trace(go.Scatter(x=dates, y=value, mode=GRAPHIC_MODE, name=key))

    fig.update_layout(
        xaxis_title="Дата",
        yaxis_title="Курс к рублю"
    )
    fig.show()


def main():
    courses = get_courses(dates)
    draw_graphics(courses)


if __name__ == "__main__":
    main()
