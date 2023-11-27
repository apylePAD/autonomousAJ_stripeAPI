# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/refunds_data.py
# Endpoint: refunds
# URL: {'proper_name': 'Refunds', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.refunds import Refunds
from autonomousAJ_stripeAPI.config import global_config

class Refunds_Data:
    def __init__(self):
        self.refunds = Refunds()

    def get_and_process_data(self):
        data = self.refunds.get_refunds()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
