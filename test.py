# Imports
import os
import shutil

# Internal Import
from lib.accounts import accounts

# We have a specific address we want to inject
test_address = ""

# Test print
test_account = accounts("ethereum", test_address)
account_json = test_account.test_ret_account()

# insert the account_json into a test folder
print("---"*16)

# Get the path
path = os.getenv('APPDATA')+"\\Ledger Live"
print(f"Getting path: {path}")

# Check if app.json exists
file_list = os.listdir(path)
print(file_list)
if 'app.json' in file_list:
    print("app.json appears!")

# Copy app.json into corresponding file
appjson_copy = "copy_of_app.json"
dest = shutil.copy(f"{path}\\app.json", f"{path}\\{appjson_copy}")

result_file_list = os.listdir(path)
print(result_file_list)
if 'copy_of_app.json' in result_file_list:
    print("app.json appears!")