# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/customers_data.py
# Endpoint: customers
# URL: {'proper_name': 'Customers', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.customers import Customers
from autonomousAJ_stripeAPI.config import global_config

class Customers_Data:
    def __init__(self):
        self.customers = Customers()

    def get_and_process_data(self):
        data = self.customers.get_customers()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
