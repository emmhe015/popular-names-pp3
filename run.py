import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('top3_popular_names')

def get_names_data():
    """
    Get name input from the user.
    """
    print("Please enter the name you would like to know more about")
    print("The names are: Noah, Hugo, William, Elsa, Vera, Alma.")
    print("One name at a time.\n")

    data_str = input("Enter the name you have chosen here: ")
    print(f"The data provided is {data_str}")


get_names_data()