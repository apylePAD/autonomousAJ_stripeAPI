# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/auth.py
import os
from dotenv import load_dotenv
import stripe

load_dotenv()

class Get_Stripe_Client:
    def __init__(self):
        self.publishable_key = os.getenv("STRIPE_PUBLISHABLE_KEY")
        self.secret_key = os.getenv("STRIPE_SECRET_KEY")

    def get_stripe_client(self):
        publishable_key = self.publishable_key
        secret_key = self.secret_key

        stripe.api_key = secret_key
        return stripe.api_key, publishable_key

stripe_client = Get_Stripe_Client()