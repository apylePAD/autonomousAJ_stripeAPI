# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/subscriptions_data.py
# Endpoint: subscriptions
# URL: {'proper_name': 'Subscriptions', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.subscriptions import Subscriptions
from autonomousAJ_stripeAPI.config import global_config

class Subscriptions_Data:
    def __init__(self):
        self.subscriptions = Subscriptions()

    def get_and_process_data(self):
        data = self.subscriptions.get_subscriptions()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
