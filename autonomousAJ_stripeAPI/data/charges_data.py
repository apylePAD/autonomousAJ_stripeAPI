# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/charges_data.py
# Endpoint: charges
# URL: {'proper_name': 'Charges', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.charges import Charges
from autonomousAJ_stripeAPI.config import global_config

class Charges_Data:
    def __init__(self):
        self.charges = Charges()

    def get_and_process_data(self):
        data = self.charges.get_charges()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
