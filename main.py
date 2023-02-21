# Imports

# Internal Import
from lib.accounts import accounts

# We have a specific address we want to inject
test_address = "0x7BAf0fC50fa41E35365FB5B45D3d133EF41B9c77"

# Test print
test_account = accounts("ethereum", test_address)
account_json = test_account.test_ret_account()

# insert the account_json into a test folder