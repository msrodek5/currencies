from currencyrateretriver import CurrencyRateRetriver
from FileReader import *


def main():

    data_items = get_input_data("c:\\users\\mzsk\\Downloads\\import dywidend 2019.txt")
    currency_rate_retriver = CurrencyRateRetriver()

    new_data_items = []
    for data_item in data_items:
        currency_rate = currency_rate_retriver.get_rate_by_date(data_item.currency_date)

        new_data_item = DataItemTaxDue(data_item.share_id,\
                                 data_item.currency_date,\
                                 data_item.dividend_amount,\
                                 currency_rate)

        new_data_items.append(new_data_item)
        print(new_data_item)


if __name__ == '__main__':
    main()
