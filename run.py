import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('top3_popular_names')

boynames = SHEET.worksheet('boynames')
databoy = boynames.get_all_values()
print(databoy)

girlnames = SHEET.worksheet('girlnames')
datagirl = girlnames.get_all_values()
print(datagirl)