# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/data/products_data.py
# Endpoint: products
# URL: {'proper_name': 'Products', 'url': nan}
import pandas as pd
from autonomousAJ_stripeAPI.api.products import Products
from autonomousAJ_stripeAPI.config import global_config

class Products_Data:
    def __init__(self):
        self.products = Products()

    def get_and_process_data(self):
        data = self.products.get_products()
        df = pd.DataFrame(data)
        return df

    def save_data(self, df):
        # df.to_csv(FILE_PATH, index=False)
        print(df)
