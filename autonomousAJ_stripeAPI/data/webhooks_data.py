# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/webhooks_data.py
# Endpoint: webhooks
# URL: {'proper_name': 'Webhooks', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.webhooks import Webhooks
from autonomousAJ_stripeAPI.config import global_config

class Webhooks_Data:
    def __init__(self):
        self.webhooks = Webhooks()

    def get_and_process_data(self):
        data = self.webhooks.get_webhooks()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
