import unittest
import requests
from faker import Faker
from faker.providers import BaseProvider
import re

import ipdb

fake = Faker()

class SaleProvider(BaseProvider):
    def customer_name(self):
        return fake.name()
    
    def description(self):
        return fake.sentence().strip('.')

    def price(self):
        return fake.pyfloat(right_digits=2, min_value=1, max_value=300)

    def quantity(self):
        return fake.pyint(min_value=1, max_value=300)

    def merchant_name(self):
        return fake.company() 

    def merchant_address(self):
        return fake.street_address()

    def sales_row(self):
        return [self.customer_name(), self.description(), self.price(),
                self.quantity(), self.merchant_name(), self.merchant_address()]

    def sales_data(self, num_rows):
        """
        Returns a list of cleaned rows and the revenue
        """
        # Map to string and remove commas
        data = [self.sales_row() for i in range(num_rows)]
        revenue = calculate_revenue(data)
        cleaned_data = [list(map(lambda x: clean(str(x)), row)) for row in data]
        return (cleaned_data, revenue)

    def sales_csv(self, header, num_rows):
        """
        Return csv as a single string, and revenue.
        Rows are delimited by '\n'
        """
        data, revenue = self.sales_data(num_rows)
        data_with_header = [list(header)] + data 
        return ('\n'.join([','.join(row) for row in data_with_header]), revenue)

def calculate_revenue(data):
    price_index = fields.index('price')
    quantity_index = fields.index('quantity')
    revenue = 0
    for row in data:
        revenue += row[price_index] * row[quantity_index]
    return round(revenue, 2)

def clean(s):
    """
    Remove commas

    TODO: make the parser more robust to commas in values in the future
    """
    return re.sub(',', '', s)

   
# Add new provider to faker instance
fake.add_provider(SaleProvider)

fields = ('customer_name', 'description', 'price',
          'quantity', 'merchant_name', 'merchant_address')

class AppTest(unittest.TestCase):
    def test_upload(self):
        for num_rows in range(1, 100):
            print(f'Sending csv with {num_rows} rows')
            data, revenue = fake.sales_csv(header=fields, num_rows=num_rows)
            url = 'http://localhost:5000/sales'    
            r = requests.post(url, data=data)
            resp = r.json()
            self.assertEqual(r.status_code, 200)
            self.assertEqual(resp['num_rows'], num_rows)
            self.assertEqual(resp['revenue'], revenue)

def write_example_csv(num_rows):
    data, revenue = fake.sales_csv(header=fields, num_rows=num_rows)
    with open(f'examples/test_{num_rows}.csv', 'w') as f:
        f.write(data)

if __name__ == '__main__':
    # write_example_csv(10)
    unittest.main()