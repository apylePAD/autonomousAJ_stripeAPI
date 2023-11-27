# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/payment_methods_data.py
# Endpoint: payment_methods
# URL: {'proper_name': 'Payment_Methods', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.payment_methods import Payment_Methods
from autonomousAJ_stripeAPI.config import global_config

class Payment_Methods_Data:
    def __init__(self):
        self.payment_methods = Payment_Methods()

    def get_and_process_data(self):
        data = self.payment_methods.get_payment_methods()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
