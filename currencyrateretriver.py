import requests
from bs4 import BeautifulSoup
from datetime import date
from workalendar.europe import Poland

class CurrencyRateRetriver(object):

    _root_request_url: str = 'https://www.nbp.pl/home.aspx?navid=archa&c=/ascx/tabarch.ascx&n=a{}z{}'

    def _init(self):
        pass

    def get_rate_by_date(self, currency_date):
        cal = Poland()

        t = self.__convert_date2(currency_date)
        nr_of_days = cal.get_working_days_delta(date(2018, 1, 1), t)

        if len(str(nr_of_days)) == 1:
            formatted_nr_of_days = "00{}".format(nr_of_days)
        elif len(str(nr_of_days)) == 2:
            formatted_nr_of_days = "0{}".format(nr_of_days)
        elif len(str(nr_of_days)) == 3:
            formatted_nr_of_days = "{}".format(nr_of_days)

        url = self._root_request_url.format(formatted_nr_of_days, self.__convert_date(currency_date))

        print(url)
        response = requests.get(url)

        if response.status_code == 200:
            print('Got the data from web page')

        soup = BeautifulSoup(response.content, 'html5lib')
        table = soup.find('table', {'width': '386'})

        rows = table.find_all('tr')

        for row in rows:
            cels = row.find_all('td')
            row_content = [cel.text.strip() for cel in cels if cel]
            #print("Row content {}".format(row_content))

            if len(row_content) == 3:
                #print("Row content len {}".format(len(row_content)))
                #print("row 0: {}".format(row_content[0]))
                if row_content[0] == "euro":
                    current_rate = row_content[2].replace(",", ".")
                    break

        return float(current_rate)

    @staticmethod
    def __convert_date(current_date):
        return ''.join(list(reversed(current_date.split('-'))))

    @staticmethod
    def __convert_date2(current_date):
        temp = list(reversed(current_date.split('-')))
        return date(int(temp[0])+2000, int(temp[1]), int(temp[2]))
