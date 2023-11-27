# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/balances_data.py
# Endpoint: balances
# URL: {'proper_name': 'Balances', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.balances import Balances
from autonomousAJ_stripeAPI.config import global_config

class Balances_Data:
    def __init__(self):
        self.balances = Balances()

    def get_and_process_data(self):
        data = self.balances.get_balances()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
