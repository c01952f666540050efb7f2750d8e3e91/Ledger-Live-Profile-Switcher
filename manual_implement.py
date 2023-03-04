# Imports

# Internal Import
from lib.accounts import accounts
from lib.appjson import appjson
from lib.writer import inject_appjson, replace_appjson
from lib.support import account_types

# # We have a specific address we want to inject
# test_address = "0x7BAf0fC50fa41E35365FB5B45D3d133EF41B9c77"

# # Test print
# test_account = accounts("ethereum", test_address)
# account_json = test_account.test_ret_account()

# # insert the account_json into a test folder
# We have a specific address we want to inject
test_address = "0x17d4b6e3ef4f7c9091b7296efea34648b6b2bf33"
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
