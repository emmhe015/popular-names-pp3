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

def get_names_data(names_list):
    """
    Get name input from the user and provide associated data if available.
    Args:
    - names_list: List of names to choose from.
    """
def get_names_data(names_list):
    """
    Get name input from the user and provide associated data if available.
    Args:
    - names_list: List of names to choose from.
    """
    while True:  # Start an infinite loop
        print("Please enter the name you would like to know more about.")
        print("The available names are:", ", ".join(names_list) + ".")
        print("Enter one name at a time.\n")

        data_str = input("Enter the name you have chosen here: ")

        if data_str in names_list:
            print(f"Data available for {data_str}: ")
            if data_str == "Noah": 
                print("from worksheetNoah")
            elif data_str == "Hugo":
                print("from worksheetHugo")
            elif data_str == "William":
                print("from worksheetWilliam")
            elif data_str == "Elsa":
                print("from worksheetElsa")
            elif data_str == "Vera":
                print("from worksheetVera")
            elif data_str == "Alma":
                print("from worksheetAlma")
            break 
        else:
            print("Invalid name. Please choose a name from the provided list.\n")


if __name__ == "__main__":
    names_list = ["Noah", "Hugo", "William", "Elsa", "Vera", "Alma"]  
    get_names_data(names_list) 