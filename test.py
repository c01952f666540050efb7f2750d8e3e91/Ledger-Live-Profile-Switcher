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
test_address = "0x777fDB494d0825669Bb50f5B1e075E18e671F8A7"
test_obj = appjson()

# This creates the account
test_account = accounts("bsc", test_address)

# We then create the json
account_json = test_account.ret_account()

# Test print of the account (not full appjson)
print(account_json)
print("---"*16)

# Test print appjson
print(test_obj.return_appjson())
print("---"*16)

# Add account
test_obj.add_account(account_json)

# Test Print
print(test_obj.return_appjson())
print("---"*16)

# Inject JSON
inject_appjson(test_obj.return_appjson())
