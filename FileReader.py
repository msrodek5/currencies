from dataItem import *

def get_input_data(file_name):
    tax_paid_items = []

    with open(file_name, 'r') as work_file:
        for line in work_file:
            items = line.replace(',', '.').strip('\n').split('|')
            tax_paid_items.append(DataItemTaxPaid(items[0].strip(), items[4].strip(), items[1].strip(), items[2].strip()))

    return tax_paid_items


