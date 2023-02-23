# Imports
import os
import shutil
from pprint import pprint
import json

# Internal Import
from lib.accounts import accounts
from lib.writer import inject_appjson, replace_appjson

# We shall use this as the testing file in the future

# We have a specific address we want to inject
test_address = "0x741aa7cfb2c7bf2a1e7d4da2e3df6a56ca4131f3"

# Test print
test_account = accounts("ethereum", test_address)
account_json = test_account.test_ret_account()

# insert the account_json into a test folder
print("---"*16)

# insert_data["data"]["accounts"][0]["data"] = 

test_dict = {
    "data": {
        "settings": {
            "hasCompletedOnboarding": True
        },
        "user": {
            "id": "_"
        },
        "accounts": [
            {
                "data": {
                    "id": "js:2:ethereum:0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045:",
                    "seedIdentifier": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
                    "xpub": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
                    "derivationMode": "",
                    "index": 0,
                    "freshAddress": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
                    "freshAddressPath": "0'/0'/0'/0/0",
                    "freshAddresses": [],
                    "name": "CS ETH",
                    "starred": True,
                    "balance": "0",
                    "blockHeight": 0,
                    "currencyId": "ethereum",
                    "operations": [],
                    "pendingOperations": [],
                    "swapHistory": [],
                    "unitMagnitude": 0,
                    "lastSyncDate": "0"
                }
            }
        ]
    }
}

test_dict['data']['accounts'][0]['data'] = account_json

inject_appjson(test_dict)