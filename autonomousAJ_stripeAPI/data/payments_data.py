# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/payments_data.py
# Endpoint: payments
# URL: {'proper_name': 'Payments', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.payments import Payments
from autonomousAJ_stripeAPI.config import global_config

class Payments_Data:
    def __init__(self):
        self.payments = Payments()

    def get_and_process_data(self):
        data = self.payments.get_payments()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
