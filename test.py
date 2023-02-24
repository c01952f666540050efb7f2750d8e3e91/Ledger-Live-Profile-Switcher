# Imports
import os
import shutil
from pprint import pprint
import json

# Internal Import
from lib.accounts import accounts
from lib.appjson import appjson
from lib.writer import inject_appjson, replace_appjson

# We shall use this as the testing file in the future

# We have a specific address we want to inject
test_address = "0x4a4374cA885d590FcE52B1C6D7c500B3bAbAedb6"

# Test print
test_account = accounts("ethereum", test_address)
account_json = test_account.test_ret_account()

# insert the account_json into a test folder
print("---"*16)

# insert_data["data"]["accounts"][0]["data"] = 
test_obj = appjson()

# test_dict['data']['accounts'][0]['data'] = account_json
inject_data = test_obj.test_ret_appjson(account_json)
print(inject_data)

# print(test_obj)
inject_appjson(inject_data)
# Note BSC did not work - will need to check what's going on
# Maybe I'm just an idiot, i think so tbh