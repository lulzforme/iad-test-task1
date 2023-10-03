import requests
from bs4 import BeautifulSoup

# URL для доступа к веб-сервису Центрального банка России
url = 'https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx'


def get_course_on_date(date):
    headers = {
        'Content-Type': 'application/soap+xml; charset=utf-8',
    }

    body = f'''
        <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
          <soap12:Body>
            <GetCursOnDateXML xmlns="http://web.cbr.ru/">
              <On_date>'''+date+'''</On_date>
            </GetCursOnDateXML>
          </soap12:Body>
        </soap12:Envelope>
    '''

    return requests.post(url, data=body, headers=headers)


dates = ['2023-09-29', '2023-09-30', '2023-10-01', '2023-10-02']

course_list = {}

for date in dates:
    response = get_course_on_date(date)
    soup = BeautifulSoup(response.text, 'xml')
    valute_data = soup.find_all('ValuteCursOnDate')
    for course in valute_data:
        if course.VchCode.string == 'USD':
            val = {
                'code': course.VchCode.string,
                'value': course.Vcurs.string
            }
            course_list.update({date: val})

print(course_list)
