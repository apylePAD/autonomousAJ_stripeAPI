# autonomousAJ_stripeAPI/autonomousAJ_stripeAPI/api/balances.py
# Endpoint: balances
# URL: nan
import os
import requests
from .base import Stripe_API_Base
import stripe
from dotenv import load_dotenv

load_dotenv()

class Balances(Stripe_API_Base):
    def get_balances(self):
        
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        balance = stripe.Balance.retrieve()
        
        return balance