# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/invoices_data.py
# Endpoint: invoices
# URL: {'proper_name': 'Invoices', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.invoices import Invoices
from autonomousAJ_stripeAPI.config import global_config

class Invoices_Data:
    def __init__(self):
        self.invoices = Invoices()

    def get_and_process_data(self):
        data = self.invoices.get_invoices()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
