# autonomousAJ_stripeAPI/run.py
import inquirer
from autonomousAJ_stripeAPI.data import (
    Balances_Data, Charges_Data, Customers_Data, Invoices_Data, 
    Payment_Methods_Data, Payments_Data, Products_Data, 
    Refunds_Data, Subscriptions_Data, Webhooks_Data
)

def main_menu():
    questions = [
        inquirer.List("choice",
                      message="What type of data would you like to interact with?",
                      choices=["Balances", "Charges", "Customers", "Invoices", "Payment_Methods", "Payments", "Products", "Refunds", "Subscriptions", "Webhooks", "Exit"]),
    ]
    return inquirer.prompt(questions)["choice"]

def process_data(data_class):
    processor = data_class()
    processor.get_and_process_data()

def run():
    action_mapping = {
        "Balances": Balances_Data,
        "Charges": Charges_Data,
        "Customers": Customers_Data,
        "Invoices": Invoices_Data,
        "Payment_Methods": Payment_Methods_Data,
        "Payments": Payments_Data,
        "Products": Products_Data,
        "Refunds": Refunds_Data,
        "Subscriptions": Subscriptions_Data,
        "Webhooks": Webhooks_Data
    }

    while True:
        choice = main_menu()
        if choice == "Exit":
            break
        data_class = action_mapping.get(choice)
        if data_class:
            process_data(data_class)

if __name__ == "__main__":
    run()

